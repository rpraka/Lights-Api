from auth_keys import auth_keys
import os
import psycopg2

def setup_db():
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS light_meta (
        id integer NOT NULL,  
        status integer NOT NULL
        );
        """)

    conn.commit()
    
    for id in auth_keys:
        cursor.execute(""" INSERT INTO light_meta (id, status) values (%s,-1); """,(id,))
    conn.commit()

    return conn, cursor
