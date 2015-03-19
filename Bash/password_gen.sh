#!/bin/bash
LENGTH=$1
NUM=$2
CHARSET=$3

echo "Super awesome password generator!"

if [ -z "${NUM}" ]; then
	read -p "Enter length of password(s): " length
fi
	
if [ -z "${LENGTH}" ]; then
	read -p "Enter number of passwords to generate: " num
fi

if [ -z "${CHARSET}" ]; then
	printf "\n**Available character sets** 
	\t 1) All printable characters
	\t 2) Alpha numeric 
	\t 3) Hexadecimal\n"
	read -p "Select a character set: " charSetSel
fi

case "$charSetSel" in

	1) charSet="[:print:]"
	   ;;
	2) charSet="[:alnum:]"
	   ;;
	3) charSet="[:xdigit:]" 
	   ;;
	#*) echo "Whaaat?"

esac

printf  "\nPasswords:\n"
cat /dev/urandom | tr -cd $CHARSET | fold -w$LENGTH | head -$NUM
