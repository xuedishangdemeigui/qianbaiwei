from datetime import datetime


def parse_unix_time(unix_time: any) -> str:
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
