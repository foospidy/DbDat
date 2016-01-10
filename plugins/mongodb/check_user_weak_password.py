import os
from hashlib import md5

class check_user_weak_password():
    """
    check_user_weak_password:
    Accounts with weak passwords.
    """
    # References:

    TITLE    = 'Weak Password'
    CATEGORY = 'User'
    TYPE     = 'nosql'
    SQL    	 = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip	= False
    result  = {}
    
    db      = None

    def do_check(self):
        password_file         = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'etc', 'check_user_weak_password.txt')
        self.result['level']  = 'GREEN'
        output                = ''
        match                 = False
        
        try:
            database_list         = self.db.database_names()
            
            for database in database_list:
                cursor = self.db[database].system.users.find()
                
                for document in cursor:
                    with open(str(password_file), 'r') as passwords:
                        for password in passwords:
                            if md5(document['user'] + ':mongo:' + str(password.strip())).hexdigest() == document['pwd']:
                                match = True
                                output += 'database: %s user: %s\n' % (database, document['user'])
        
        except Exception as e:
            print e
            self.result['level']  = 'ORANGE'
            output                = 'Problem accessing database list, message:\n%s\n' % (e)

        if match:
            self.result['level']  = 'RED'
            output                = 'Weak password found for:\n %s' % (output)
        else:
            self.result['level']  = 'GREEN'
            output                = 'No weak password found.'

        self.result['output'] = output
        
        return self.result
	
    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
