#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import time,os
def logPrint(filename1):
    # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    logfilename=os.getcwd()+'\logs\\'+filename1
    logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename=logfilename,
            )
