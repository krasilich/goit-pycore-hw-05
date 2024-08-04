from typing import Iterable


def load_logs_generator(path: str) -> Iterable[str]:
    """
    Load logs from the file and yield one line at a time.
    :param path: str
    :return: generator
    """
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()


def parse_log_line(line: str) -> dict:
    """
    Parse a log line and return a dictionary with the log data.
    :param line: str
    :return: dict
    """
    parts = line.split(' ')
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': ' '.join(parts[3:])
    }


def count_logs_by_level(logs: Iterable[str]) -> dict:
    """
    Count logs by level.
    :param logs: Iterable
    :return: dict
    """
    counts = {}
    for log in logs:
        level = parse_log_line(log)['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts


def display_log_counts(counts: dict):
    """
    Display the log counts.
    Format putput as table with header Level and Count.
    Should consider the longest level string length in the logs.
    :param counts: dict
    :return: None
    """
    if not counts:
        print('No logs found.')
        return

    max_level_len = max(len(level) for level in counts)
    print(f'{"Level":<{max_level_len}} | Count')
    print('-' * (max_level_len + 8))
    for level, count in counts.items():
        print(f'{level:<{max_level_len}} | {count}')


def display_filtered_logs(logs: Iterable[str], level: str):
    """
    Display logs filtered by level.
    :param logs: Iterable
    :param level: str
    :return: None
    """
    for record in filter(lambda log: parse_log_line(log)['level'] == level.upper(), logs):
        print(record)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print('Usage: python task3.py <log_file> [log_level]')
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    # Check if the file exists
    try:
        with open(file_path, 'r'):
            pass
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        sys.exit(1)  # Non-zero exit code for file not found

    # Logs generator
    logs = load_logs_generator(file_path)

    # Display log counts
    display_log_counts(count_logs_by_level(logs))

    # Filter logs by level
    if level:
        display_filtered_logs(load_logs_generator(file_path), level)  # Reload logs to display from the start
