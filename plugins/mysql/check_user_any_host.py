class check_user_any_host():
	"""
	User can connect from any host.
	"""
	# References:

	TITLE    = 'Connect from Any Host'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.user WHERE host='%'"
	
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
				self.result['output'] = 'No users can connect from any host.'
			
			for r in row:
				output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
