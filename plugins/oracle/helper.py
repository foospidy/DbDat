def get_version(dbcurs):
    version = None

    dbcurs.execute("SELECT * FROM v$version")

    rows    =   dbcurs.fetchall()
    version = str(rows[0]).split()[-3].split('.')[0]

    return version
