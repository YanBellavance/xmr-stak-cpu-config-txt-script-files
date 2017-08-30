#!/usr/bin/python

import sys, getopt
from tempfile import mkstemp
from shutil import move
#from os import fdopen, remove
import os
import io
import re

from pyquery import PyQuery as pq
from lxml import etree
import urllib

#./setupConfig.py -i $CONFIG_TXT_INPUT -o $CONFIG_TXT_OUTPUT  -c $NUM_CORES -u $USER_ID

def main(argv):
  username = 'ubuntu'
  password = ' -pw BeCarFullIfYouPutYOurPasswordHere'
  usePassword = 'no'
  ipv4 = 'DEAD_COW_TOE_KINS'
  cloudCmd = 'ssh'
  
  #***TOODO**
  #replace \ chars with / when coming from cli cuz some people dont know how to program well 
  # aws KEY FOR UBUNTU
  ssh_key_path = 'C:/path/to/your/ssh/key/keyfile.ppk'    
  scripts_path = 'C:/path/to/xmr-stak-cpu-config-txt-script-files/'
  d = pq(filename=scripts_path+'htmlData.html')
  ipList = ['104.197.148.123','104.197.92.235','104.197.215.183','107.178.219.218','130.211.117.72','104.154.81.232','104.197.223.113','104.197.121.87']
  # ipList = d('tbody').find('tr').find('td').not_('.EFB').find('div').text().split(' ')
  ipListProtected = ['54.172.172.236','52.87.166.170','52.90.25.125','52.70.26.4','52.201.254.40']
  print 'ip list  : '+', '.join(ipList)
  print 'protected'
  print 'ip list  : '+', '.join(ipListProtected)
  ipList = set(ipList) - set(ipListProtected)
  print 'new'
  print 'ip list  : '+', '.join(ipList)
  try:
    opts, args = getopt.getopt(argv,"hi:m:s:u:p")
  except getopt.GetoptError:
    print 'setupConfig.py -ip <ipv4> -m <cloudCmd>  -ssh <ssh>'
    print '-m <cloudCmd> == -m [install,fix,upd,launch,ssh]'
    print 'Or Enter any custom script name with optional args'
    print '-m <cloudCmd> == -m newScript.sh -o option'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'setupConfig.py -ip <ipv4> -m <cloudCmd>  -ssh <ssh>'
      print '-m <cloudCmd> == -m [install,fix,upd,launch,ssh]'
      sys.exit()
    elif opt == '-i':
      ipv4 = arg
    elif opt == '-m':
      cloudCmd = arg      
    elif opt == '-s':
      ssh_key_path = arg
    elif opt == '-u':
      username = arg
    elif opt == '-p':
      usePassword = 'yes'

  fullCloudCmd = ''
  if ipv4 <> 'DEAD_COW_TOE_KINS':
    ipList = [ipv4]
        
  for ip_entry in ipList:
    print 'ip iter' + ip_entry
    if cloudCmd == 'reboot':
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + '/reboot.sh '
    elif cloudCmd == 'install':
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + '/installAndLaunch.sh '
    elif cloudCmd == 'fix':                                                                                          
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + '/kill_FixMalloc_UpdConfig_Launch.sh '
    elif cloudCmd == 'upd':                                                                                          
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + '/kill_UpdConfig.sh '
    elif cloudCmd == 'launch':                                                                                       
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + '/launchOnly.sh '
    elif cloudCmd == 'ssh':                                                                                          
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path                         
    #means we have a custom script to execute                                            
    elif cloudCmd <> '':  
      fullCloudCmd = 'putty.exe -ssh ' + username + '@' + ip_entry + ' -i ' + ssh_key_path + ' -m ' + scripts_path + cloudCmd
    else:
      print 'm undefined. This should not have happenned'
      print '-m <cloudCmd> == -m [install,fix,upd,launch,ssh]'
      print 'Or Enter any custom script name with optional args'
      print '-m <cloudCmd> == -m newScript.sh -o option'
      sys.exit(2)

    if usePassword <> 'yes':
      password =''
    os.system('start '+ fullCloudCmd + password)

  
  print 'ip is is :"', ipv4
  print 'command is :"', cloudCmd
  print 'fullCloudCmd is :"', fullCloudCmd
  print 'ssh_key_path is :"', ssh_key_path
  



if __name__ == "__main__":
  main(sys.argv[1:])

