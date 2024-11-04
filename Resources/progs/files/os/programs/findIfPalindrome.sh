#!/bin/bash

echo "Enter the string:"
read str

len=$(echo -n "$str" | wc -c)
rev=""

while [ $len -gt 0 ]; do
  temp=$(echo "$str" | cut -c $len)
  rev="$rev$temp"
  len=$((len - 1))
done

echo "The reversed string is $rev"

if [ "$rev" = "$str" ]; then
  echo "$str is a palindrome"
else
  echo "$str is not a palindrome"
fi