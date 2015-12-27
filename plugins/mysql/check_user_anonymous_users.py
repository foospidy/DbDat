class check_user_anonymous_users():
	"""
    check_user_anonymous_users:
	Do anonymous users exist.
	"""
	# References:

	TITLE    = 'Anonymous Users'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL      = "SELECT * FROM mysql.user WHERE user=''"
	
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
				output = output + r[0] + "\n"
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
