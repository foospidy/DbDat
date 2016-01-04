
class check_privilege_sys_user_mig():
	"""
	check_privilege_sys_user_mig:
	The table sys.user$mig is created during migration and contains the Oracle
	password hashes before the migration starts.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'SYS.USER$MIG Table'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT owner, table_name FROM all_tables WHERE owner='SYS' AND table_name='USER$MIG'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'RED'
				output += 'USER$MIG found with owner: (%s)\n' % (row[0])

		if 'GREEN' == self.result['level']:
			output = 'USER$MIG table was not found.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
