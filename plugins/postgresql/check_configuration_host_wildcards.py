import os
import helper

class check_configuration_host_wildcards():
	"""
	Are wildcards used when specifying allowed hosts?
	"""
	# References:
	# https://dba.stackexchange.com/questions/87049/postgresql-accept-subdomain-wildcards

	TITLE    = 'Wildcard Hosts'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = ''
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, configuration_file):
		output               = ''
		pg_hba_file_path     = None
		self.result['level'] = 'GREEN'

		pg_hba_file_path = helper.get_config_value(configuration_file, 'hba_file')

		try:
			if os.path.isfile(str(pg_hba_file_path)):
				with open(str(pg_hba_file_path), 'r') as config:
					for line in config:
						if not line.startswith('#'):
							if '' != line.strip():
								values = line.strip().split()
								if 'host' == values[0]:
									if not values[2].startswith('.'):
										self.result['level'] = 'RED'
										output +=  values[2] + '\n'
			
			self.result['output'] = output
			
		except IOError as e:
			self.result['level']  = 'ORANGE'
			self.result['output'] = 'DbDat could not read configuration file. You may need to run DbDat using sudo.'

		return self.result

	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
