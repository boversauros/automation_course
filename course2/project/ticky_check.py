#!/usr/bin/env python3
import re
import operator
import sys


def search_pattern(pattern, line):
    result = re.search(pattern, line)
    # egde case
    if result == None:
        return None
    # return only the captured group
    return result.group(1)


# Parse the syslog.log file into two different dictionarys. Use for loops to count each occurence of each regex pattern above
def parse_log(syslog):
    # Dictionaries to keep count of each number and user interaction
    error = {}
    per_user = {}
    info_pattern = r"ticky: INFO ([\w ]*)"
    error_pattern = r"ticky: ERROR ([\w'? ]*)"
    user_pattern = r"\((.*)\)"

    with open(syslog, 'r') as syslog:
        for line in syslog.readlines():
            res_err = search_pattern(error_pattern, line)
            res_info = search_pattern(info_pattern, line)
            res_user = search_pattern(user_pattern, line)
            # Check if the name of the user is already in the per_user dictionary
            if res_user not in per_user:
                per_user[res_user] = {'INFO': 0, 'ERROR': 0}
            # Check if the kind of error is already in the error dictionary
            elif res_err != None and res_err not in error:
                error[res_err] = 0
            # If there is an error
            elif res_err != None:
                # increment the value of key 'ERROR' by 1 'INFO' in per_user dictionary
                per_user[res_user]['ERROR'] += 1
                # increment the type of that error in the error dictionart
                error[res_err] += 1
            # If there is an info string only increment the value of key 'INFO' in per_user dictionary
            elif res_info != None:
                per_user[res_user]['INFO'] += 1
        syslog.close()
    return (error, per_user)


# Generate report function to sort and write error into a csv report file

def generate_error_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.write("Error"+', ' + "Count" + '\n')
        for k in sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(k[0])+', '+str(k[1])+'\n')
        f.close()


# Generate report function to sort and write user stats into a csv report file
def generate_user_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.write("NAME"+', '+"INFO"+', '+"ERROR" + '\n')
        for k in sorted(dictionary.items(), key=operator.itemgetter(0)):
            f.write(
                str(k[0])+', '+str(k[1]['INFO'])+', '+str(k[1]['ERROR']) + '\n')
        f.close()


if __name__ == "__main__":
    # Calling definitions
    syslog = sys.argv[1]
    error, per_user = parse_log(syslog)
    generate_error_report(
        error, 'error_message.csv')
    generate_user_report(
        per_user, 'user_statistics.csv')
    sys.exit(0)
