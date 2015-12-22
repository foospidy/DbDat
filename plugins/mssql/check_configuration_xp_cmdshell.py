class check_configuration_xp_cmdshell():
	"""
	Determine current database version
	"""
	# References:
	# http://sqltidbits.com/scripts/check-if-xpcmdshell-enabled-across-multiple-servers

	TITLE    = 'Xp Cmdshell Enabled'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name AS [Configuration], CONVERT(INT, ISNULL(value, value_in_use)) AS [IsEnabled] FROM  master.sys.configurations WHERE  name = 'xp_cmdshell'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output         = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'xp_cmdshell not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'xp_cmdshell is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
