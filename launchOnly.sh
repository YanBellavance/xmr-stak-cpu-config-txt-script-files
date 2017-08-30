#!/bin/sh

#kill xmr-stak-cpu in case
sudo ps -ef | grep -v grep | grep xmr-stak-cpu | awk '{print "kill " $2}'| sh -x
sudo sysctl -w vm.nr_hugepages=128
cd # start from home
cd xmr-stak-cpu
cd bin
screen -q -d -m ./xmr-stak-cpu
echo done. press any key to continue
# n option doe not work when shell called from term
# read -n 1 -s -r -p "Press any key to continue"  
