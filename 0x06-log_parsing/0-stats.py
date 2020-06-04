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
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parse = line.split()
            # print(parse)
            try:
                file_size += [int(parse[-1])]
            except:
                pass
            try:
                status_code = parse[-2]
                if status_code in status_codes.keys():
                    status_codes[status_code] += 1
            except:
                pass
            list_of_tuples = sorted([(k, v) for k, v in
                                     status_codes.items() if v != 0])
            if line_count % 10 == 0:
                metrics(file_size, list_of_tuples)
        metrics(file_size, list_of_tuples)
    except KeyboardInterrupt:
        metrics(file_size, list_of_tuples)
        raise