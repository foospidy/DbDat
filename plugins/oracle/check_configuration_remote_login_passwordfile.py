class check_configuration_remote_login_passwordfile():
	"""
	check_configuration_remote_login_passwordfile:
    The	remote_login_passwordfile setting specifies whether	or not	Oracle
    checks for a password file during login and	how	many databases can use
    the password file.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Remote Login Password File'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='REMOTE_LOGIN_PASSWORDFILE'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		self.result['output'] = 'Remote Login Password File not enabled.'
		
		for rows in results:
			for row in rows:
				if 'NONE' != row[0]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Remote Login Password File is (%s) enabled.' % (row[0])
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
