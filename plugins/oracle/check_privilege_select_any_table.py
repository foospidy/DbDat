class check_privilege_select_any_table():
	"""
	check_privilege_select_any_table:
	The	Oracle database SELECT ANY TABLE privilege allows the designated user
	to open any table, except of SYS, to view it.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Select Any Table'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='SELECT ANY TABLE' AND grantee NOT IN ('DBA', 'MDSYS', 'SYS', 'IMP_FULL_DATABASE', 'EXP_FULL_DATABASE', 'DATAPUMP_IMP_FULL_DATABASE', 'WMSYS', 'SYSTEM')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Select Any Table granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Select Any Table.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
