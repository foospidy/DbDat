class check_configuration_xp_cmdshell():
	"""
	check_configuration_xp_cmdshell:
    The xp_cmdshell procedure allows an authenticated SQL Server user to execute
    operating- system command shell commands and return results as rows within
    the SQL client.
	"""
	# References:
	# http://sqltidbits.com/scripts/check-if-xpcmdshell-enabled-across-multiple-servers
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Xp Cmdshell Enabled'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) AS value_configured, CAST(value_in_use as int) AS value_in_use FROM  master.sys.configurations WHERE  name='xp_cmdshell'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
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
