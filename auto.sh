#!bin/bash
wireshark -i 3 -k -a duration:80 -w sa
tshark -V -r sa > output.txt
cat output.txt | grep 'BD_ADDR' | grep '(' | awk '{print $2}' | sed 's/(//' | sed 's/)//' | sed 's/://g' > database.txt

python3 code.py
