#!/usr/bin/python3
"""
Reads stdin line by line and compute metrics
which are then written out to stdout
"""
from datetime import datetime
import signal
import sys

line_count = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_dict = {}
size = 0


def line_parser(line):
    """
    performing parsing the log
    """
    args = line.split(' ')
    return args


def validate_ip(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for part in ip:
        if not part.isdigit():
            return False
        int_part = int(part)
        if int_part < 0 or int_part > 255:
            return False
    return True


def validate_date(*args):
    date = ''.join(args)
    date = date.replace('[', '')
    date = date.replace(']', '')
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d%H:%M:%S.%f')
        return True
    except Exception as e:
        return False


def validate_codes(code):
    try:
        if int(code) in status_codes:
            return True
        return False
    except Exception as e:
        return False


def validate_size(size):
    try:
        size = int(size)
        return True if 1 <= size <= 1024 else False
    except Exception as e:
        return False


def validate_hyphen(arg):
    if arg == '-':
        return True
    else:
        return False


def print_metrics(size, status_dict):
    print("File size: {}".format(size))
    if status_dict:
        for k, v in sorted(status_dict.items()):
            if v != 0:
                print("{}: {}".format(k, v))


try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        args = line_parser(line)
        if (validate_ip(args[0]) and
            validate_hyphen(args[1]) and
            validate_date(args[2], args[3]) and
            validate_codes(args[7])
            and validate_size(args[8])):
            # confirms that log line format is okay
            prev_size = int(args[8])
            size += prev_size
            current_code = args[7]
            if current_code.isdigit():
                current_code = int(current_code)
                if current_code in status_dict:
                    status_dict[current_code] += 1
                else:
                    status_dict[current_code] = 1
        else:
            continue
        if line and (line_count != 0 and line_count % 10 == 0):
            print_metrics(size, status_dict)
            status_dict = dict.fromkeys(status_dict, 0)
        line_count += 1
except KeyboardInterrupt as err:
    print_metrics(size, status_dict)
