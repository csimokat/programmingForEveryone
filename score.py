#!/usr/bin/env python

score = raw_input("Enter Score:")

try: 
	score = float(score)
except:
	print "Input is not a number."
	quit()

if score > 1 :
	print "Inputted score is out of range."
	quit()

if score < 0 :
	print "Inputted score is out of range."
	quit()

if score >= .9 :
	print "A"
elif score >= .8 :
	print "B"
elif score >= .7 :
	print "C"
elif score >= .6 :
	print "D"
else :
	print "F"