#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def mapper():
    for row in sys.stdin:
        row = row.strip()
        if not row.startswith('<row'):
            continue
        
        parser = ET.fromstring(row)
        views = parser.get('ViewCount')
        score = parser.get('Score')
        answers = parser.get('AnswerCount')

        if answers:
            print('{}\t{}'.format(views, score))

        # Maybe this will help with memory
        del parser

if __name__ == "__main__":
    mapper()
