import helper

class check_user_users_with_defpwd():
	"""
	check_user_users_with_defpwd
	Users with default passwords
	"""
	# References:
	# http://docs.oracle.com/cd/B28359_01/server.111/b28320/statviews_5074.htm

	TITLE    = 'Users With Default Passowrds'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = 'SELECT username FROM dba_users_with_defpwd'
	
	verbose = False
	skip	= False
	result  = {}
	
	dbversion = None
	
	def do_check(self, *rows):
		output               = ''
		self.result['level'] = 'GREEN'
		
		for row in rows:
			for r in row:
				self.result['level'] = 'RED'
				output += r[0] + '\n'

		self.result['output'] = output
			
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)

		self.dbversion = helper.get_version(parent.dbcurs)
