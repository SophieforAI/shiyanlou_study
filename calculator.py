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
                config[l[0].strip()]=float(l[1].strip())
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
        
        #return userdata

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self):
   
        Arg = Args()
        file_road = Arg.read_fileroad()
       
        cfg_file = file_road[0]
        user_file = file_road[1]
        config = Config(cfg_file).config
        userdata = UserData(user_file).userdata
        start_point= 3500
        try:
            all_user_output = []
            for key,value in userdata.items():
                key = int(key)
                value = int(value)
                insurance_prob = config['YangLao']+config['YiLiao']+config['ShiYe']+config['GongShang']+config['ShengYu']+config['GongJiJin']
                if value>=0 and value<config['JiShuL']:
                    insurance = config['JiShuL']*insurance_prob
                elif value >=config['JiShuL'] and value <= config['JiShuH']:
                    insurance = value* insurance_prob
                elif value>config['JiShuH']:
                    insurance = config['JiShuH']*insurance_prob
                sd_tax = value - insurance - start_point
                if sd_tax <=0 :
                    t = 0
                    num =0
                elif sd_tax>0 and  sd_tax<=1500:
                    t = 0.03
                    num = 0
                elif sd_tax>1500 and sd_tax<=4500:
                    t = 0.1
                    num = 105
                elif sd_tax>4500 and sd_tax<=9000:
                    t = 0.2
                    num = 555
                elif sd_tax>9000 and sd_tax<=35000:
                    t = 0.25
                    num = 1005
                elif sd_tax>35000 and sd_tax<=55000:
                    t = 0.30
                    num = 2755
                elif sd_tax>55000 and sd_tax<=80000:
                    t = 0.35
                    num = 5505
                elif sd_tax>80000:
                    t = 0.45
                    num = 13505

                final_tax =abs(sd_tax*t - num)
                salary_taxed = format(value-final_tax-insurance,".2f")
                insurance_2f = format(insurance,".2f")
                final_tax_2f = format(final_tax,'.2f')
                user_output = [key,value,insurance_2f,final_tax_2f,salary_taxed]
                all_user_output.append(user_output)
            return all_user_output 
        except:
            print("Parameter Error") 
        
    def export(self,export_file,default = 'csv'):
        result = self.calc_for_all_userdata()
        print(result)
        with open(export_file,'a') as f :
            writer = csv.writer(f)
            writer.writerows(result)
        
                
          

  

if __name__ =='__main__':
    Arg = Args()
    file_road = Arg.read_fileroad()
    out_put_file = file_road[2]
   
    Income = IncomeTaxCalculator()
    Income.export(out_put_file)
    
   # print(Config._read_config(cfg_file))
    
