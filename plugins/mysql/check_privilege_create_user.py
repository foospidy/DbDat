class check_privilege_create_user():
    """
    check_privilege_create_user:
    The following accounts have the CREATE USER privilege. Do not grant to non Admin users.
    """
    # References:
    # https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

    TITLE    = 'CREATE USER Privilege'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT user, host FROM mysql.user WHERE Create_user_priv='Y'"

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
                    output += r[0] + '\t' + r[1] + '\n'
            
            if 'GREEN' == self.result['level']:
                output = 'No users found with CREATE USER privilege.'
            
            self.result['output'] = output
            
        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
