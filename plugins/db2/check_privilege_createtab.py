class check_privilege_createtab():
	"""
	check_privilege_createtab:
	The CREATETABAUTH (create table) role grants the authority to a user to create tables within a
	specific database. It is recommended thatthe createtab role be granted to authorized
	users only.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=db2.120

	TITLE    = 'CREATETABAUTH Role'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = "SELECT DISTINCT grantee, granteetype FROM syscat.dbauth WHERE createtabauth='Y'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		output = ''
		self.result['level']  = 'GREEN'
		
		for rows in results:
			for row in rows:
				self.result['level']  = 'YELLOW'
				output += 'CREATETABAUTH granted to %s\n' % (row[0])
					
		if 'GREEN' == self.result['level']:
			output = 'No users granted CREATETABAUTH.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
