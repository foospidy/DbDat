class check_user_builtin_administrators():
	"""
	check_user_builtin_administrators:
    By default the BUTLTIN/Administrators group may unecessarily have SQL Server
    system administrator rights. Best practice is to follow the principle of
    least privileges.
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
	
	def do_check(self, *results):
		self.result['level'] = 'GREEN'
		output               = 'BUILTIN\Administrators does not exist.'
		
		for rows in results:
			for row in rows:
				self.result['level'] = 'RED'
				output = 'BUILTIN\Administrators does exist.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
