import frandom, helper, definitions
import random

def phone_number(format=None):
  if not format:
    format = frandom.phone_formats()

  return helper.replace_symbol_with_number(format)

def phone_number_format(phone_formats_array_index):
  return helper.replace_symbol_with_number(definitions.phone_formats()[phone_formats_array_index])
