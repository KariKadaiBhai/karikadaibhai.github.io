#!/bin/bash

echo "Enter the number of terms in the Fibonacci series:"
read n
a=0
b=1
count=0

echo "Fibonacci series up to $n terms:"
while [ $count -lt $n ]; do
  echo $a
  fn=$((a + b))
  a=$b
  b=$fn
  count=$((count + 1))
done

echo "Program terminated."