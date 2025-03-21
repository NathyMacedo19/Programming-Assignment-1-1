#
import sqlite3
 
try:
   
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('sqlv2.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
 
    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)
 
    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
 
    # Close the cursor
    cursor.close()
 
# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)
 
# Close DB Connection irrespective of success
# or failure
finally:
   
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')