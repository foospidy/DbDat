class check_user_password_grace_time():
	"""
	check_user_password_grace_time:
	The	password_grace_time setting	determines how many days can pass after
    the user's password expires	before the user's login capability is
    automatically locked out.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Password Grace Time'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT profile, resource_name, limit FROM sys.dba_profiles WHERE resource_name='PASSWORD_GRACE_TIME' AND (limit='DEFAULT' OR limit='UNLIMITED' OR limit>5)"
	
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
					output += 'Password Grace Time for the ' + row[0] + ' profile is ' + row[2] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'Password Grace Time is 5 or less.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
