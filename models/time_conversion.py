import re

def time_to_milliseconds(time_str):
    h, m, s = time_str.split(':')
    s, ms = s.split('.')
    return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000 + int(ms) * 10

def time_code_to_milliseconds(time_code):
    time_re = re.compile("(?P<start_time>\d*:\d*:\d*.\d*).wav")
    return time_to_milliseconds(time_re.findall(time_code)[0])