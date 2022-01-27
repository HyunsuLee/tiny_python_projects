#!/usr/bin/env python3
# bin/env 명령을 이용해 python3를 찾는 것.
"""
Author : Hyunsu Lee <hyunspookey@gmail.com>
Original Author : Ken Youens-Clark <kyclark@gmail.com>
Purpose : Say hello
"""


import argparse


def get_args():
    """Get name from command-line"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Lets play"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
