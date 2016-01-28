import helper
from distutils.version import LooseVersion

class check_configuration_ssl_allow_invalid_cert():
    """
    check_configuration_ssl_allow_invalid_cert:
    Bypasses the validation checks for TLS/SSL certificates on other servers in
    the cluster and allows the use of invalid certificates. When using the 
    allowInvalidCertificates setting, MongoDB logs as a warning the use of the 
    invalid certificate.

    MongoDB versions 2.6.4 and above, check the net.ssl.weakCertificateValidation configuration option.
    """
    # References:
    # https://docs.mongodb.org/v2.6/reference/configuration-options/#net.ssl.allowInvalidCertificates

    TITLE    = 'Allow Invalid Certificate'
    CATEGORY = 'Configuration'
    TYPE     = 'configuration_file'
    SQL         = None # SQL not needed... because this is NoSQL.

    verbose = False
    skip    = False
    result  = {}

    db      = None

    def do_check(self, configuration_file):
        option         = None
        version_number = self.db.server_info()['version']
        
        if LooseVersion(version_number) >= LooseVersion("2.6.4"):
            option = 'net.ssl.allowInvalidCertificates'
            value  = helper.get_yaml_config_value(configuration_file, option)

            if None == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s not found, not enabled.' % (option)
            elif False == value:
                self.result['level']  = 'GREEN'
                self.result['output'] = '%s is (%s) not enabled.' % (option, value)
            else:
                self.result['level']  = 'RED'
                self.result['output'] = '%s is (%s) enabled.' % (option, value)

        else:
            self.result['level']  = 'GRAY'
            self.result['output'] = 'This check does not apply to MongoDB versions below 2.6.4.'

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)

        self.verbose = parent.verbose
        self.db      = parent.db
