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
	
	def do_check(self, *results):
		self.result['level']  = 'GREEN'
		output                = ''
		
		for rows in results:
			for row in rows:
				self.result['level'] = 'YELLOW'
				output +='user: ' + str(row[0]) + ' host: ' + str(row[1]) + '\n'
		
		if 'GREEN' == self.result['level']:
			output = 'No remote hosts found.'
			
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
