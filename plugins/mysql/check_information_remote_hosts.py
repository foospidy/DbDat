class check_information_remote_hosts():
	"""
    check_information_remote_hosts:
	Review allowed remote hosts. Administrative accounts (e.g. root) should only
    connect from localhost.
	"""
	# References:

	TITLE    = 'Remote Hosts'
	CATEGORY = 'Information'
	TYPE     = 'sql'
	SQL    	 = "SELECT user, host FROM mysql.user WHERE host NOT LIKE '%127.0.0.1' AND host NOT LIKE '%localhost'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output  = ''
		
		for row in rows:
			if len(row) > 0:
				self.result['level'] = 'YELLOW'
				
				for r in row:
					output = output + 'user: ' + str(r[0]) + ' host: ' + str(r[1]) + '\n'
					self.result['output'] = output
				
			else:
				self.result['level']  = 'GREEN'
				self.result['output'] = 'No remote hosts found.'
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
