import re

class check_configuration_admin_restrictions_listener():
	"""
	check_configuration_admin_restrictions_listener
	"""
	# References:
	# http://docs.oracle.com/cd/B19306_01/network.102/b14266/policies.htm

	TITLE    = 'Admin Restrictions Listener'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, configuration_file):
		self.result['level']  = 'RED'
		self.result['output'] = 'ADMIN_RESTRICTIONS_LISTENER is not enabled.'
		
		try:
			with open(configuration_file) as file:
				for line in file:
					if not line.strip().startswith('#'):
						if re.match('^ADMIN_RESTRICTIONS_LISTENER\s*?=\s*?ON$', line.strip()):
							self.result['level']  = 'GREEN'
							self.result['output'] = 'ADMIN_RESTRICTIONS_LISTENER is enabled.'
			
		except Exception as e:
			if self.verbose:
				print('Cannot read configuration file:\n' + str(e))
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
