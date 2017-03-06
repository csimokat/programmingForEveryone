#!/usr/bin/env python

# Program is an extension of hours3.py 
#embedding logic in a user defined function computepay()

try:
	hrs = raw_input("Enter Hours:")
	h = float(hrs)
	rate = raw_input("Enter Rate:")
	r = float(rate)

except: 
	print "Error, please enter numeric input"
	quit()

def computepay(h,r):
	if h <= 40 :
		p = r * h
	else :
		p = (r * 40) + ((h - 40) * r * 1.5)
	return p

pay = computepay(h,r)

print pay