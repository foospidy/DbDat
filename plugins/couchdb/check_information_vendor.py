class check_information_vendor():
    """
    check_information_vendor:
    CouchDB vendor information.
    """
    # References:

    TITLE    = 'Vendor'
    CATEGORY = 'Information'
    TYPE     = 'nosql'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}
    db      = None

    def do_check(self):
        self.result['level']  = 'GREEN'
        vendor                = self.db.config()['vendor']
        output                = ''

        for info in vendor:
            output += info + ': ' + vendor[info] + '\n'

        self.result['output'] = output

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
        self.db = parent.db
