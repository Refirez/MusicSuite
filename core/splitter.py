"""Parse chapter lists and split a local audio file with FFmpeg."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Chapter:
    start: int
    title: str


_CHAPTER = re.compile(
    r"^\s*(?P<time>(?:\d{1,2}:)?\d{1,2}:\d{2})\s*(?:[-–—|]\s*)?(?P<title>.+?)\s*$"
)


def timestamp_to_seconds(value: str) -> int:
    parts = [int(part) for part in value.split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        hours = 0
    elif len(parts) == 3:
        hours, minutes, seconds = parts
    else:
        raise ValueError("Use mm:ss ou hh:mm:ss.")
    if seconds > 59 or minutes > 59:
        raise ValueError(f"Tempo inválido: {value}")
    return hours * 3600 + minutes * 60 + seconds


def parse_chapters(text: str) -> list[Chapter]:
    chapters = []
    for line in text.splitlines():
        match = _CHAPTER.match(line)
        if not match:
            continue
        title = match.group("title").strip(" -–—|")
        if title:
            chapters.append(Chapter(timestamp_to_seconds(match.group("time")), title))

    if not chapters:
        raise ValueError("Não encontrei capítulos. Exemplo: 01:23 Nome da música")
    if any(right.start <= left.start for left, right in zip(chapters, chapters[1:])):
        raise ValueError("Os tempos precisam estar em ordem crescente, sem repetição.")
    return chapters


def _safe_name(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(". ")
    return name[:120] or "Faixa"


def split_audio(
    source: str | Path,
    destination: str | Path,
    chapters: list[Chapter],
    audio_format: str = "mp3",
    bitrate: str = "320k",
    progress_callback=None,
) -> list[Path]:
    """Create one re-encoded audio file per chapter; FFmpeg must be installed."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg não foi encontrado. Instale-o e reinicie o aplicativo.")
    source = Path(source)
    if not source.is_file():
        raise ValueError("Selecione um arquivo de áudio existente.")
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    result = []
    for index, chapter in enumerate(chapters):
        output = destination / f"{index + 1:02d} - {_safe_name(chapter.title)}.{audio_format}"
        command = ["ffmpeg", "-y", "-ss", str(chapter.start), "-i", str(source)]
        if index + 1 < len(chapters):
            duration = chapters[index + 1].start - chapter.start
            command += ["-t", str(duration)]
        if audio_format == "mp3":
            # Mantém a capa incorporada no arquivo original, quando houver.
            command += [
                "-map", "0:a:0", "-map", "0:v?", "-map_metadata", "0",
                "-c:a", "libmp3lame", "-c:v", "copy",
                "-disposition:v:0", "attached_pic",
                "-metadata", f"title={chapter.title}",
            ]
        else:
            command += ["-map", "0:a:0", "-c:a", "pcm_s16le"]
        if audio_format == "mp3":
            command += ["-b:a", bitrate]
        command += [str(output)]
        completed = subprocess.run(command, capture_output=True, text=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        if completed.returncode:
            raise RuntimeError(completed.stderr.splitlines()[-1] or "FFmpeg não conseguiu separar o áudio.")
        result.append(output)
        if progress_callback:
            progress_callback((index + 1) / len(chapters))
    return result
