Faker - Generate any amount of fake data for python
========

Usage
======
```python
from faker import name
random_name = name.find_name() #" 'Darrin Schmitt'
```
Installation

      $ sudo pip install faker.py

Or clone the git repo and install from source

      $ git clone https://github.com/hrishikeshio/Faker.py.git
      $ cd Faker.py
      $ sudo python setup.py install

## API
* lorem
  * words
  * sentence
  * sentences
  * paragraph
  * paragraphs
* phone
  * phone_number
  * phone_number_format
* internet
  * email
  * user_name
  * domain_name
  * domain_word
  * ip
* name
  * first_name
  * last_name
  * find_name
* frandom
  * list_element
  * ca_city
  * ca_province_abbr
  * ca_postal_code
  * gender
  * ICD_code
  * education
  * patient_status
  * city_prefix
  * city_suffix
  * street_suffix
  * br_state
  * br_state_abbr
  * us_state
  * us_state_abbr
  * uk_county
  * uk_country
  * first_name
  * last_name
  * name_prefix
  * name_suffix
  * catch_phrase_adjective
  * catch_phrase_descriptor
  * catch_phrase_noun
  * bs_adjective
  * bs_buzz
  * bs_noun
  * phone_formats
  * domain_suffix
  * address
  * zip_code
  * zip_code_format
  * city
  * ca_city
  * ca_postal_code
  * ca_province_abbr
  * street_name
  * street_address
  * secondary_address
  * br_state
  * uk_county
  * uk_country
  * us_state
* cards
  * create_card
  * user_card
* company
  * suffixes
  * company_name
  * company_suffix
  * catch_phrase
  * bs
* helper
  * slugify
  * replace_symbol_with_number
  * shuffle
  * clinical
  * ICD
  * ICD_code
  * ICD_code_descr
  * blood_pressure
  * systolic
  * diastolic
  * glycohemoglobin
  * patient_status
* definitions
  * ca_province
  * ca_province_abbr
  * ca_city
  * ca_postal_codes
  * gender
  * ICD_codes
  * education
  * patient_status
  * first_name
  * last_name
  * name_prefix
  * name_suffix
  * br_state
  * br_state_abbr
  * us_state
  * us_state_abbr
  * city_prefix
  * city_suffix
  * street_suffix
  * uk_county
  * uk_country
  * catch_phrase_adjective
  * catch_phrase_descriptor
  * catch_phrase_noun
  * bs_adjective
  * bs_buzz
  * bs_noun
  * domain_suffix
  * lorem
  * phone_formats
* demographics
  * ID
  * gender
  * education
  * education_code
  * education_descr
  * birthdate

## Authors
#### Hrishikesh Huilgolkar
Follow on twitter http://twitter.com/hrishikeshio <br/>
My Blog http://blogicious.com <br/>
Ported from javascript library Faker.js by Matthew Bergman & Marak Squires http://github.com/marak/Faker.js/
Copyright (c) 2013 Hrishikesh Huilgolkar http://github.com/hrishikeshio/Faker.py/
#### Barton Satchwill
Added extenstions for Canadian locales and medical data


Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:


The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
