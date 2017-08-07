#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def head_command(list_args):
    parser = argparse.ArgumentParser()
    head_init(parser)

    args = parser.parse_args(list_args[1:])
    number_of_rows = args.n

    try:
        filexpto = open(args.file_name, "r")
    except IOError:
        return "File does not exists\n"

    total_rows = filexpto.readlines()
    filexpto.close()

    return total_rows[:number_of_rows]

def head_init(parser):
    parser.add_argument("-n", required=False, type=int,
                action="store", default=10,
                help="number of rows that will be displayed")
    parser.add_argument("file_name")

if __name__ == '__main__':
    rows = head_command(sys.argv)

    for row in range(len(rows)):
        sys.stdout.write(rows[row])
