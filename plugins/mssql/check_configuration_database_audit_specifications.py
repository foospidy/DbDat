class check_configuration_database_audit_specifications():
    """
    check_configuration_database_audit_specifications:
    Auditing of defined database level events. Review to ensure proper auditing
    is enabled.
    """
    # References:
    # https://blog.netspi.com/sql-server-persistence-part-1-startup-stored-procedures/
    # https://gist.github.com/nullbind/5da8b5113da007ba0111

    TITLE    = 'Database Audit Specifications'
    CATEGORY = 'Configuration'
    TYPE     = 'sql'
    SQL      = """
                SELECT	a.audit_id,
                a.name as audit_name,
                s.name as database_specification_name,
                d.audit_action_name,
                s.is_state_enabled,
                d.is_group,
                s.create_date,
                s.modify_date,
                d.audited_result
                FROM sys.server_audits AS a
                JOIN sys.database_audit_specifications AS s
                ON a.audit_guid = s.audit_guid
                JOIN sys.database_audit_specification_details AS d
                ON s.database_specification_id = d.database_specification_id 
                WHERE s.is_state_enabled = 1
                """

    verbose = False
    skip    = False
    result  = {}

    def do_check(self, *results):
        
        for rows in results:
            if 0 == len(rows):
                self.result['level']  = 'RED'
                self.result['output'] = 'There are no database audit specifications enabled.'
                
            else:
               for row in rows:
                   self.result['level']  = 'YELLOW'
                   self.result['output'] = '%s %s %s %s \n' % (row[0], row[1], row[2], row[3])

        return self.result

    def __init__(self, parent):
        print('Performing check: ' + self.TITLE)
