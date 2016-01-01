class check_privilege_user_grantables():
	"""
    check_privilege_user_grantables:
	Privileges the application account can grant.
	"""
	# References:
	# http://dbadiaries.com/no-mysql-show-users-how-to-list-mysql-user-accounts-and-their-privileges
	# http://www.java2s.com/Code/SQL/User-Permission/MySQLPrivilegeTypes.htm

	TITLE    = 'User Grantables'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL      = '' # sql set on init
	
	verbose = False
	skip	= False
	result  = {}
	
	appuser = None

	def do_check(self, *results):
		if not self.skip:
			output               = ''
			self.result['level'] = 'GREEN'
			
			for rows in results:
				for row in rows:
					if 0 == len(output):
						output = output + 'grantee\ttable_catalog\tprivilege_type\n'
					
					self.result['level'] = 'YELLOW'
					output += row[0] + '\t' + row[1] + '\t' + row[2] + "\n"
			
			if 'GREEN' == self.result['level']:
				output = 'The application account (%s) has no grant privileges.' % (self.appuser)
			
			self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		if '' != parent.appuser:
			self.SQL     = "SELECT grantee, table_catalog, privilege_type FROM information_schema.user_privileges WHERE is_grantable='YES' AND grantee LIKE '''" + parent.appuser + "''%'"
			self.appuser = parent.appuser
		else:
			self.skip             = True
			self.result['level']  = 'GRAY'
			self.result['output'] = 'No application user set, check skipped.'
