class check_privilege_grant_any_object_privilege():
	"""
	check_privilege_grant_any_object_privilege:
	The	Oracle database GRANT ANY OBJECT PRIVILEGE keyword provides the grantee
	the capability to grant access to any single or multiple combinations of
	objects to any grantee	in the catalog of the database.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Grant Any Object Privilege'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='GRANT ANY OBJECT PRIVILEGE' AND grantee NOT IN ('SYS','SYSTEM','DBA')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Grant Any Object Privilege granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Grant Any Object Privilege.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
