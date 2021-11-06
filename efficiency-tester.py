from os import listdir
from os.path import isfile, join
# import subprocess

from subprocess import Popen, PIPE, STDOUT


def generate_report(directory):
    files = [join(path, f) for f in listdir(directory) if (isfile(join(directory, f)) and (f != '.DS_Store'))]

    for file in files:
        cmd = f'time python3 wc.py {file}'
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        raw_timing = p.stdout.read().decode("utf-8")
        print(raw_timing, file, '\n')


















if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('We don’t handle that situation yet!')
        sys.exit()

    # path that contains test files
    path = sys.argv[1]

    generate_report(path)








