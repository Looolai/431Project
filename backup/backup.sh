#!/bin/bash
#########################################
# Options:
# Documentname: backup.sh
# Description: Automated Backup
# Author: Loai Afify
# Created on: 11.05.2022
#########################################
# Changes:
# Created Document
# Changed Header
#########################################
# Important Information:
# Add "PermitUserEnvironment yes" to your server sshd_config
# Add a Cronjob with the Value "30 16 * * * root {Path to this Script} > /dev/null &2>1"
# Add a Log Rotate if you want to
# Change SSHPass option to -i or create Passwd.txt with your Password
#########################################
# Start of Script below
#########################################
timestamp=$(date +%Y%m%d%H%M%S)
function action_check() {
    command=$@
    $@
    check_code=$?
    if [ $check_code -eq 0 ]
        then
            echo "$timestamp OK - Command: $command war Erfolgreich" >> /var/log/backup.log
        else
            echo "$timestamp ERROR - Command: $command ist Fehlgeschlagen" >> /var/log/backup.log
    fi
}
function backup_exec() {
dir="/home"
varscp="sshpass -f passwd.txt scp -rC $dir loai@192.168.32.134:/home/backups/backup$timestamp"
action_check $varscp
currentbackupfolder=backup$timestamp
archivefile=backup$timestamp.tar.gz
action_check sshpass -f passwd.txt ssh loai@192.168.32.134 "cd /home/backups; tar -czf $archivefile $currentbackupfolder; rm -rf $currentbackupfolder"
}
function availability() {
    ping_check=$(ping -c 1 192.168.32.134 ; echo $?)
    if [ ${ping_check: -1} -eq 0 ]
        then
            echo "$timestamp OK - Command: ping war Erfolgreich" >> /var/log/backup.log
        else
            echo "$timestamp ERROR - Command: ping ist Fehlgeschlagen" >> /var/log/backup.log
            exit 1
    fi
}
function log_check() {
    if [ -e /var/log/backup.log ]
        then
            echo "Backup.log exists"
        else
            sudo touch /var/log/backup.log
    fi
}
log_check
availability
backup_exec
#########################################
# End of Script