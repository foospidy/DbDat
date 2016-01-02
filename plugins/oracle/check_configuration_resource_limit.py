class check_configuration_resource_limit():
	"""
	check_configuration_resource_limit:
	RESOURCE_LIMIT determines whether resource limits are enforced in database
    profiles.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Resource Limit'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='RESOURCE_LIMIT'"

	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		
		for rows in results:
			for row in rows:
				if 'TRUE' == row[0]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Resource limit is (%s) enabled.' % (row[0])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Resource limit is (%s) not enabled.' % (row[0])

		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
