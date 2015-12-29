class check_configuration_remote_os_roles():
	"""
	check_configuration_remote_os_roles:
	The	remote_os_roles setting	permits remote users' OS roles to be applied to database
    management.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Remote OS Roles'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='REMOTE_OS_ROLES'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output       = ''
		for row in rows:
			if 'TRUE' == row[0][0]:
				self.result['level'] = 'RED'
				output += 'REMOTE_OS_ROLES is enabled. Set remtoe_os_authent to FALSE.'
			else:
				self.result['level'] = 'GREEN'
				output += 'REMOTE_OS_ROLES is disabled.'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
