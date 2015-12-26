class check_configuration_ole_automation_procedures():
	"""
	check_configuration_ole_automation_procedures:
    Extended stored procedures that allow SQL Server users to execute functions
    external to SQL Server.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Ole Automation Procedures'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Ole Automation Porcedures'"
		
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'Ole Automation Porcedures not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'Ole Automation Porcedures is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
