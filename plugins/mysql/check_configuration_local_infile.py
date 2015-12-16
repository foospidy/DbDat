class check_configuration_local_infile():
	"""
	check_configuration_local_infile
	"""
	# References:
	# https://dev.mysql.com/doc/refman/5.5/en/load-data-local.html

	TITLE    = 'Load Local data'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW GLOBAL VARIABLES LIKE 'local_infile'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			for r in row:
				if 'ON' == r[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Load local data is enabled.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Load local data is disabled.'
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
