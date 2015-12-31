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
	
	def do_check(self, *results):

		for rows in results:
			for row in rows:
				if 'Windows NT Authentication' == row[1]:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Windows Authentication mode only is (%s) enabled.' % row[1]
				else:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'Authentication mode is (%s), Windows Authentication mode only not enabled.' % row[1]

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
