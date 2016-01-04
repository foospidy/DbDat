
class check_privilege_user():
	"""
	check_privilege_user:
	The Oracle database SYS.USER$ table contains the users' hashed password information.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Privileges On USER$'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_tab_privs WHERE table_name='USER$' AND GRANTEE NOT IN ('CTXSYS','XDB','APEX_030200','APEX_040000','APEX_040100','APEX_040200')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Privileges On USER$ (%s) granted to %s\n' % (row[1], row[0])

		if 'GREEN' == self.result['level']:
			output = 'No users granted Privileges On USER$.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
