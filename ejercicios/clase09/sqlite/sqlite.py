import sqlite3

connection = sqlite3.connect('blog.db')

cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS post(
        id number PRIMARY KEY , 
        title text, 
        body text, 
        pub_date text
        )
    """
)

cursor.execute(
    """
      INSERT INTO post VALUES (1, "Hello world", "lorem ipsum", "");
    """
)

connection.commit()

