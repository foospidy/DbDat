class check_privilege_select_any_dictionary():
	"""
	check_privilege_select_any_dictionary:
	The	Oracle database SELECT ANY DICTIONARY privilege	allows the designated
	user to access SYS schema objects.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Select Any Dictionary'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='SELECT ANY DICTIONARY' AND grantee NOT IN ('DBA','DBSNMP','OEM_MONITOR', 'OLAPSYS','ORACLE_OCM','SYSMAN','WMSYS')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Select Any Dictionary granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Select Any Dictionary.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
