import psycopg2

def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=euromast user=velid")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results
