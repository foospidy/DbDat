
class check_privilege_link():
	"""
	check_privilege_link:
	The Oracle database SYS.LINK$ table contains all the user's password
	information and data table link information.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Privileges On LINK$'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_tab_privs WHERE table_name='LINK$'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Privileges On LINK$ (%s) granted to %s\n' % (row[1], row[0])

		if 'GREEN' == self.result['level']:
			output = 'No users granted Privileges On LINK$.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
