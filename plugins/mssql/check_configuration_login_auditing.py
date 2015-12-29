class check_configuration_login_auditing():
	"""
	check_configuration_login_auditing:
    Log both successful and failed login SQL Server authentication attempts.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Login Auditing'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "xp_loginconfig 'audit level'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output = ''
		
		for row in rows:
			for r in row:
				if 'none' == r[1]:
					self.result['level'] = 'RED'
					output = 'No login audit loging enabled.'
				elif 'all' != r[1]:
					self.result['level'] = 'YELLOW'
					output = 'Logging of %s logins only enabled.' % (r[1])
				else:
					self.result['level'] = 'GREEN'
					output = 'Logging of successful and failed logins enabled.'
        
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
