class check_configuration_cross_db_ownership():
	"""
	check_configuration_cross_db_ownership:
    This option allows controlling cross-database ownership chaining across all
    databases at the instance (or server) level.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Cross DB Ownership Chaining'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Cross db ownership chianing'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'Cross DB Ownership Chaining not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'Cross DB Ownership Chaining is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
