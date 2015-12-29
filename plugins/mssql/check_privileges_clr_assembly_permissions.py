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
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output               = 'No assemblies without SAFE_ACCESS permission found.'

		for row in rows:
			for r in row:
				if 'SAFE_ACCESS' != r[1]:
					self.result['level'] = 'RED'
					output += r[0] + '\t' + r[1] + '\n'

		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
