#!/bin/sh
# putty.exe -ssh username@123.234.124.213 -m C:\path\to\your\shell-script\launchOnly.sh -i C:\path\to\your\ssh-key.ppk

DIRECTORY="xmr-stak-cpu"

cd # start from home

# if dir doesnt exist we need to install
if [ ! -d $DIRECTORY ]; then 
  # dependencies  
  sudo add-apt-repository ppa:ubuntu-toolchain-r/test
  sudo apt update
  sudo apt --yes install gcc-5 g++-5 make
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 1 --slave /usr/bin/g++ g++ /usr/bin/g++-5
  curl -L http://www.cmake.org/files/v3.4/cmake-3.4.1.tar.gz | tar -xvzf - -C /tmp/
  cd /tmp/cmake-3.4.1/ && ./configure && make && sudo make install && cd -
  sudo update-alternatives --install /usr/bin/cmake cmake /usr/local/bin/cmake 1 --force
  sudo apt --yes install libmicrohttpd-dev libssl-dev libhwloc-dev
  # clone and build
  git clone https://github.com/fireice-uk/xmr-stak-cpu.git
  cd xmr-stak-cpu
  cmake .
  make install
  sudo apt-get --yes install python
  # setup config file
  cd bin
  mv config.txt config.txt.og
  git clone https://github.com/YanBellavance/xmr-stak-cpu-config-txt-script-files.git
  cd xmr-stak-cpu-config-txt-script-files
  CONFIG_TXT_INPUT="configPyTemplate.txt"
  CONFIG_TXT_OUTPUT="../config.txt"
  NUM_CORES=$(getconf _NPROCESSORS_ONLN)
  USER_ID="alpha_$(curl ipinfo.io/ip | tr "." "_")"
  # USER_ID="yanBellav_1"
  python ./setupConfig.py -i $CONFIG_TXT_INPUT -o $CONFIG_TXT_OUTPUT  -c $NUM_CORES -u $USER_ID
  cd ..
  # launch 
  screen -q -d -m ./xmr-stak-cpu
  echo done. press any key to continue
  read -n 1 -s -r -p "Press any key to continue"      
  # now go do a manual check of hash rate (many cores sometimes dont launch right and give like 0H/s)
else
  echo xmr-stak-cpu has already been installed on this computer
  read -n 1 -s -r -p "Press any key to continue"  
fi
