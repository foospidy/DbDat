class check_privileges_explicit_grants():
	"""
	check_privileges_explicit_grants:
    Best practice is to grant privileges to roles and then add users as members
    of roles.
	"""
	# References:
	# https://www.mssqltips.com/sqlservertip/2739/issues-determining-an-individual-sql-server-users-permissions/

	TITLE    = 'Explicit Grants'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL    	 = '' # set on init
	
	verbose = False
	skip	= False
	result  = {}
	
	user    = ''
	
	def do_check(self, *results):
		self.result['level'] = 'GREEN'
		output = 'No explicit privileges granted to user'

		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output = 'Privileges explicitly granted to user (%s): table: %s privilege: %s.' % (self.user, row[1], row[2])
		
		if 'GREEN' == self.result['level']:
			output = 'No explicit privileges granted to user (%s).' % (self.user)
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.SQL  = "SELECT grantee, table_name, privilege_type FROM INFORMATION_SCHEMA.TABLE_PRIVILEGES WHERE grantee = '" + parent.appuser + "'"
		self.user = parent.appuser
