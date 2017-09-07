#!/usr/bin/env python

from datetime import datetime
import sys
import xml.etree.ElementTree as ET

def mapper():
    for row in sys.stdin:
        row = row.strip()
        if not row.startswith('<row'):
            continue
        
        parser = ET.fromstring(row)
        first = parser.get('CreationDate')
        last = parser.get('LastActivityDate')

        first_dt = datetime.strptime(first, '%Y-%m-%dT%X.%f')
        last_dt = datetime.strptime(last, '%Y-%m-%dT%X.%f')

        dt = last_dt - first_dt

        print('{}\t{}'.format(dt.days, 1))
        
        # Maybe this will help with memory
        del parser

if __name__ == "__main__":
    mapper()
