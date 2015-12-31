class check_privileges_guest_user():
	"""
	check_privileges_guest_user:
    Remove the right of guest users to connect to SQL Server user databases.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Guest User CONNECT Privilege'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT DB_NAME() AS DBName, dpr.name, dpe.permission_name FROM sys.database_permissions dpe JOIN sys.database_principals dpr ON dpe.grantee_principal_id=dpr.principal_id WHERE dpr.name='guest' AND dpe.permission_name='CONNECT'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level'] = 'GREEN'
		output               = 'No CONNECT privilege granted to guest user'
		count                = 0
		
		for rows in results:
			for row in rows:
				count += 1
				
				if 1 == count:
					self.result['level'] = 'RED'
					output               = 'CONNECT privileges granted to guest user\n\n'
				
				output += row[0] + '\t' + row[1] + '\t' + row[2] + '\n'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
