class check_privilege_become_user():
	"""
	check_privilege_become_user:
	The	Oracle database BECOME USER privilege allows the designated user to
	inherit the	rights of another user.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Become User'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='BECOME USER' AND grantee NOT IN ('DBA','SYS','IMP_FULL_DATABASE')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Become User granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Become User.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
