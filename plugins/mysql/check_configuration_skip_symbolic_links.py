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
	
	def do_check(self, *results):

		for rows in results:
			for row in rows:
				if 'DISABLED' != row[1]:
					self.result['level']  = 'RED'
					self.result['output'] = 'Symlinks is (%s) enabled.' % (row[1])
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'Symlinks is (%s) not enabled.' % (row[1])
			
			return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
