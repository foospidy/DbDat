class check_configuration_health_mon():
	"""
	check_configuration_health_mon:
	The health_mon parameter allows you to specify whether you want to monitor the
	instance, thedatabases, and the corresponding database objects. It is recommended that
	health_mon parameter be set to on.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Health Monitoring'
	CATEGORY = 'Configuration'
	TYPE     = 'clp'
	SQL    	 = ''
	CMD      = ['db2', '-tn', 'get', 'database', 'manager', 'configuration']

	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *results):
		for line in results[0].split('\n'):
			if '(HEALTH_MON)' in line:
				value                 = line.split('=')[1].strip()
				self.result['output'] = line
				
				if 'ON' == value:
					self.result['level'] = 'GREEN'
				else:
					self.result['level'] = 'RED'
					
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
