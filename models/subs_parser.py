import re

sub_re = re.compile(r"Dialogue: (?P<layer>\d*),(?P<start>\d*:\d*:\d*.\d*),(?P<end>\d*:\d*:\d*.\d*),(?P<name>.*)(?:,)(?P<margins>(\d,\d,\d)),,(?P<text>.*)")
sub_text_re = re.compile(r"( ?\\N ?| ?\{[^\{}]+} ?)")

def path_to_subs_list(file_path: str):
    subs_file = open(file_path).read()

    subs_list = []
    for m in sub_re.finditer(subs_file):
        sub = dict(m.groupdict())
        sub |= {"text": sub_text_re.sub(" ", sub["text"])}
        subs_list.append(sub)

    return subs_list
