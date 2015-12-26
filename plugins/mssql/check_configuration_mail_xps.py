class check_configuration_mail_xps():
	"""
	check_configuration_mail_xps:
    This option controls the generation and transmission of email messages from
    SQL Server.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Database Mail XPs'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Database Mail XPs'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'Database Mail XPs not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'Database Mail XPs is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
