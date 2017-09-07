# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:10:25 2017

@author: weich
"""

#!/usr/bin/env python

import sys

def reducer():

    mentions = 0
    old_date = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 3:
            continue

        sub, this_date, mentioned = data

        if old_date and old_date != this_date:

            print("{}\t{}".format(old_date, mentions))
            mentions = 0

        old_date = this_date
        mentions += int(mentioned)
    else:
        print("{}\t{}".format(old_date, mentions))


if __name__ == "__main__":
    reducer()