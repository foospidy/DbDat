import ConfigParser
import os.path
 
class check_user_access_denied():
	"""
	Access denied for user
	"""
	# References:
	# https://www.percona.com/blog/2012/12/28/auditing-login-attempts-in-mysql/

	TITLE    = 'User Access Denied'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None
	
	
	verbose = False
	skip	= False
	result  = {}
	appuser = None
	
	def do_check(self, configuration_file):
		configuration = ConfigParser.ConfigParser()
		count         = 0
	
		try:
			configuration.read(configuration_file)
		
		except ConfigParser.ParsingError as e:
			if self.verbose:
				print('Ignoring parsing errors:\n' + str(e))
		
		try:
			error_log_file = configuration.get('mysqld', 'log_error')[0]
			
			if os.path.isfile(str(error_log_file)):
				with open(str(error_log_file), 'r') as log:
					for line in log:
						if "Access denied for user '" + self.appuser + "'" in line:
							count += 1

				if 0 == count:
					self.result['level']  = 'GREEN'
					self.result['output'] = 'No access denied events found for user.'
				
				elif count < 5:
					self.result['level']  = 'YELLOW'
					self.result['output'] = 'Access denied events found for user.'
				
				else:
					self.result['level']  = 'RED'
					self.result['output'] = 'Excessive access denied events found for user.'
			
			else:
				self.result['level']  = 'YELLOW'
				self.result['output'] = 'Could not access error log file ' + str(error_log_file) + '.'
		
		except ConfigParser.NoOptionError as e:
			self.result['level']  = 'RED'
			self.result['output'] = 'Error log file not enabled.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
		
		if '' != parent.appuser:
			self.appuser = parent.appuser
		else:
			self.skip             = True
			self.result['level']  = 'GRAY'
			self.result['output'] = 'No application user set, check skipped.'
