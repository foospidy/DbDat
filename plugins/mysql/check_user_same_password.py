class check_user_same_password():
	"""
	Accounts using the same password.
	"""
	# References:

	TITLE    = 'Same Password'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT CONCAT(user,'@', host) AS account, pass FROM (SELECT user1.user, user1.host, user2.user AS u2, user2.host AS h2, left(user1.password,5) as pass FROM mysql.user AS user1 INNER JOIN mysql.user AS user2 ON (user1.password = user2.password) WHERE user1.user != user2.user AND user1.password != '') users GROUP BY CONCAT(user,'@',host) ORDER BY pass"
	
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
				self.result['output'] = 'No users with the same password found.'
			
			for r in row:
				output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
