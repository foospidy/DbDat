class check_configuration_sec_max_failed_login_attempts():
	"""
	check_configuration_sec_max_failed_login_attempts:
	The SEC_MAX_FAILED_LOGIN_ATTEMPTS parameter determines how many failed login
	attempts are allowed before Oracle closes the login connecction.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Max Failed Login Attempts'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='SEC_MAX_FAILED_LOGIN_ATTEMPTS'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		
		for rows in results:
			for row in rows:
				if int(row[0]) > 10:
					self.result['level']  = 'RED'
					self.result['output'] = 'SEC_MAX_FAILED_LOGIN_ATTEMPTS is %s (greater than 10).' % (row[0])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'SEC_MAX_FAILED_LOGIN_ATTEMPTS is %s (10 or less).' % (row[0])
		
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
