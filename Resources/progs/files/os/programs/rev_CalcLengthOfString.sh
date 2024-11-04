#!/bin/bash

echo "Enter the string:"
read str

len=`echo $str | wc -c`
len=`expr $len - 1`

echo "The length of the string is $len"

rev=""

while [ $len -gt 0 ]
do
  temp=`echo $str | cut -c $len`
  rev=`echo $rev$temp`
  len=`expr $len - 1`
done

echo "The reversed string is $rev"