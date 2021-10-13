import re

# https://gist.github.com/allooshcode/8fc7873c9f351f3168f9a2d3f881b9e5


def show_time_of_pid(line):
    pattern = r"^([\w]+ [\d]+ [\d]+:[\d]+:[\d]+) [\w. ]+\[(\d{5})\]"
    result = re.search(pattern, line)
    return "{} pid:{}".format(result[1], result[2])


# Jul 6 14:01:23 pid:29440
print(show_time_of_pid(
    "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))
