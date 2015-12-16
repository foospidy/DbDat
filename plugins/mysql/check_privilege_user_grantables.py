class check_privilege_user_grantables():
	"""
	Privileges a user can grant.
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

	def do_check(self, *rows):
		if not self.skip:
			output               = ''
			self.result['level'] = 'GREEN'
			
			for row in rows:
				for r in row:
					if 0 == len(output):
						output = output + 'grantee\ttable_catalog\tprivilege_type\n'
					
					self.result['level'] = 'YELLOW'
					output = output + r[0] + '\t' + r[1] + '\t' + r[2] + "\n"
			
			self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		if '' != parent.appuser:
			self.SQL = "SELECT grantee, table_catalog, privilege_type FROM information_schema.user_privileges WHERE is_grantable='YES' AND grantee LIKE '''" + parent.appuser + "''%'"
		else:
			self.skip             = True
			self.result['level']  = 'GRAY'
			self.result['output'] = 'No application user set, check skipped.'
