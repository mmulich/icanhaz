# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse


def haz(**kw):
    print('{pronoun} can haz {noun}?'.format(**kw))

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('noun', nargs='?', default='gitburger')
    parser.add_argument('pronoun', nargs='?', default='we')
    args = parser.parse_args(argv)
    haz(**vars(args))
    return 0


if __name__ == '__main__':
    main()
