import psycopg2

# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=project2 user=postgres host='localhost' password='Drakenadem97'")
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


# Uploads a score into the hiscore table
def upload_score(name, score):
    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                           .format(score, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM highscores")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM highscores ORDER BY score")[0][1]
    return result
def insert_player(name,score):
    interact_with_database("INSERT INTO highscores(name, score) VALUES('{}',{})".format(name,score))



def naam_check(name):
    interact_with_database("SELECT highscores.name  FROM highscores WHERE name != name")

