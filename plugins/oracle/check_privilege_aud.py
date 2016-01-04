
class check_privilege_aud():
	"""
	check_privilege_aud:
	The  Oracle database SYS.AUD$ table contains all the audit records for the 
	database of the non-Data Manipulation Language  (DML) events, such as ALTER,
	DROP, CREATE, and so forth.  (DML changes need trigger-based audit events
	to record data alterations.)
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Privileges On AUD$'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_tab_privs WHERE table_name='AUD$' AND grantee NOT IN ('DELETE_CATALOG_ROLE')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Privileges On AUD$ (%s) granted to %s\n' % (row[1], row[0])

		if 'GREEN' == self.result['level']:
			output = 'No users granted Privileges On AUD$.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
