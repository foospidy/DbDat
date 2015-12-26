import ConfigParser

class check_configuration_error_log():
	"""
	check_configuration_error_log
    In order to log failed login attemtps ensure error logging is enabled with 
    the log_warnings set to a value greater than 1.
	"""
	# References:
	# https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/

	TITLE    = 'Error Log'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, configuration_file):
		configuration = ConfigParser.ConfigParser()
	
		try:
			configuration.read(configuration_file)
			
		except ConfigParser.ParsingError as e:
			if self.verbose:
				print('Ignoring parsing errors:\n' + str(e))
		
		try:
			general_log_file      = configuration.get('mysqld', 'log_error')
			self.result['level']  = 'GREEN'
			self.result['output'] = 'Error log file enabled.'
			
			log_warnings = configuration.get('mysqld', 'log_warnings')
			
			if log_warnings < 2:
				self.result['level']  = 'RED'
				self.result['output'] = 'Error log not capturing access denied events.'
					
		except ConfigParser.NoOptionError as e:
			self.result['level']  = 'RED'
			self.result['output'] = 'Error log file not enabled.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
