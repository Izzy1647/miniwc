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

    except FileNotFoundError:
        print('wc: {}: open: No such file or directory'.format(path))


# params like: [2, 3, 'testinputs/etest.txt']
def generate_output(params):
    return "\t" + "\t".join(str(param) for param in params)


if __name__ == "__main__":
    import sys
    arguments = list(sys.argv[1:])
    if len(arguments) == 0:
        print('We don’t handle that situation yet!')
        sys.exit()

    flags = []
    paths = []

    # extract flags and paths from inputs
    for index, arg in enumerate(arguments):
        if arg[0] == '-' and len(arg) > 1:
            flags.append(arg)
        else:
            paths = arguments[index:]
            break

    totals = []  # for the 'totals' line

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
    if len(totals) > 1:
        total_res = [0] * len(totals[0])
        for nums in totals:
            for index, num in enumerate(total_res):
                total_res[index] += nums[index]
        total_res = [*total_res, 'total']
        print("\t" + "\t".join(str(item) for item in total_res))
