class check_configuration_datalinks():
	"""
	check_configuration_datalinks:
	Datalinks enables the database to support the Data Links Manager to manage
	unstructured data, such as images, large files and other unstructured files on the host. It is
	recommended that data links support be disabled.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Data Links'
	CATEGORY = 'Configuration'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *results):
		self.result['level']  = 'GRAY'
		self.result['output'] = 'DATALINKS setting not found'
		
		for line in results[0].split('\n'):
			if '(DATALINKS)' in line:
				value                 = line.split('=')[1].strip()
				self.result['output'] = line
				
				if 'NO' == value:
					self.result['level'] = 'GREEN'
				else:
					self.result['level'] = 'RED'
				
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
