# coding=utf-8
import sys, os
import time
for i in range( 100 ):
    time.sleep( .5 )
    sys.stdout.write( "File transfer progress :[%3d] percent complete!\r" % i )
    #T_sys.stdout.flush()