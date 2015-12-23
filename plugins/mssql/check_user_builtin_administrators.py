class check_user_builtin_administrators():
	"""
	check_user_builtin_administrators
	"""
	# References:
	# https://www.mssqltips.com/sqlservertip/1017/security-issues-with-the-sql-server-builtin-administrators-group/

	TITLE    = 'Builtin Administrators Group'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT * FROM master..syslogins WHERE name='BUILTIN\Administrators'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output = 'BUILTIN\Administrators does not exist.'
		
		for row in rows:
			self.result['level'] = 'RED'
			output = 'BUILTIN\Administrators exists.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
