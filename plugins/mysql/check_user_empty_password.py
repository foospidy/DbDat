class check_user_empty_password():
	"""
	Accounts with empty passwords.
	"""
	# References:

	TITLE    = 'Empty Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.user WHERE password=''"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output  = ''
		
		for row in rows:
			if len(row) > 0:
				self.result['level'] = 'RED'
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No anonymous users found.'
			
			for r in row:
				output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
