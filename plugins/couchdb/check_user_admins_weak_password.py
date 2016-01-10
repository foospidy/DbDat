import os
from hashlib import sha1

class check_user_admins_weak_password():
    """
    check_user_admins_weak_password:
    Admin users with weak passwords.
    """
    # References:
    # http://guide.couchdb.org/draft/security.html

    TITLE    = 'Admins Weak Password'
    CATEGORY = 'Configuration'
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
            admins = self.db.config()['admins']
            
            for admin in admins:
                admin_hash       = admins[admin]
                admin_hash_parts = admin_hash.split(',')
                salt             = admin_hash_parts[1]
                
                with open(str(password_file), 'r') as passwords:
                    for password in passwords:
                        if '-hashed-' + sha1(password.strip() + salt).hexdigest() + ',' + salt == admin_hash:
                            match = True
                            output += '%s\n' % (admin)
        
        except Exception as e:
            self.result['level']  = 'ORANGE'
            output                = 'Problem accessing config, message:\n%s\n' % (e)
            
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
