class check_configuration_keepfenced():
	"""
	check_configuration_keepfenced:
	The keepfenced parameter indicates whether or not external user-defined functions or
	stored procedures will reuse a DB2 process after each subsequent call. It is recommended
	that this parameter be set to NO. 
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Health Monitoring'
	CATEGORY = 'Configuration'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *results):
		for line in results[0].split('\n'):
			if '(KEEPFENCED)' in line:
				value                 = line.split('=')[1].strip()
				self.result['output'] = line
				
				if 'NO' == value:
					self.result['level'] = 'GREEN'
				else:
					self.result['level'] = 'RED'
					
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
