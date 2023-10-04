
#   https://www.youtube.com/watch?v=alSgAbyC7K8

import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m", ['filename', 'message'])


def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])
 
myfunction('hey', True,19,'wow', KEYONE="TEST", KEYTWO=7)


