# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse


def haz(**kw):
    print('i can has {noun}'.format(**kw))

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('noun')
    args = parser.parse_args(argv)
    haz(**vars(args))
    return 0


if __name__ == '__main__':
    main()
