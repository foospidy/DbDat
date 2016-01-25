import os
import helper

class check_information_remote_hosts():
    """
    Error log file
    """
    # References:
    # http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html

    TITLE    = 'Remote Host'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, configuration_file):
        output               = ''
        pg_hba_file_path     = None
        self.result['level'] = 'GREEN'

        pg_hba_file_path = helper.get_config_value(configuration_file, 'hba_file')

        try:
            if os.path.isfile(str(pg_hba_file_path)):
                with open(str(pg_hba_file_path), 'r') as config:
                    for line in config:
                        if not line.startswith('#'):
                            if '' != line.strip():
                                output += line.strip() + '\n'

            self.result['output'] = output

        except IOError as e:
            self.result['level']  = 'ORANGE'
            self.result['output'] = 'DbDat could not read configuration file. You may need to run DbDat using sudo.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
