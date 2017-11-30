#!/usr/bin/env python3
from functools import wraps
import json, sys

def json_app(app):
    @wraps(app)
    def inner(*args, **kwargs):
        clargs = sys.argv[1:]
        assert len(clargs) >= 2, 'json_app requires two command line arguments: inputfilename and outputfilename'
        infilename, outfilename = clargs
        with open(infilename, 'r') as infile:
            data = json.load(infile)
        data = app(data)
        with open(outfilename, 'w') as outfile:
            json.dump(data, outfile)
        return data
    return inner

@json_app
def my_app(data):
    return data

if __name__ == '__main__':
    my_app()
