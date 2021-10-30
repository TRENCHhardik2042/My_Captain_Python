import sqlite3

def connect(dbname):
    connection = sqlite3.connect(dbname)

    connection.execute(" CREATE TABLE IF NOT EXISTS OYO_MUMBAI (NAME TEXT , ADDRESS TEXT , PRICE INT, AMENITIES TEXT, RATING TEXT)")
    print("Table created successfully")
    connection.close()
    
    


def instert_into_table(dbname, values):
    connection = sqlite3.connect(dbname)
    print("Inserted intyo table: "+ str(values))
    insert_sql = "INSERT INTO OYO_HOTELS(NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)"
    connection.execute(insert_sql, values)
    connection.commit()
    connection.close()




def get_hotel_info(dbname):
    connection = sqlite3.connect(dbname)
    cur = connection.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data = cur.fetchall()

    for record in table_data :
            print(record)
    connection.close()


