#!/bin/sh
# putty.exe -ssh ubuntu@123.234.124.213 -m C:\path\to\your\shell-script\launchOnly.sh -i C:\path\to\your\ssh-key.ppk

DIRECTORY="xmr-stak-cpu"


if [ -d $DIRECTORY ]; then 

  cd
  #kill xmr-stak-cpu
  sudo ps -ef | grep -v grep | grep xmr-stak-cpu | awk '{print "kill " $2}'| sh -x

  #@reboot sudo /home/$USER/xmr-stak-cpu/bin/xmr-stak-cpu-config-txt-script-files/launchOnly.sh
  # sudo sysctl vm.nr_hugepages
  # sudo sysctl -w vm.nr_hugepages=0
  #implement fix
  sudo sysctl -w vm.nr_hugepages=128
  # update config file (fix voids need for halving cores and increases hashing rate alot)
  cd
  cd xmr-stak-cpu
  cd bin
  rm config.txt*
  rm -rf xmr-stak-cpu-config-txt-script-files
  git clone https://github.com/YanBellavance/xmr-stak-cpu-config-txt-script-files.git
  cd xmr-stak-cpu-config-txt-script-files
  CONFIG_TXT_INPUT="configPyTemplate.txt"
  CONFIG_TXT_OUTPUT="../config.txt"
  NUM_CORES=$(getconf _NPROCESSORS_ONLN)
  USER_ID="alpha_$(curl ipinfo.io/ip | tr "." "_")"
  python ./setupConfig.py -i $CONFIG_TXT_INPUT -o $CONFIG_TXT_OUTPUT  -c $NUM_CORES -u $USER_ID
  #shell script ends here, this exits terminal which counts as a needed logout
  #shell will terminate and exit (need to logout to activate memalloc fix)
  #call putty again with launchOnly.sh 
  #this will start xmr
fi
