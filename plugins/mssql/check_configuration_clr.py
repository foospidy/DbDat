class check_configuration_clr():
	"""
	check_configuration_clr:
    The CLR enabled option specifies whether user assemblies can be run by SQL
    Server.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'CLR Enabled'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='clr enabled'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'CLR not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'CLR is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
