#!/bin/bash
LENGTH=$1
NUM=$2
CHARSET=$3

echo "Super awesome password generator!"

if [ -z "${LENGTH}" ]; then
	read -p "Enter length of password(s): " LENGTH
fi
	
if [ -z "${NUM}" ]; then
	read -p "Enter number of passwords to generate: " NUM
fi

if [ -z "${CHARSET}" ]; then
	printf "\n**Available character sets** 
	\t 1) All printable characters
	\t 2) Alpha numeric 
	\t 3) Hexadecimal\n"
	read -p "Select a character set: " CHARSETSEL
fi

case "$CHARSETSEL" in

	1) CHARSET="[:print:]"
	   ;;
	2) CHARSET="[:alnum:]"
	   ;;
	3) CHARSET="[:xdigit:]" 
	   ;;
	#*) echo "Whaaat?"

esac

printf  "\nPasswords:\n"
cat /dev/urandom | tr -cd $CHARSET | fold -w$LENGTH | head -$NUM
