__author__ = 'jzs'
__date__='2017/1/13'
import ConfigParser,os

def configini(key,value):
    ini=ConfigParser.ConfigParser()
    ini.read(os.getcwd()+'\python.ini')
    url=ini.get(key,value)
    return url
