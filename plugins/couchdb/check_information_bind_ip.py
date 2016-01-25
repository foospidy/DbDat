import ConfigParser


class check_information_bind_ip():
    """
    check_information_bind_ip:
    If your system has multiple network interfaces you can use the "bind_ip" option
    to restrict your couchdb server to listen only on the interfaces that are
    relevant. By default couchdb will bind to the loopback interface (127.0.0.1 or
    localhost).
    """
    # References:
    # http://guide.couchdb.org/draft/security.html

    TITLE    = 'Bind IP'
    CATEGORY = 'Information'
    TYPE     = 'configuration_file'
    SQL         = None  # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, configuration_file):
        configuration = ConfigParser.ConfigParser()

        try:
            configuration.read(configuration_file)

        except ConfigParser.ParsingError as e:
            if self.verbose:
                print('Ignoring parsing errors:\n' + str(e))

        try:
            bind_address = configuration.get('httpd', 'bind_address')

            if '127.0.0.1' == bind_address or 'localhost' == bind_address:
                self.result['level']  = 'GREEN'
                self.result['output'] = 'Database listening on localhost only. (' + str(bind_address) + ')'
            else:
                self.result['level']  = 'YELLOW'
                self.result['output'] = 'Database listening is not localhost only (' + str(bind_address) + ')'

        except ConfigParser.NoOptionError as e:
            self.result['level']  = 'GREEN'
            self.result['output'] = 'bind-address option not set, default is 127.0.0.1 or localhost.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
