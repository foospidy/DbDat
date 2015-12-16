class check_configuration_test_database():
	"""
	Does a test database exist?
	"""
	# References:

	TITLE    = 'Test Databases'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT datname FROM pg_database WHERE datistemplate=false;"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			for r in rows:
				if 'test' == r[0]:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'test database exists.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'No test database found.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
