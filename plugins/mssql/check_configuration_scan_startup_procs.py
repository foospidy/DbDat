class check_configuration_scan_startup_procs():
	"""
	check_configuration_scan_startup_procs:
    This option causes SQL Server to scan for and automatically run all stored
    procedures that are set to execute upon service startup.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Scan For Startup Procs'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Scan for startup procs'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
				
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'Remote admin connections not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'Remote admin connections is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
