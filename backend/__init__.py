try:
    import pymysql
    # Mocking a newer mysqlclient version to satisfy Django's requirements
    pymysql.version_info = (2, 2, 1, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
