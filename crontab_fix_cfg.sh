#!/bin/sh

sudo sysctl -w vm.nr_hugepages=128
sudo chmod 777 /home/$USER/xmr-stak-cpu/bin/xmr-stak-cpu-config-txt-script-files/launchOnly.sh

FILE="ubuntu"
DIR="/var/spool/cron/crontabs/"
# init
# look for empty dir 
if [ "$(sudo ls -A /var/spool/cron/crontabs/)" ]; then
    echo "Need to clean, crontab not Empty"
    #remove my mistakes
    crontab -l > crontab_tmp
    grep -v "xmr-stak-cpu" crontab_tmp > crontab_tmp2
    #echo new cron into cron file
    echo "@reboot /home/$USER/xmr-stak-cpu/bin/xmr-stak-cpu-config-txt-script-files/launchOnly.sh" >> crontab_tmp2
    #install new cron file
    crontab crontab_tmp2
    rm crontab_tmp
    rm crontab_tmp2
     
else
    echo "$DIR is Empty"
    (crontab -e && echo "@reboot /home/$USER/xmr-stak-cpu/bin/xmr-stak-cpu-config-txt-script-files/launchOnly.sh") | crontab 
fi


