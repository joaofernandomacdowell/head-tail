#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cannot combine -r with -n. When -r is used, the whole file is printed on screen

import sys
import argparse


def tail_command(list_args):
    parser = argparse.ArgumentParser()
    tail_init(parser)

    args = parser.parse_args(list_args[1:])
    number_of_rows = args.n

    if args.r:
        filexpto = open(args.file_name, "r")
        rows = filexpto.readlines()
        rows.reverse()
        filexpto.close()

        return rows

    try:
        filexpto = open(args.file_name, "r")
    except IOError:
        return "File does not exists\n"

    else:
        rows = filexpto.readlines()
        total_rows = len(rows)
        starting_point = total_rows - number_of_rows
        filexpto.close()

    return rows[starting_point:total_rows]

def tail_init(parser):
    parser.add_argument("-n", required=False, type=int,
                action="store", default=10,
                help="number of rows that will be displayed")
    parser.add_argument("-r", required=False, action="store_true")
    parser.add_argument("file_name")

if __name__ == "__main__":
    rows = tail_command(sys.argv)
    for row in rows:
        sys.stdout.write(row)
