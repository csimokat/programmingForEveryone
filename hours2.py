#!/usr/bin/env python

# Program is an extension of hours.py that pays time and a half for work over 40 hours

hrs = raw_input("Enter Hours:")
h = float(hrs)
r = raw_input("Enter Rate:")
rate = float(r)

if h <= 40 :
	pay = rate * h
else :
	pay = (rate * 40) + ((h - 40) * rate * 1.5)

print pay