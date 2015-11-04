from faker import frandom, definitions
from faker import helper
import random

import datetime

def ID():
	return helper.replace_symbol_with_number('####-#####')

def gender():
	return frandom.gender()

def education():
	code = education_code()
	descr = education_descr(code)
	return code + " : " + descr

def education_code():
	return frandom.education()

def education_descr(code):
	return definitions.education()[code]

def birthdate(format='%d-%m-%Y'):
	age = random.randint(1, (85*365)) # days
	today = datetime.date.today()
	birthdate = today - datetime.timedelta(days=age)
	return birthdate.strftime(format)
