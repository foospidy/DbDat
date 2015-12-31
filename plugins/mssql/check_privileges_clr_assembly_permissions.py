class check_privileges_clr_assembly_permissions():
	"""
	check_privileges_clr_assembly_permissions:
    Setting CLR Assembly Permission Sets to SAFE_ACCESS will prevent assemblies 
    from accessing external system resources such as files, the network, 
    environment variables, or the registry.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=sql2012DB.120

	TITLE    = 'CLR Assembly Permissions'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, permission_set_desc FROM sys.assemblies WHERE is_user_defined=1"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):
		self.result['level'] = 'GREEN'
		output               = ''

		for rows in results:
			for row in rows:
				if 'SAFE_ACCESS' != row[1]:
					self.result['level'] = 'RED'
					output += row[0] + '\t' + row[1] + '\n'

		if 'GREEN' == self.result['level']:
			output = 'Assemblies without SAFE_ACCESS permission not found.'
		
		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
