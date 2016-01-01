class check_user_empty_password():
	"""
    check_user_empty_password:
	Accounts with empty passwords.
	"""
	# References:

	TITLE    = 'Empty Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.user WHERE LENGTH(password)=0 OR password IS null"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output  = ''
		
		for rows in results:
			if len(rows) > 0:
				self.result['level'] = 'RED'
				for row in rows:
					output += 'user: ' + str(row[0]) + ' host: ' + str(row[1]) + '\n'
			else:
				self.result['level']  = 'GREEN'
				output                = 'No anonymous users found.'
			
			self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
