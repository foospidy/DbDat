import os
import csv
import hashlib
import binascii
import helper

class check_user_default_credentials():
    """
    check_user_default_credentials:
    Checks if an account is using credentials that appear on an Oracle default passworld list.
    """
    # Referecnes:
    # http://www.petefinnigan.com/default/default_password_list.htm
    # http://www.red-database-security.com/whitepaper/oracle_passwords.html
    # http://blog.red-database-security.com/2007/09/21/oracle-password-algorithm-11g-poc-code/
    # http://www.petefinnigan.com/weblog/archives/00001097.htm

    TITLE    = 'Default Credentials'
    CATEGORY = 'User'
    TYPE     = 'sql'
    SQL      = '' # set on init

    verbose   = False
    skip      = False
    result    = {}
    dbcurs    = None
    dbversion = None

    def do_check(self, *results):
        output        = ''
        password_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'etc', 'oracle_default_passwords.csv')
        field_names   = ['product', 'security_level', 'username', 'password', 'hash_value', 'commentary']

        for rows in results:
            for row in rows:
                with open(password_file) as passwords:
                    file = csv.DictReader(passwords, fieldnames=field_names)

                    for line in file:
                        if str(row[0]) == str(line['username']):
                            if int(self.dbversion) >= 11:
                                # sha-1 hash
                                ora_password = str(row[1])[2:]
                                ora_sha1     = ora_password[:40].upper()
                                ora_salt     = ora_password[40:60]
                                sha_hash     = hashlib.sha1()

                                sha_hash.update(line['password'])
                                sha_hash.update(binascii.a2b_hex(ora_salt))

                                if sha_hash.hexdigest().upper() == ora_sha1:
                                    self.result['level'] = 'RED'
                                    output += 'Default credential used for %s, commentary: %s' % (line['username'], line['commentary'])

                            else:
                                # DES
                                if line['hash_value'] == row[1]:
                                    self.result['level'] = 'RED'
                                    output += 'Default credential used for %s, commentary: %s' % (line['username'], line['commentary'])

        if 0 == len(output):
            self.result['level'] = 'GREEN'
            output += 'No default credentials found.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.dbversion = helper.get_version(parent.dbcurs)

        if int(self.dbversion) >= 11:
            # sha-1 hash
            self.SQL = "SELECT name, spare4 FROM sys.user$ WHERE password IS NOT NULL"
        else:
            # DES
            self.SQL = "SELECT username, password FROM dba_users"
