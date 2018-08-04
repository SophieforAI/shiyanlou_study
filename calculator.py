#!/usr/bin/env python3
import sys 
import csv


class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
        
    def read_fileroad(self):
        index0 = self.args.index('-c')+1
        index1 = self.args.index('-d')+1
        index2 = self.args.index('-o')+1
        return([self.args[index0],self.args[index1],self.args[index2]])
        
            
class Config(object):
    def __init__(self,cfgfile):
        self.config = self._read_config(cfgfile)
    def _read_config(self,cfgfile):
        config = {}
        with open(cfgfile,'r') as file:
            for line in file:
                l = line.strip().split('=')
                config[l[0].strip()]=l[1].strip()
       
        return config

class UserData(object):
    def __init__(self,userfile):
        self.userdata = self._read_users_data(userfile)
    def _read_users_data(self,userfile):
        userdata ={}
        with open(userfile,'r') as file:
            for line in file:
                l = line.strip().split(',')
                userdata[l[0]]=l[1]
        
        return userdata

class IncomeTaxCalculator(UserData):
    def calc_for_all_userdata(self):
        userdata = self.userdata
        for key,value in userdata.items():
            key = int(key)
            value = int(value)
        
        
        print(userdata)
        
    def export(self,export_file,default = 'csv'):
        result = self.calc_for_all_userdata()
        print(result)
        with open(export_file,'w') as f :
           
            write = csv.write(f)
            write.writerows(result)

  

if __name__ =='__main__':
    Arg = Args()
    file_road = Arg.read_fileroad()
    cfg_file = file_road[0]
    user_file = file_road[1]
    UserData = UserData(user_file)
    Income = IncomeTaxCalculator(user_file)
    Income.calc_for_all_userdata()
   # Config = Config(cfg_file)
   # print(Config._read_config(cfg_file))
    
