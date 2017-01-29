class check_privilege_public_links():
    """
    check_privilege_public_links
    Ensure no public database links exist
    A database link allows users to connect to a remote database server.
    """
    # References:
    # http://www.davidlitchfield.com/AddendumtotheOracle12cCISGuidelines.pdf
    
    TITLE    = 'PUBLIC Database Links'
    CATEGORY = 'Privilege'
    TYPE     = 'sql'
    SQL      = "SELECT DB_LINK FROM DBA_DB_LINKS WHERE OWNER = 'PUBLIC'"

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        self.result['level']  = 'GREEN'
        output                = ''

        for rows in results:
            for row in rows:
                self.result['level'] = 'RED'
                output += 'PUBLIC database link ' + row[0] + '\n'

        if 'GREEN' == self.result['level']:
            output = 'No PUBLIC Database Links.'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
