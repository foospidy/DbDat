class check_privilege_tablespaces():
	"""
	check_privilege_tablespaces:
	A tablespace is where the data is physically stored. It is recommended that
	tablespace usage be restricted to authorized users.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'Tablespaces'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT tbspace FROM sysibm.systbspaceauth WHERE grantee='PUBLIC'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output = ''
		self.result['level']  = 'GREEN'
		
		for rows in results:
			for row in rows:
				self.result['level']  = 'RED'
				output += '%s granted to PUBLIC.\n' % (row[0])
					
		if 'GREEN' == self.result['level']:
			output = 'Tablespaces not granted to PUBLIC.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
