import ConfigParser

class check_configuration_listen_addresses():
	"""
	check_configuration_listen_addresses
	"""
	# References:
	# https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/

	TITLE    = 'Listen Addresses'
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
			bind_address = configuration.get('mysqld', 'bind-address')[0]
			
			if '127.0.0.1' == bind_address or 'localhost' == bind_address: 
				self.result['level']  = 'GREEN'
				self.result['output'] = 'Database listening on localhost only. (' + str(bind_address) + ')'
			else:
				self.result['level']  = 'YELLOW'
				self.result['output'] = 'Database listening is not localhost only (' + str(bind_address) + ')'
					
		except ConfigParser.NoOptionError as e:		
			self.result['level']  = 'YELLOW'
			self.result['output'] = 'bind-address option not set, default is (\'*\')'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
