count_states = {
    "-l": False,
    "-w": False,
    "-c": False
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


# paths: [path1, path2, path3, ...]
# flags: ['-w', '-l']
def count(path, flags):
    try:
        with open(path, 'rb') as file:

            # get all counts
            bytes_read = file.read()
            line_count = bytes_read.count(b'\n')
            word_count = len(bytes_read.split())
            byte_count = len(bytes_read)

            # determine what contained in output by input flags
            flag_map = {
                '-l': line_count,
                '-w': word_count,
                '-c': byte_count
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
                    # '-m' in wc but not in wc.py
                    if flag == '-m':
                        # put msg into sys.exit() as a parameter
                        print('We don’t handle that situation yet!')
                        sys.exit()
                    # handle illegal flag
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

    except (FileNotFoundError, IsADirectoryError):
        print('wc: {}: open: No such file or directory'.format(path))


# params like: [2, 3, 'testinputs/text.txt']
def generate_output(params):
    return '\t' + '\t'.join(str(param) for param in params)


if __name__ == "__main__":
    import sys
    import argparse

    # No arguments: better to use sys.argv than argparse
    if len(sys.argv) <= 1:
        print('We don’t handle that situation yet!')
        sys.exit()

    parser = argparse.ArgumentParser(description='word count')

    # flag arguments
    parser.add_argument('-l', '--lines', action='store_true', help='count lines in the file')
    parser.add_argument('-w', '--words', action='store_true', help='count words in the file')
    parser.add_argument('-c', '--bytes', action='store_true', help='count bytes in the file')
    parser.add_argument('--v', '--version', action='store_true', help='version info')
    parser.add_argument('--h', action='store_true', help='help info')

    # path arguments
    parser.add_argument('paths', metavar='paths', type=str, nargs='*', help='file path')

    # use parse_known_args() to customize invalid flags error
    args = parser.parse_known_args()
    valid_args = args[0]
    invalid_args = args[1]

    if len(invalid_args):
        invalid_flag = invalid_args[0]
        if invalid_flag == '-m':
            print('We don’t handle that situation yet!')
            sys.exit()
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
    if valid_args.v:
        flags.append('-v')
    if valid_args.h:
        flags.append('-h')

    # 'totals' line at bottom
    totals = []

    # handle each path via count() function
    for path in paths:
        try:
            # save figures for 'totals' line
            counts = count(path, flags)
            figures = counts[0: len(counts)-1]
            totals.append(figures)

            # handle illegal flags
            output = 'wc: illegal option -- {}'.format(counts[1][1:]) if counts[0] == 'flag error' else generate_output(counts)
            print(output)

        except TypeError:
            pass

    # total_res for the 'totals' line'
    if len(paths) > 1:
        total_res = [0] * len(totals[0])
        for nums in totals:
            for index, num in enumerate(total_res):
                total_res[index] += nums[index]
        total_res = [*total_res, 'total']
        print('\t' + '\t'.join(str(item) for item in total_res))
