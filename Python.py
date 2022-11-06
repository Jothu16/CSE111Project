import sqlite3

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

# cursor.execute("""CREATE TABLE Function_Table(
#     AQ_Key INTEGER PRIMARY KEY,
#     Date TEXT,
#     Country TEXT,
#     Status TEXT,
#     AQI_Value TEXT,
#     Continent TEXT,
#     )""")

# Add Function_Table to the table and commit these changes to the database
Function_Table = (1,'2022-07-21','Albania','Good',14,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (2,'2022-07-21','Algeria','Moderate',65,'Africa')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (3,'2022-07-21','Andorra','Moderate',55,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (4, '2022-07-21','Angola','Unhealthy for Sensitive Groups',113,'Africa')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (5, '2022-07-21','Argentina','Moderate',63,'South America')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (6, '2022-07-21','Armenia','Moderate',76,'Asia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (7, '2022-07-21','Australia','Moderate',56,'Oceania')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (8, '2022-07-21','Austria','Good',45,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (9, '2022-07-21','Azerbaijan','Good',12,'Asia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (10, '2022-07-21','Bahrain','Unhealthy',165,'Asia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (11,'2022-07-21','Bangladesh','Unhealthy for Sensitive Groups',141,'Asia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (12, '2022-07-21','Belarus','Good',13,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (13, '2022-07-21','Belgium','Moderate',61,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (14, '2022-07-21','Belize','Good',28,'North America')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (15, '2022-07-21','Bermuda','Good',12,'North America')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (16, '2022-07-21','Bolivia','Good',9,'South America')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (17, '2022-07-21','Bosnia and Herzegovina','Moderate',58,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (18, '2022-07-21','Brazil','Moderate',67,'South America')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (19, '2022-07-21','Brunei','Good',15,'Asia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (20, '2022-07-21','Bulgaria','Good',28,'Europe')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (21, '2022-07-21','Burkina Faso','Unhealthy for Sensitive Groups',118,'Africa')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?)", Function_Table)
db.commit()

#Delete data(needs fixing or maybe put into separate file)
cursor.execute("DELETE FROM Function_Table WHERE AQ_Key = 1000") #change number to which key you want to delete (leave at 1000 to not delete anything)

#Select statment get data from Function_Table
cursor.execute("SELECT * FROM Function_Table")
Function_Table = cursor.fetchall()

# Loops through prints each row
for row in Function_Table:
    print(row)