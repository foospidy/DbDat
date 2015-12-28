class check_configuration_skip_symbolic_links():
	"""
	check_configuration_skip_symbolic_links:
    Prevents sym links being used for data base files. This is especially
    important when MySQL is executing as root as arbitrary files may be overwritten.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'Skip Symbolic Links'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SHOW GLOBAL VARIABLES LIKE 'have_symlink'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):		
		for row in rows:
			for r in row:
				if 'DISABLED' != r[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Symlinks is enabled.'
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Symlinks is disabled.'
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
