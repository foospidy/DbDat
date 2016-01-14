class check_configuration_diaglevel():
	"""
	check_configuration_diaglevel:
	The diaglevel parameter specifies the type of diagnostic errors that will be recorded in
	the db2diag.log file. It is recommended that the diaglevel parameter be set to at least 3
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Diag Level'
	CATEGORY = 'Configuration'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *results):
		for line in results[0].split('\n'):
			if '(DIAGLEVEL)' in line:
				value                 = line.split('=')[1].strip()
				self.result['output'] = line
				
				if int(value) >= 3:
					self.result['level'] = 'GREEN'
				elif int(value) > 0:
					self.result['level'] = 'YELLOW'
				else:
					self.result['level'] = 'RED'
					
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
