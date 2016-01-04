class check_privilege_execute_catalog_role():
	"""
	check_privilege_execute_catalog_role:
	The Oracle database EXECUTE_CATALOG_ROLE provides EXECUTE privileges for a
	number of packages and procedures in the data dictionary in the SYS schema.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Execute Catalog Role'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, granted_role FROM dba_role_privs WHERE granted_role='EXECUTE CATALOG ROLE' AND grantee NOT IN ('DBA','SYS','IMP_FULL_DATABASE','EXP_FULL_DATABASE')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Execute Catalog Role granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Execute Catalog Role.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
