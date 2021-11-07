count_states = {
    "-l": False,
    "-w": False,
    "-c": False,
    "-m": False,
    "-L": False
}


def print_version():
    print(
        '''
        wc (GNU coreutils) 9.0
        Copyright (C) 2021 Free Software Foundation, Inc.
        License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        
        Written by Paul Rubin and David MacKenzie.
        
        '''
    )
    sys.exit()


def print_help():
    print(
        '''
        Usage: gwc [OPTION]... [FILE]...
          or:  gwc [OPTION]... --files0-from=F
        Print newline, word, and byte counts for each FILE, and a total line if
        more than one FILE is specified.  A word is a non-zero-length sequence of
        printable characters delimited by white space.
        
        With no FILE, or when FILE is -, read standard input.
        
        The options below may be used to select which counts are printed, always in
        the following order: newline, word, character, byte, maximum line length.
          -c, --bytes            print the byte counts
          -m, --chars            print the character counts
          -l, --lines            print the newline counts
              --files0-from=F    read input from the files specified by
                                   NUL-terminated names in file F;
                                   If F is - then read names from standard input
          -L, --max-line-length  print the maximum display width
          -w, --words            print the word counts
              --help     display this help and exit
              --version  output version information and exit
        
        GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
        Report any translation bugs to <https://translationproject.org/team/>
        Full documentation <https://www.gnu.org/software/coreutils/wc>
        or available locally via: info '(coreutils) wc invocation'
        '''
    )
    sys.exit()


def count_from_bytes(bytes, flags, path):
    # get all counts
    line_count = bytes.count(b'\n')
    word_count = len(bytes.split())
    byte_count = len(bytes)
    character_count = byte_count

    lines = bytes.split(b'\n')
    max_line_length = len(max(lines, key=len))

    # determine what contained in output by input flags
    flag_map = {
        '-l': line_count,
        '-w': word_count,
        '-c': byte_count,
        '-m': character_count,
        '-L': max_line_length
    }

    # handle version & help
    if '-v' in flags:
        print_version()
    if '-h' in flags:
        print_help()

    for flag in flags:
        if flag in count_states:
            count_states[flag] = True
        else:
            return ['flag error', flag]

    # generate output
    res = []
    if len(flags) == 0:
        # no flags, show'em all
        res = [line_count, word_count, byte_count]
    else:
        for k in flag_map:
            if count_states[k]:
                res.append(flag_map[k])

    return [*res, path]


def handle_input():
    parser = argparse.ArgumentParser(description='word count')

    # flag arguments
    parser.add_argument('-l', '--lines', action='store_true', help='count lines in the file')
    parser.add_argument('-w', '--words', action='store_true', help='count words in the file')
    parser.add_argument('-c', '--bytes', action='store_true', help='count bytes in the file')
    parser.add_argument('-m', '--chars', action='store_true', help='count characters in the file')
    parser.add_argument('-L', '--max-line-length', action='store_true', help='length of longest line')

    parser.add_argument('--v', '--version', action='store_true', help='version info')
    parser.add_argument('--h', action='store_true', help='help info')

    # path arguments
    parser.add_argument('paths', metavar='paths', type=str, nargs='*', help='file path')

    parser.add_argument('--files0-from', metavar='files0', type=str, help='files0')

    # use parse_known_args() to customize invalid flags error
    args = parser.parse_known_args()
    valid_args = args[0]
    invalid_args = args[1]

    # handle valid_args.files0_from
    if valid_args.files0_from:
        file0 = valid_args.files0_from
        try:
            with open(file0) as f:
                content = f.read()
                if content.find('\x00') == -1:
                    print('wc: \'{}\' : No such file or directory'.format(content))
                # else:

        except FileNotFoundError:
            print('wc: cannot open \'{}\' for reading: No such file or directory'.format(file0))
        except IsADirectoryError:
            print('wc: {}: read error: Is a directory'.format(file0))

        print(valid_args.files0_from)
        sys.exit()

    if len(invalid_args):
        invalid_flag = invalid_args[0]
        print('wc: illegal option -%s\n' % invalid_flag)
        print('usage: wc [-clw] [file ...]\n')
        sys.exit()

    flags = []
    paths = valid_args.paths

    if valid_args.lines:
        flags.append('-l')
    if valid_args.words:
        flags.append('-w')
    if valid_args.bytes:
        flags.append('-c')
    if valid_args.chars:
        flags.append('-m')
    if valid_args.v:
        flags.append('-v')
    if valid_args.h:
        flags.append('-h')
    if valid_args.max_line_length:
        flags.append('-L')

    # 'totals' line at bottom
    totals = []

    # handle each path via count_from_bytes() function
    for path in paths:
        try:
            with open(path, 'rb') as file:
                counts = count_from_bytes(file.read(), flags, path)
                figures = counts[0: len(counts) - 1]
                totals.append(figures)

                # handle illegal flags
                output = 'wc: illegal option -- {}'.format(counts[1][1:]) \
                    if counts[0] == 'flag error' \
                    else generate_output(counts)
                print(output)
        except (FileNotFoundError, IsADirectoryError):
            print('wc: {}: open: No such file or directory'.format(path))

    # total_res for the 'totals' line'
    if len(paths) > 1:
        total_res = [0] * len(totals[0])
        for nums in totals:
            for index, num in enumerate(total_res):
                total_res[index] += nums[index]
        total_res = [*total_res, 'total']
        print('\t' + '\t'.join(str(item) for item in total_res))


def generate_output(params):
    return '\t' + '\t'.join(str(param) for param in params)


if __name__ == "__main__":
    import sys
    import argparse

    # No arguments: better to use sys.argv than argparse
    if len(sys.argv) <= 1:
        std_in = sys.stdin.buffer.read()
        params = count_from_bytes(std_in, [], '')
        res = generate_output(params)
        sys.exit(res)

    handle_input()
