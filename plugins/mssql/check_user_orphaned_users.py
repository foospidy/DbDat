class check_user_orphaned_users():
	"""
	check_user_orphaned_users:
    A database user for which the corresponding SQL Server login is undefined
    or is incorrectly defined on a server instance cannot log in to the instance
    and is referred to as orphaned and should be removed..
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'Orphaned Users'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "EXEC sp_change_users_login @Action='Report'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output               = 'No orphaned users found.'
		count                = 0
		
		for row in rows:
			for r in row:
				count += 1
				
				if 1 == count:
					self.result['level'] = 'RED'
					output = 'Orphaned users found:\n\n'
			
				output += r[0] + '\t' + r[1] + '\n'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
