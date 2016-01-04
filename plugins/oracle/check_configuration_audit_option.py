class check_configuration_audit_option():
	"""
	check_configuration_audit_option:
	Auditing database activity is critical to database security. Ensure sufficient
	auditing is enabled for your database and applications.
	"""
	# References:
    # https://benchmarks.cisecurity.org/downloads/show-single/?file=oracle11gR2.210

	TITLE    = 'Audit Option'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = ''  # set in init
	
	verbose = False
	skip	= False
	result  = {}
	
	audit_options = {
		'USER',
		'ALTER USER',
		'DROP USER',
		'ROLE',
		'SYSTEM GRANT',
		'ALTER PROFILE',
		'DROP PROFILE',
		'DATABASE LINK',
		'PUBLIC DATABASE LINK',
		'PUBLIC SYNONYM',
		'SYNONYM',
		'GRANT DIRECTORY',
		'SELECT ANY DICTIONARY',
		'GRANT ANY OBJECT PRIVILEGE',
		'GRANT ANY PRIVILEGE',
		'DROP ANY PROCEDURE',
		'PROCEDURE',
		'ALTER SYSTEM',
		'TRIGGER',
		'CREATE	SESSION'
		}
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''
		audit_options_found   = []

		for rows in results:
			for row in rows:
				audit_options_found.append(row[0])
		
		for option in self.audit_options:
			if option not in audit_options_found:
				self.result['level'] = 'YELLOW'
				output += 'Audit option (%s) not enabled.\n' % (option)

		if 'GREEN' == self.result['level']:
			output = 'Minimum set of audit options is enabled.'

		output += '\nEnabled audit options are:\n'
		
		for option in audit_options_found:
			output += '\t%s\n' % (option)
		
		self.result['output'] = output

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.SQL = "SELECT DISTINCT audit_option FROM dba_stmt_audit_opts WHERE user_name IS NULL AND proxy_name IS NULL AND success='BY ACCESS' AND failure='BY ACCESS'"
