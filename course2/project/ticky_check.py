#!/usr/bin/env python3
import re
import csv
import operator
import sys

per_user = {}
errors = {}
pattern = r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$"

logfile = 'syslog.log'
f = open(logfile, 'r')

error_file = 'error_message.csv'
user_file = 'user_statistics.csv'

for log in f:
    result = re.search(pattern, log)

    if result.group(2) not in errors.keys():
        errors[result.group(2)] = 0
    errors[result.group(2)] += 1

    if result.group(3) not in per_user.keys():
        per_user[result.group(3)] = {}
        per_user[result.group(3)]["INFO"] = 0
        per_user[result.group(3)]["ERROR"] = 0

    if result.group(1) == "INFO":
        per_user[result.group(3)]["INFO"] += 1
    elif result.group(1) == "ERROR":
        per_user[result.group(3)]["ERROR"] += 1

errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items())

f.close()
errors.insert(0, ('Error', 'Count'))

f = open(error_file, 'w')
for error in errors:
    a, b = error
    f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(user_file, 'w')
f.write('Username, INFO, ERROR\n')
for stats in per_user:
    a, b = stats
    f.write(str(a)+','+str(b["INFO"])+str(b["ERROR"])+'\n')
