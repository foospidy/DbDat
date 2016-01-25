class check_privilege_user_grants():
    """
    check_privilege_user_grants
    The application account's privileges.
    """
    # References:
    # reference: http://dbadiaries.com/no-mysql-show-users-how-to-list-mysql-user-accounts-and-their-privileges

    TITLE    = 'User Grants'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = '' # sql set on init

    verbose = False
    skip    = False
    result  = {}
    dbcurs  = None

    def do_check(self, *results):
        if not self.skip:
            output  = ''
            self.result['level'] = 'GREEN'

            for rows in results:
                for r in rows:
                    self.SQL = "SHOW GRANTS FOR '" + r[0] + "'@'" + r[1] + "'"

                    self.dbcurs.execute(self.SQL)

                    rows = self.dbcurs.fetchall()

                    for row in rows:
                        grant = row[0].split('IDENTIFIED')[0] # don't want to capture password field
                        if 'GRANT ALL' in grant:
                            self.result['level'] = 'RED'
                            output += 'GRANT ALL:\t' + grant + '\n'

                        if 'ON *.* TO' in grant:
                            self.result['level'] = 'RED'
                            output += 'ON *.*:\t\t' + grant + '\n'

                        if 'WITH GRANT OPTION' in grant:
                            self.result['level'] = 'RED'
                            output += 'GRANT OPTION:\t' + grant + '\n'

                        if 'GRANT PROXY' in grant:
                            self.result['level'] = 'RED'
                            output += 'GRANT PROXY:\t' + grant + '\n'

            self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        if '' != parent.appuser:
            self.SQL    = "SELECT user, host FROM mysql.user WHERE user='" + parent.appuser + "'"
            self.dbcurs = parent.dbcurs

        else:
            self.skip             = True
            self.result['level']  = 'GRAY'
            self.result['output'] = 'No application user set, check skipped.'
