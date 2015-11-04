from faker import frandom, definitions
from faker import helper
import random, string

def ICD():
	code = ICD_code()
	descr = ICD_code_descr(code)
	return code + " : " + descr

def ICD_code():
	return frandom.ICD_code()

def ICD_code_descr(ID):
	return definitions.ICD_codes()[ID]

def blood_pressure(): # Normal resting blood pressure in an adult is approximately 120/80 mm Hg
	s = systolic()
	d = diastolic(s)
	return str(s) + '/' + str(d) + " mm Hg"

# Minimum value 40, Maximum value 300. Must be a minimum of 20 mmHg greater than diastolic number.
def systolic(): 
	s = random.randint(40, 300)
	return s

def diastolic(systolic): # Minimum value 10, Maximum value 200. Must be a minimum of 20 mmHg less than systolic number.	
	delta = random.randint(20, 50)
	return systolic - delta

def glycohemoglobin(): #Single digit number expressed as a percentage to 1 decimal point <6 6-12 abn0rm
	return "{:0.1f}".format(random.uniform(2.4, 10.7))

def patient_status():
	return frandom.patient_status()