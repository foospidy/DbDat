class check_configuration_adhoc_distributed_queries():
	"""
	check_configuration_adhoc_distributed_queries:
    Ad Hoc Distributed Queries Allow users to query data and execute statements
    on external data sources. This functionality should be disabled.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Ad Hoc Distributed Queries'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='ad hoc distributed queries'"
		
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			if 0 != len(row):
				if 0 == row[0][1]:
					self.result['level'] = 'GREEN'
					output = 'Ad Hoc Distributed Queries not enabled.'
				else:
					self.result['level'] = 'RED'
					output = 'Ad Hoc Distributed Queries is enabled.'
			else:
				self.result['level'] = 'GRAY'
				output = 'Ad Hoc Distributed Queries setting not found in sys.configurations table.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
