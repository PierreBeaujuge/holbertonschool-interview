#!/usr/bin/python3
"""
Log parsing
"""
if __name__ == '__main__':

    import sys

    def metrics(file_size, list_of_tuples):
        """function that computes metrics"""
        print("File size: {}".format(sum(file_size)))
        for kv in list_of_tuples:
            print("{}: {}".format(kv[0], kv[1]))

    file_size = []
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                    '404': 0, '405': 0, '500': 0}
    try:
        for line in sys.stdin:
            parse = line.split()
            # print(parse)
            file_size += [int(parse[8])]
            status_codes[parse[7]] += 1
            list_of_tuples = sorted([(k, v) for k, v in
                                     status_codes.items() if v != 0])
            if len(file_size) % 10 == 0:
                metrics(file_size, list_of_tuples)
    except KeyboardInterrupt:
        metrics(file_size, list_of_tuples)
        raise
