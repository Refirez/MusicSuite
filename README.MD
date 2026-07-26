# MusicSuite

Aplicativo desktop para organizar áudio de vídeos e separar shows longos em faixas.

## Como usar

1. Instale as dependências: `python -m pip install -r requirements.txt`.
2. Garanta que o [FFmpeg](https://ffmpeg.org/) esteja disponível no `PATH`.
3. Execute `python app.py`.
4. Em **Splitter**, selecione um arquivo de áudio, escolha a pasta de saída e cole os capítulos, por exemplo:

```text
00:00 Abertura
04:32 Primeira música
08:15 Segunda música
```

O programa aceita `mm:ss` e `hh:mm:ss`, ignora linhas que não tenham timestamp e cria arquivos numerados.

Use o downloader apenas para conteúdo que você criou, possui ou tem autorização para baixar. Para fontes sem capítulos, copie a lista de tempos de uma descrição ou comentário e revise-a antes de exportar.
