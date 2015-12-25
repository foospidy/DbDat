class check_configuration_remote_admin_connections():
	"""
	check_configuration_remote_admin_connections
	"""
	# References:
	# http://sqltidbits.com/scripts/check-if-xpcmdshell-enabled-across-multiple-servers

	TITLE    = 'Remote Admin Connections'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Remote admin connections' AND SERVERPROPERTY('IsClustered')=0"
	
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		self.result['level'] = 'GREEN'
		output = 'Remote admin connections not enabled.'
				
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
