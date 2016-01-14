class check_information_version():
	"""
	check_information_version:
	Periodically, IBM releases "Fixpaks" to enhance features and resolve defects, including
	security defects. It is recommended that the DB2 instance remain current with all fix packs. 
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'DB2 Level'
	CATEGORY = 'Information'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2level']
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		self.result['output'] = results[0]
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
