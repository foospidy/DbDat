class check_privilege_mysql_database():
	"""
	check_privilege_mysql_database
	"""
	# References:
	# 

	TITLE    = 'MySQL Databse'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL      = "SELECT user, host FROM mysql.db WHERE db='mysql' AND ((Select_priv = 'Y') OR (Insert_priv = 'Y') OR (Update_priv = 'Y') OR (Delete_priv = 'Y') OR (Create_priv = 'Y') OR (Drop_priv = 'Y'))"
	
	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *rows):
		if not self.skip:
			output               = ''
			self.result['level'] = 'GREEN'
			
			for row in rows:
				for r in row:					
					self.result['level'] = 'RED'
					output = output + r[0] + '\t' + r[1] + '\n'
			
			self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
