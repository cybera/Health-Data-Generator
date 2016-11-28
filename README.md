Health Data Generator
=======

### Generate realistic medical records
This tool will create files of convincingly realistic comma-separated medical records suitable for testing and system development.

Installation
=============
clone the git repository and install from source

    $ git clone https://github.com/cybera/health-data-generator.git
    $ cd health-data-generator
    $ sudo python setup.py install
    or
    $ sudo pip install .


Usage
======
To generate any number of health records, use the 'generate' command.  Either a 'simple' or a 'complex' record format can be created.
```
generate <integer> <simple|complex>
where:
	'n' is the number of records to generate, and
	'simple' or 'complex' are the type of record to generate
```

To use this package in your own project, simply import the required packages:
```python
from health_data_generator.faker import name
random_name = name.find_name() # 'Anne Howe'
```
## Features
This is a list of the major features.  See source for additional functionality
* lorem - pseudo-latin words, sentences, and paragraphs
* phone - randomly generated phone numbers in various formats
* internet - randomly generated email addresses and domain names
* name - male and female names
* frandom - utility to randomly generate fragments of names, addresses, medical codes
* cards - business cards
* company - company names and slogans
* demographics - personal attributes, such as gender, birthdate, education level



License and Authors
==================
Author:: Barton Satchwill (<barton.satchwill@cybera.ca>)
Copyright:: 2016, Cybera, Inc.

We gratefully acknowledge the prior work of Hrishikesh Huilgolkar, Matthew Bergman & Marak Squires

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

