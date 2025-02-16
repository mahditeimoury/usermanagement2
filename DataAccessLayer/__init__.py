import pyodbc
conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-U0RMNUE\\SQL2022;'
        'DATABASE=user_management;'
        'UID=sa;'
        'PWD=kmtokt2000;'
        "Trusted_Connection=yes;"
    )