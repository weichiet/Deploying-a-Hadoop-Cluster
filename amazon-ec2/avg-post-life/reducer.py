#!/usr/bin/env python

from __future__ import division
import sys

def reducer():

    total_days = 0
    post_count = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        days, _ = data

        total_days += int(days)
        post_count += 1
        
    else:
        print('{}'.format(total_days/post_count))
        
if __name__ == "__main__":
    reducer()
