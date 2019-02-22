import _mysql

db =_mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="my-secret-pw",
    db="blog"
)

db.query(
    """
        CREATE TABLE IF NOT EXISTS post(
        id serial PRIMARY KEY , 
        title VARCHAR(80), 
        body text, 
        pub_date TIMESTAMP 
        )
    """
)


db.query(
    """
      INSERT INTO post (id, title, body, pub_date) VALUES (1, 'Hello world', 'lorem ipsum', '2018-10-12');
    """
)

db.commit()

db.query(
    """
    SELECT * FROM post;
    """
)


rows = db.store_result()

rows.fetch_row()