#!/bin/bash

echo "Enter basic pay:"
read basic_pay
echo "Enter DA (Dearness Allowance):"
read da
echo "Enter HRA (House Rent Allowance):"
read hra
echo "Enter PF (Provident Fund):"
read pf

gross_pay=$(expr $basic_pay + $da + $hra)
net_pay=$(expr $gross_pay - $pf)

echo "Net Pay: $net_pay"
echo "Gross Pay: $gross_pay"