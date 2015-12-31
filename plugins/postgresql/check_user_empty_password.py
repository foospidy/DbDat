class check_user_empty_password():
	"""
	Accounts with empty passwords.
	"""
	# References:
	# https://stackoverflow.com/questions/23641823/check-if-a-role-in-postgresql-has-a-password-set

	TITLE    = 'Empty Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL      = "SELECT * FROM pg_shadow WHERE passwd IS NULL"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output  = ''
		
		for rows in results:
			if len(rows) > 0:
				self.result['level'] = 'RED'
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No empty passwords found.'
			
			for row in rows:
				output += 'user name: ' + str(row[0]) + '\n'
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
