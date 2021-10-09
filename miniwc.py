def count(path):
    try:
        with open(path, 'rb') as file:
            # The output is linecount wordcount bytecount filepath(each separated by
            # tab characters)
            bytes_read = file.read()
            line_count = bytes_read.count(b'\n')
            word_count = len(bytes_read.split())
            byte_count = len(bytes_read)

            return [line_count, word_count, byte_count, path]

    except FileNotFoundError:
        print('wc: {}: open: No such file or directory'.format(path))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print('We don’t handle that situation yet!')
    else:
        path = sys.argv[1]
        try:
            counts = count(path)
            output = "\t".join(str(count) for count in counts)
            print(output)
        except TypeError:
            pass
