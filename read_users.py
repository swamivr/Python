import sys

try:
    import pyodbc
except ImportError:
    print("Error: 'pyodbc' module is not installed. Run: pip install pyodbc")
    sys.exit(1)

try:
    from tabulate import tabulate
except ImportError:
    print("Error: 'tabulate' module is not installed. Run: pip install tabulate")
    sys.exit(1)


def read_persons():
    """Connect to AdventureWorks and print Person.Person table in tabular format."""
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=AdventureWorks2014;"
        "Trusted_Connection=yes;"
    )

    conn = None
    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to the database successfully.\n")
    except pyodbc.InterfaceError as e:
        print(f"Connection failed: ODBC driver not found or misconfigured.\n{e}")
        sys.exit(1)
    except pyodbc.OperationalError as e:
        print(f"Connection failed: Unable to reach the SQL Server.\n{e}")
        sys.exit(1)
    except pyodbc.DatabaseError as e:
        print(f"Connection failed: Database error occurred.\n{e}")
        sys.exit(1)

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Person.Person")

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        if rows:
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            print(f"\nTotal records: {len(rows)}")
        else:
            print("No records found in the Person.Person table.")

    except pyodbc.ProgrammingError as e:
        print(f"Query error: The 'Person.Person' table may not exist or the query is invalid.\n{e}")
        sys.exit(1)
    except pyodbc.Error as e:
        print(f"Database error while fetching data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        try:
            conn.close()
            print("\nDatabase connection closed.")
        except Exception:
            pass


if __name__ == "__main__":
    read_persons()
