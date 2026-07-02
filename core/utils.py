from datetime import timedelta


def seconds_to_time(seconds: int):

    if not seconds:
        return "--:--"

    return str(timedelta(seconds=seconds))


def format_views(views):

    if not views:
        return "0"

    if views >= 1_000_000:
        return f"{views/1_000_000:.1f} M"

    if views >= 1_000:
        return f"{views/1_000:.1f} mil"

    return str(views)


def format_date(date):

    if not date:
        return "-"

    return f"{date[6:8]}/{date[4:6]}/{date[:4]}"