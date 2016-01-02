class check_user_password_lock_time():
	"""
	check_user_password_lock_time:
	The	PASSWORD_LOCK_TIME setting determines how many days	must pass for the
    user's account to be unlocked after the set number of failed login 
    attempts has occurred.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Password Lock Time'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='PASSWORD_LOCK_TIME' AND (limit='DEFAULT' OR limit='UNLIMITED' OR limit<1)"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''
		
		for rows in results:
			for row in rows:
				if 'UNLIMITED' == row[2]:
					self.result['level'] = 'RED'
					output += 'Password Lock Time for the ' + row[0] + ' profile is ' + row[2] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'Password Lock Time is at least 1 day.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
