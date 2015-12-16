from pg_read_config import *

class check_information_remote_hosts():
	"""
	Error log file
	"""
	# References:
	# http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html

	TITLE    = 'Remote Host'
	CATEGORY = 'Configuration'
	TYPE     = 'configuration_file'
	SQL    	 = None
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, configuration_file):
		output               = ''
		pg_hba_file_path     = None
		self.result['level'] = 'GREEN'
		
		pg_hba_file_path = get_pg_config_value(configuration_file, 'hba_file')
		
		if os.path.isfile(str(pg_hba_file_path)):
			with open(str(pg_hba_file_path), 'r') as config:
				for line in config:
					if not line.startswith('#'):
						if '' != line.strip():
							output += line.strip() + '\n'

			self.result['output'] = output
		
		else:
			print 'fuuu'
	
		return self.result
		
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
		
		self.verbose = parent.verbose
