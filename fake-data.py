#!/usr/bin/env python

from faker import name, address, demographics, phone_number, clinical, lorem, definitions
import random, string, sys, collections


header = None
record_count = 0

def generate_simple_record():
	od = collections.OrderedDict()
	od['phn'] = demographics.ID()
	od['first_name'] = name.first_name()
	od['last_name'] = name.last_name()
	od['birthdate'] = demographics.birthdate()
	od['city'] = address.ca_city()
	od['postal_code'] = address.ca_postal_code(od['city'])
	od['education'] = demographics.education_code()
	od['systolic'] = clinical.systolic()
	od['diastolic'] = clinical.diastolic(od['systolic'])
	od['ICD'] = clinical.ICD_code()
	od['glycohemoglobin'] = clinical.glycohemoglobin()
	od['patient_status'] = '"' + clinical.patient_status() + '"'
	return od


def generate_tricky_record():
	od = collections.OrderedDict()
	od['phn'] = demographics.ID()
	od['name'] = name.find_name()
	od['birthdate'] = '"' + demographics.birthdate(random.choice(['%Y-%m-%d', '%b %d, %Y', '%d %B %Y'])) + '"'
	od['postal_code'] = address.ca_postal_code(address.ca_city())
	od['province'] = 'Alberta' 
	od['province_abbr'] = address.ca_province_abbr(od['province'])
	od['gender'] = demographics.gender()
	od['phone'] = phone_number.phone_number()
	od['education'] = '"' + demographics.education() + '"'
	od['blood_pressure'] = clinical.blood_pressure()
	od['ICD'] = '"' + clinical.ICD() + '"'
	od['glycohemoglobin'] = clinical.glycohemoglobin()
	od['patient_status'] = '"' + clinical.patient_status() + '"'
	return od


def print_record(record):
	for key in record.keys():
		print key.upper().rjust(15) + " : " + str(record[key])


def write_record(record, file):
	global header
	values = ''

	if not header:
		header = True
		f = open(file, 'w')
		header = ', '.join(record.keys()).upper()
		f.write(header + '\n')
		f.close()

	for key, value in record.iteritems():
		values += str(value) + ', '
	values = values[:-2]
	f = open(file, 'a')
	f.write(values + '\n')
	f.close()


if __name__ == '__main__':
	mode = 'test'
	count = 1

	if len(sys.argv) == 3:
		mode = sys.argv.pop()
		count = int(sys.argv.pop())

	if mode == 'test':
		r = generate_tricky_record()
		print_record(r)

	if mode == 'simple':
		print "generating " + str(count) + " " + mode + " records"
		for i in range(0,count):
			r = generate_simple_record()
			write_record(r, '../fake_data_simple.csv')
			print i+1

	if mode == 'tricky':
		print "generating " + str(count) + " " + mode + " records"
		for i in range(0, count):
			r = generate_tricky_record()
			write_record(r, '../fake_data_complex.csv')
			print i+1


	