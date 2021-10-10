count_states = {
    "-l": False,
    "-w": False,
    "-c": False
}


def count(input):
    path = input[-1]
    flags = input[0:len(input)-1]

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


def generate_output(params):
    return "\t" + "\t".join(str(param) for param in params)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 5:
        print('We don’t handle that situation yet!')
    else:
        arguments = list(sys.argv[1:])
        try:
            counts = count(arguments)

            # handle illegal flags
            if counts[0] == 'flag error':
                print('wc: illegal option -- {}'.format(counts[1][1:]))
            else:
                res = generate_output(counts)
                print(res)

        except TypeError:
            pass
