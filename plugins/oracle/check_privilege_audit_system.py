class check_privilege_audit_system():
	"""
	check_privilege_audit_system:
	The	Oracle database AUDIT SYSTEM privilege allows the change auditing
	activities on the system.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Audit System'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='AUDIT SYSTEM' AND grantee NOT IN ('DBA','DATAPUMP_IMP_FULL_DATABASE','IMP_FULL_DATABASE','SYS')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Audit System granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Audit System.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
