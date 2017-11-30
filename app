#!/usr/bin/env python3
import json, sys

def process(data):
    return data

def main(args):
    assert len(args) == 2, 'main requires two arguments'
    infilename, outfilename = args
    with open(infilename, 'r') as infile:
        data = json.load(infile)
    data = process(data)
    with open(outfilename, 'w') as outfile:
        json.dump(data, outfile)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
