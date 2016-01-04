class check_privilege_create_library():
	"""
	check_privilege_create_library:
	The	Oracle database CREATE LIBRARY privilege allows the designated user
	to create objects that are associated to the shared libraries.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Create Library'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT grantee, privilege FROM dba_sys_privs WHERE privilege='CREATE LIBRARY' AND grantee NOT IN ('SYS','SYSTEM','DBA')"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output += 'Create Library granted to ' + row[0] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'No users granted Create Library.'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
