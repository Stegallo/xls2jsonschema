#!/usr/bin/python

import sys
from generateschema import x


if len(sys.argv) < 4:
    print 'missing arguments. only', len(sys.argv)-1, 'found. 3 needed.'
else:
    print "The arguments are: " , str(sys.argv)

#TODO
f_obj=open(sys.argv[1])
x(f_obj)
# print f_obj
# reader = csv.DictReader(f_obj, delimiter=',')
# for line in reader:
#     print line
#     # break

# print reader[0]

#generateschema
#generateexample
print 'Terminated'
