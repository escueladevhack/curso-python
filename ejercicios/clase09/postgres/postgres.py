import psycopg2

connection = psycopg2.connect("dbname=blog user=postgres password=your_secret_password host=localhost")

cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS post(
        id serial PRIMARY KEY , 
        title VARCHAR(80), 
        body text, 
        pub_date TIMESTAMP 
        )
    """
)

cursor.execute(
    """
      INSERT INTO post (id, title, body, pub_date) VALUES (1, 'Hello world', 'lorem ipsum', '2018-10-12');
    """
)

connection.commit()


cursor.execute(
    """
    SELECT * FROM post;
    """
)

rows = cursor.fetchall()