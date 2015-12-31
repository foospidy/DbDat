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
	
	def do_check(self, *results):
		self.result['level']  = 'GRAY'
		self.result['output'] = 'Ole Automation Porcedures setting not found in sys.configurations table.'
		
		for rows in results:
			for row in rows:
				if 0 != len(row):
					if 0 == row[1]:
						self.result['level']  = 'GREEN'
						self.result['output'] = 'Ole Automation Porcedures is (%s) not enabled.' % (row[1])
					else:
						self.result['level']  = 'RED'
						self.result['output'] = 'Ole Automation Porcedures is (%s) enabled.' % (row[1])

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
