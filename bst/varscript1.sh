#!/bin/bash
#!/data/data/com.termux/files/usr/bin/bash

#Demonstrate var scope 1

var1=blah
var2=foo

# Let's verify their current value

echo $0 :: var1 : $var1, var2 : $var2

export var1

./varscript2.sh

# Ler's see what they are now

echo $0 :: var1 : $var1, var2 : $var2


