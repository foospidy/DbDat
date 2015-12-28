import ConfigParser

class check_configuration_client_password():
	"""
	check_configuration_client_password:
    The [Client] section of the MySQL configuration file allows setting a password
    to be used. Verify this option is not used.
	"""
	# References:
	# https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/
    # https://dev.mysql.com/doc/refman/5.7/en/password-security-user.html

	TITLE    = 'Client Password'
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
			general_log_file = configuration.get('client', 'password')
            
			# if the option is found, then red!
			self.result['level']  = 'RED'
			self.result['output'] = 'Client password is in use.'
		except ConfigParser.NoOptionError as e:
			self.result['level']  = 'GREEN'
			self.result['output'] = 'Client password not used.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
