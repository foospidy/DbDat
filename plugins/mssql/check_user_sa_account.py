class check_user_sa_account():
	"""
	check_user_sa_account
	Rename and disable the SA account if your applications allow it.
	"""
	# References:
	# https://www.mssqltips.com/sqlservertip/3159/sql-server-security-checklist/

	TITLE    = 'SA Account'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT loginname FROM master..syslogins WHERE name='sa'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output = 'sa account does not exist.'
		
		for row in rows:
			self.result['level'] = 'YELLOW'
			output = 'sa account exists.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
