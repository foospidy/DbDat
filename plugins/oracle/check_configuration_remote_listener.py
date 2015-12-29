class check_configuration_remote_listener():
	"""
	check_configuration_remote_listener:
    The	remote_listener setting determines whether or not a	valid listener can be
    established on a system separate from the database instance.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'REMOTE_LISTENER'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='REMOTE_LISTENER'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output               = 'REMOTE_LISTENER not set.'
		
		for row in rows:
			for r in row:
				if None != r[0]:
					self.result['level'] = 'RED'
					output               = 'REMOTE_LISTENER set to: %s' % (row[0][0])

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
