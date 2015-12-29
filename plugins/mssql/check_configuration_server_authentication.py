class check_configuration_server_authentication():
	"""
	check_configuration_server_authentication:
    Use Windows Authentication to validate attempted connections.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Server Authentication Mode'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "xp_loginconfig 'login mode'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 'Windows NT Authentication' == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'Windows Authentication mode only enabled.'
			else:
				self.result['level'] = 'YELLOW'
				output = 'Non optimal authentication mode (%s) enabled.' % row[0][1]
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
