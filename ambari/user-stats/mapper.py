# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:22:37 2017

@author: weich
"""
#!/usr/bin/python
#!/usr/bin/env python3

import csv
import sys


for row in sys.stdin:
	row = row.strip()
	data = next(csv.reader([row], delimiter='\t'))

	if len(data) != 8:
	   continue

	_, author, body, _, ups, downs, _, _ = data 

	print('{}\t{}\t{}'.format(author, ups, len(body.split(' '))))

