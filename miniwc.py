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

            res = []

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
    flags = []
    paths = []

    # extract flags and paths from inputs
    for index, arg in enumerate(arguments):
        if arg[0] == '-' and len(arg) > 1:
            flags.append(arg)
        else:
            paths = arguments[index:]
            break

    # handle each path via count() function
    for path in paths:
        try:
            counts = count(path, flags)
            # handle illegal flags
            if counts[0] == 'flag error':
                print('wc: illegal option -- {}'.format(counts[1][1:]))
            else:
                res = generate_output(counts)
                print(res)

        except TypeError:
            pass
