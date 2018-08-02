#!usr/bin/env python3
import sys 
import csv


class cfg_input:
    def __init__(self,filename):
        self._filename = filename
        
    def writecfg(self):
        with open(self._filename,'a') as file:
            file.write('JiShuL = 2193.00')
            file.write('JiShuH = 16446.00')
            file.write('YangLao = 0.08')
            file.write('YiLiao = 0.02')
            file.write('ShiYe = 0.005')
            file.write('GongShang = 0')
            file.write('ShengYu = 0')
            file.write('GongJiJin = 0.06')





class csv_input:
    def __init__(pass):
        pass
    def readcsv(self):
        return



class Calculator:
    def __init__(self):
        pass
    def tax_calculator(self):
        return (id,sqgz,sbje,gsje,shgz)

if __name__ ='__main__':
    cfg_write = cfg_input('/home/shiyanlou/test.cfg')
    cfg_write.writecfg()
