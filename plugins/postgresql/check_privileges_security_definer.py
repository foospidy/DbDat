class check_privileges_security_definer():
	"""
	Security Definer
	"""
	# References:
	# https://vibhorkumar.wordpress.com/2012/07/29/list-user-privileges-in-postgresqlppas-9-1/

	TITLE    = 'Security Definer'
	CATEGORY = 'User'
	TYPE     = 'sql'
	SQL    	 = "SELECT pg_proc.proname, pg_namespace.nspname, pg_user.usename FROM pg_proc JOIN pg_namespace ON pg_proc.pronamespace=pg_namespace.oid JOIN pg_user ON pg_proc.proowner=pg_user.usesysid WHERE prosecdef='t';"
	
	verbose = False
	skip	= False
	result  = {}
	appuser = None
	
	def do_check(self, *rows):
		output = ''
		
		if 0 == len(rows[0]):
			self.result['level'] = 'GREEN'
			output               = 'No security definer functions found.'
		
		for row in rows:
			for r in row:
				output += str(r[0]) + ' ' + str(r[1]) + ' ' + str(r[2]) + '\n'
				self.result['level'] = 'RED'
			
		self.result['output'] = output
		
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
