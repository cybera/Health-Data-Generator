#!/usr/bin/env python

from faker import name, address, demographics, phone_number, clinical, lorem, definitions
import random, string, sys, collections


header = None
record_count = 0

def generate_simple_patient():
	od = collections.OrderedDict()
	od['phn'] = demographics.ID()
	od['first_name'] = name.first_name()
	od['last_name'] = name.last_name()
	od['birthdate'] = demographics.birthdate()
	od['city'] = address.ca_city()
	od['postal_code'] = address.ca_postal_code(od['city'])
	od['education'] = demographics.education_code()
	return od


def generate_simple_medical_record():
	od = collections.OrderedDict()
	# od['phn'] = demographics.ID()
	# od['first_name'] = name.first_name()
	# od['last_name'] = name.last_name()
	# od['birthdate'] = demographics.birthdate()
	# od['city'] = address.ca_city()
	# od['postal_code'] = address.ca_postal_code(od['city'])
	# od['education'] = demographics.education_code()

	od['systolic'] = clinical.systolic()
	od['diastolic'] = clinical.diastolic(od['systolic'])
	od['ICD'] = clinical.ICD_code()
	od['glycohemoglobin'] = clinical.glycohemoglobin()
	od['patient_status'] = '"' + clinical.patient_status() + '"'
	return od


def generate_complex_patient():
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
	return od


def generate_complex_medical_record():
	od = collections.OrderedDict()
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

	if not header:
		f = open(file, 'w')
		header = ', '.join(record.keys()).upper()
		f.write(header + '\n')
		f.close()
		header = True

	f = open(file, 'a')
	row = ', '.join(map(str, record.values()))
	f.write(row +'\n')
	f.close()


def generate_patient(mode):
	if mode == 'simple':
		return generate_simple_patient()
	if mode == 'complex':
		return generate_complex_patient()
	return None

def generate_medical_record(mode):
	if mode == 'simple':
		return generate_simple_medical_record()
	if mode == 'complex':
		return generate_complex_medical_record()
	return None




if __name__ == '__main__':
	mode = 'test'
	count = 1

	if len(sys.argv) == 3:
		mode = sys.argv.pop()
		count = int(sys.argv.pop())

	if mode == 'test':
		p = generate_simple_patient()
		print_record(p)
		for i in range (0, random.randint(0,9)):
			r = generate_simple_medical_record()
			for k,v in r.iteritems():
				p[k]=v
			print "-------------"
			print_record(r)
			exit()

	i = 0
	print "generating " + str(count) + " " + mode + " records"
	while i < count:
		p = generate_patient(mode)
		j = random.randint(1,9)
		while i < count and j > 0:
			r = generate_medical_record(mode)
			# append medical record to patient record
			for k,v in r.iteritems():
				p[k]=v
			write_record(p, '../fake_data_%s.csv' % mode)
			i+=1
			j-=1
		print i
