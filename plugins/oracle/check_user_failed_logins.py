class check_user_failed_logins():
	"""
	check_user_failed_logins
	Check the number of allowed failed login attempts.
	"""
	# References:

	TITLE    = 'Failed Login Attempts'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='FAILED_LOGIN_ATTEMPTS' AND profile IN (SELECT profile FROM sys.dba_users) ORDER BY profile"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		ver_database = None
		ver_plsql    = None
		ver_core     = None
		ver_tns      = None
		ver_nlsrtl   = None
		
		for row in rows:
			for r in row:
				if 'UNLIMITED' == r[2]:
					self.result['level'] = 'RED'
					output += 'Number of allowed failed attempts for the ' + r[0] + ' profile is ' + r[2] + '\n'
				elif r[2] > 10:
					self.result['level'] = 'RED'
					output += 'Number of allowed failed attempts for the ' + r[0] + ' profile is ' + r[2] + '\n'
				elif r[2] > 3:
					self.result['level'] = 'YELLOW'
					output += 'Number of allowed failed attempts for the ' + r[0] + ' profile is ' + r[2] + '\n'
				else:
					self.result['level'] = 'GREEN'
					output += 'Number of allowed failed attempts for the ' + r[0] + ' profile is ' + r[2] + '\n'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
