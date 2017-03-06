#!/usr/bin/env python

# Program is an extension of hours2.py adds error handling
try:
	hrs = raw_input("Enter Hours:")
	h = float(hrs)
	r = raw_input("Enter Rate:")
	rate = float(r)

except: 
	print "Error, please enter numeric input"
	quit()

if h <= 40 :
	pay = rate * h
else :
	pay = (rate * 40) + ((h - 40) * rate * 1.5)

print pay