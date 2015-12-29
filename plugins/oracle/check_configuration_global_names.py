class check_configuration_global_names():
	"""
	check_configuration_global_names:
    The	global_names setting requires that the name	of a database link matches
    that of the remote database it will connect	to.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'GLOBAL_NAMES'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='GLOBAL_NAMES'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'TRUE' == row[0][0]:
				self.result['level'] = 'GREEN'
				output += 'GLOBAL_NAMES is set to true.'
			else:
				self.result['level'] = 'RED'
				output += 'GLOBAL_NAMES is set to %s.' % (row[0][0])

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
