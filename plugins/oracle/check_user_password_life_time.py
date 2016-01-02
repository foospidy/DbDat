class check_user_password_life_time():
	"""
	check_user_password_life_time:
    The	password_life_time setting determines how long a password may be used
    before the user is required to be change it.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Password Life Time'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='PASSWORD_LOCK_TIME' AND (limit='DEFAULT' OR limit='UNLIMITED' OR limit>90)"
	
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
					output += 'Password Life Time for the ' + row[0] + ' profile is ' + row[2] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'Password Life Time is 90 days or less.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
