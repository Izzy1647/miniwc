def count(path):
    with open(path, 'rb') as file:
        # The output is linecount wordcount bytecount filepath(each separated by
        # tab characters)
        bytes_read = file.read()
        line_count = bytes_read.count(b'\n')
        word_count = len(bytes_read.split())
        byte_count = len(bytes_read)

        return [line_count, word_count, byte_count, path]


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print('Invalid input.')
    else:
        path = sys.argv[1]
        counts = count(path)
        output = "\t".join(str(count) for count in counts)
        print(output)
