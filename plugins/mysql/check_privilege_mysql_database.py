class check_privilege_mysql_database():
    """
    check_privilege_mysql_database:
    Non Admin database users should not have access to the "mysql" database.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'mysql Database Access'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT user, host FROM mysql.db WHERE db='mysql' AND ((Select_priv = 'Y') OR (Insert_priv = 'Y') OR (Update_priv = 'Y') OR (Delete_priv = 'Y') OR (Create_priv = 'Y') OR (Drop_priv = 'Y'))"

    verbose = False
    skip	= False
    result  = {}

    def do_check(self, *results):
		if not self.skip:
			output               = ''
			self.result['level'] = 'GREEN'

			for rows in results:
				for row in rows:
					self.result['level'] = 'RED'
					output += row[0] + '\t' + row[1] + '\n'

			if 'GREEN' == self.result['level']:
				output = 'No users found with privileges to the mysql database.'

			self.result['output'] = output

		return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
