#!/data/data/com.termux/files/usr/bin/bash

#Demonstrate var scope 2 


# Let's verify their current value

echo $0 :: var1 : $var1, var2 : $var2


var1=flop
var2=bleh

echo $var1 : $var2

exit
