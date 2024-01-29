# Necessary imports
# cx_Oracle is a Python extension module that enables access to Oracle Database
# SQLAlchemy is the Python SQL toolkit and Object Relational Mapper 
import cx_Oracle
from sqlalchemy import create_engine, exc, MetaData

# Personal Oracle 21c Database Credentials
oracle_user = 'sys'
oracle_password = 'NmweaC3Savl0kZP8nIam'
oracle_host = 'localhost'
oracle_port = '1521'  # Default Oracle listener port
oracle_service_name = 'xe'  # or SID, depending on your Oracle Database configuration

# Create connection string with SYSDBA/SYSOPER role
connection_str = f'oracle+cx_oracle://{oracle_user}:{oracle_password}@{oracle_host}:{oracle_port}/{oracle_service_name}?mode=SYSDBA'

# Create a metadata object
metadata = MetaData()

# SQLAlchemy engine
engine = create_engine(connection_str)

# Complex error handling
# Test if the connection is made or not
try:
    # Establish a connection and print success message if successful
    with engine.connect() as connection:
        print('Successfully connected to the Oracle database as SYSDBA')
except cx_Oracle.DatabaseError as db_err:
    # Handle Oracle Database errors
    print(f'Sorry, failed to connect to the Oracle database: {db_err}')
except exc.OperationalError as op_err:
    # Handle Operational errors (e.g., connection issues)
    print(f'Sorry, an operational error occurred: {op_err}')
except Exception as ex:
    # Handle other unexpected errors
    print(f'An unexpected error occurred: {ex}')



