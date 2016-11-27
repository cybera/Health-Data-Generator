import definitions
import random

def list_element(input_list):
  return random.choice(input_list)

def city_prefix():
  return list_element(definitions.city_prefix())

def city_suffix():
  return list_element(definitions.city_suffix())

def street_suffix():
  return list_element(definitions.street_suffix())

def br_state():
  return list_element(definitions.br_state())

def br_state_abbr():
  return list_element(definitions.br_state_abbr())

def us_state():
  return list_element(definitions.us_state())

def us_state_abbr():
  return list_element(definitions.us_state_abbr())

def uk_county():
  return list_element(definitions.uk_county())

def uk_country():
  return list_element(definitions.uk_country())

def first_name():
  return list_element(definitions.first_name())

def last_name():
  return list_element(definitions.last_name())

def name_prefix():
  return list_element(definitions.name_prefix())

def name_suffix():
  return list_element(definitions.name_suffix())

def catch_phrase_adjective():
  return list_element(definitions.catch_phrase_adjective())

def catch_phrase_descriptor():
  return list_element(definitions.catch_phrase_descriptor())

def catch_phrase_noun():
  return list_element(definitions.catch_phrase_noun())

def bs_adjective():
  return list_element(definitions.bs_adjective())

def bs_buzz():
  return list_element(definitions.bs_buzz())

def bs_noun():
  return list_element(definitions.bs_noun())

def phone_formats():
  return list_element(definitions.phone_formats())

def domain_suffix():
  return list_element(definitions.domain_suffix())

def ca_city():
  return list_element(definitions.ca_city())

def ca_province_abbr(province):
  return definitions.ca_province_abbr(province)

def ca_postal_code(city):
  return list_element(definitions.ca_postal_codes(city))

def gender():
  return list_element(definitions.gender())

def ICD_code():
  return list_element(definitions.ICD_codes().keys())

def education():
  return list_element(definitions.education().keys())

def patient_status():
  return list_element(definitions.patient_status())
