# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:22:56 2017

@author: weich
"""
#!/usr/bin/python
#!/usr/bin/env python3


from __future__ import division
import sys

comment_count = 0
ups_count = 0
length_sum = 0
old_user = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 3:
		continue

	this_user, ups, length = data

	if old_user and old_user != this_user:

		print("{}\t{}\t{}\t{}".format(old_user, comment_count,
								  ups_count/comment_count,
								  length_sum/comment_count))

		ups_count = 0
		length_sum = 0
		comment_count = 0

	old_user = this_user
	comment_count += 1
	ups_count += int(ups)
	length_sum += int(length)

if old_user != None:
	print("{}\t{}\t{}\t{}".format(old_user, comment_count,
							  ups_count/comment_count,
							  length_sum/comment_count))


