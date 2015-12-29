class check_configuration_util_file_dir():
	"""
	check_configuration_util_file_dir:
	The	utl_file_dir setting allows packages like utl_file to access 
    (read/write/modify/delete) files specified in utl_file_dir.  (This is
    deprecated but usable in 11g.)
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Util File Dir'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT UPPER(value) FROM v$parameter WHERE UPPER(name)='UTIL_FILE_DIR'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		self.result['level'] = 'GREEN'
		output = 'UTIL_FILE_DIR is disabled.'
		
		for row in rows:
			if '' != row[0][0]:
				self.result['level'] = 'RED'
				output = 'UTIL_FILE_DIR is enabled.'

		self.result['output'] = output
			
		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
