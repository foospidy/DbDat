class check_privileges_user_privilege():
	"""
	Show current user database privileges
	"""
	# References:
	# https://vibhorkumar.wordpress.com/2012/07/29/list-user-privileges-in-postgresqlppas-9-1/

	TITLE    = 'User Priv'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = ''
	
	verbose = False
	skip	= False
	result  = {}
	appuser = None
	
	def do_check(self, *rows):
		output  = ''
		
		for row in rows:
			for r in row:
				output = output + str(r[0]) + ' ' + str(r[1]) + ' ' + str(r[2]) + '\n'
				
				if 'GRANT ALL' in r[0]:
					result['level'] = 'RED'
				
				if 'ON *.* TO' in r[0]:
					result['level'] = 'RED'
					
				if 'WITH GRANT OPTIONS' in r[0]:
					result['level'] = 'RED'
				
				if 'GRANT PROXY' in r[0]:
					result['level'] = 'RED'
			
			result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		if '' != parent.appuser:
			self.appuser = parent.appuser
			
			self.SQL = "SELECT '" + self.appuser + "', datname, array(select privs from unnest(ARRAY[(CASE WHEN has_database_privilege('" + self.appuser + "',c.oid,'CONNECT') THEN 'CONNECT' ELSE NULL END), (CASE WHEN has_database_privilege('" + self.appuser + "',c.oid,'CREATE') THEN 'CREATE' ELSE NULL END), (CASE WHEN has_database_privilege('" + self.appuser + "',c.oid,'TEMPORARY') THEN 'TEMPORARY' ELSE NULL END), (CASE WHEN has_database_privilege('" + self.appuser + "',c.oid,'TEMP') THEN 'CONNECT' ELSE NULL END)])foo(privs) WHERE privs IS NOT NULL) FROM pg_database c WHERE has_database_privilege('" + self.appuser + "',c.oid,'CONNECT,CREATE,TEMPORARY,TEMP') AND datname <> 'template0';"
			print self.SQL
			
