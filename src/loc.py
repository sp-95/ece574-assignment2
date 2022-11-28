import re


def count_physical_loc(file):
    with open(file) as f:
        lines = list(filter(None, (line.strip() for line in f.readlines())))

    non_comments = list(filter(lambda l: not l.startswith("#"), lines))
    non_comments = list(map(lambda l: re.sub(r"(?<!['\"])#.*", "", non_comments)))

    parsed_list = []
    found = False
    for l in non_comments:
        if not found:
            parsed_list.append(l)
        else:
            parsed_list[-1] += l
        if l.count("\"\"\"") % 2 == 1:
            found = not found
    
    return len(parsed_list)
