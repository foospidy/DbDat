class check_configuration_skip_networking():
	"""
	check_configuration_skip_networking:
    Do not allow TCP/IP connections; do not bind to a port. Use if no remote
    access is needed.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'Skip Networking'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW GLOBAL VARIABLES LIKE 'skip_networking'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		for row in rows:
			for r in row:
				if 'ON' != r[1]:
					self.result['level']  = 'Yellow'
					self.result['output'] = 'Networking is enabled.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Networking is disabled.'
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
