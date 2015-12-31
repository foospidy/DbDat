class check_configuration_remote_admin_connections():
	"""
	check_configuration_remote_admin_connections:
    This setting controls whether a client application on a remote computer can
    use the Dedicated Administrator Connection (DAC).
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Remote Admin Connections'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM sys.configurations WHERE name='Remote admin connections' AND SERVERPROPERTY('IsClustered')=0"
		
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		self.result['output'] = 'Remote admin connections not enabled.'

		for rows in results:
			for row in rows:
				if 0 == row[1]:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Remote admin connections is (%s) not enabled.' % (row[1])
				else:
					self.result['level']  = 'RED'
					self.result['output'] = 'Remote admin connections is (%s) enabled.' % (row[1])

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
