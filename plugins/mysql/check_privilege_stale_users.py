class check_privilege_stale_users():
	"""
	Users in mysql.db but not in mysql.user
	"""
	# References:

	TITLE    = 'Stale User Privilege'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.db WHERE user NOT IN (SELECT user FROM mysql.user)"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			if len(row) > 0:
				self.result['level'] = 'RED'
				
				for r in row:
					output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
					self.result['output'] = output
				
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No stale privileges found.'
			
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
