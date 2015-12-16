class check_configuration_host_wildcards():
	"""
	Are wildcards used when specifying allowed hosts?
	"""
	# References:

	TITLE    = 'Wildcard Hosts'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.user WHERE host LIKE '%\%%'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			if len(row) > 0:
				self.result['level'] = 'RED'
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No wildcard hosts found.'
			
			for r in row:
				output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
				self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
