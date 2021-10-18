count_states = {
    "-l": False,
    "-w": False,
    "-c": False
}


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
    parser.add_argument('-l', action='store_true', help='count lines in the file')
    parser.add_argument('-w', action='store_true', help='count words in the file')
    parser.add_argument('-c', action='store_true', help='count bytes in the file')

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

    if valid_args.l:
        flags.append('-l')
    if valid_args.w:
        flags.append('-w')
    if valid_args.c:
        flags.append('-c')

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
