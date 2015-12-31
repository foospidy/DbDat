class check_configuration_local_infile():
	"""
	check_configuration_local_infile
	"""
	# References:

	TITLE    = 'Load Local Data'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "CREATE TEMPORARY TABLE dbdat_temp_infile (dbdat_text TEXT); COPY dbdat_temp_infile FROM '/etc/shadow'; SELECT * FROM dbdat_temp_infile LIMIT 1"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *results):		
		for rows in results:
			for row in rows:
				if 'must be superuser' not in row[0]:
					self.result['level']  = 'RED'
					self.result['output'] = row[0]
				else:
					self.result['level']  = 'GREEN'
					self.result['output'] = row[0]

		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
