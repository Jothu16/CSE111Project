import sqlite3

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

cursor.execute("DROP TABLE Function_Table")
cursor.execute("DROP TABLE Users")
cursor.execute("DROP TABLE Continent")
cursor.execute("DROP TABLE Region")
cursor.execute("DROP TABLE Capital_City")
cursor.execute("DROP TABLE History")
cursor.execute("DROP TABLE Status")
db.commit()

cursor.execute("""CREATE TABLE Function_Table(
    AQ_Key INTEGER PRIMARY KEY,
    Date TEXT,
    Country TEXT,
    Status TEXT,
    AQI_Value TEXT,
    Continent TEXT,
    Capital City TEXT
    )""")

cursor.execute("""CREATE TABLE Users(
     Usser_Key INTEGER PRIMARY KEY,
     First_Name TEXT,
     Last_Name TEXT
     )""")

cursor.execute("""CREATE TABLE Continent(
     Cont_Key INTEGER PRIMARY KEY,
     Name TEXT
     )""")

cursor.execute("""CREATE TABLE Region(
     Region_Key INTEGER PRIMARY KEY,
     Continent_Name TEXT,
     Name TEXT
     )""")

cursor.execute("""CREATE TABLE Capital_City(
     City_Key INTEGER PRIMARY KEY,
     Continent_Name TEXT,
     Region_Name TEXT, 
     Name TEXT
     )""")

cursor.execute("""CREATE TABLE History(
    History_Key INTEGER PRIMARY KEY,
    Date TEXT,
    Country TEXT,
    Status TEXT,
    AQI_Value TEXT,
    Continent TEXT,
    Capital City TEXT
    )""")

cursor.execute("""CREATE TABLE Status(
     Status_Key INTEGER PRIMARY KEY,
     Description TEXT,
     Threshold_Lower INTEGER,
     Threshold_Upper INTEGER
     )""")

#Populate Status Table
Status = (1, 'Good', 0, 50)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (2, 'Moderate', 51, 100)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (3, 'Unhealthy for Sensitive Groups', 101, 150)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (4, 'Unhealthy', 151, 200)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (5, 'Very Unhealthy', 201, 300)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (6, 'Very Unhealthy', 301, 999999)
cursor.execute("INSERT OR REPLACE INTO Status VALUES(?,?,?,?)", Status)
db.commit()

# Add Function_Table to the table and commit these changes to the database
Function_Table = (1,'2022-07-21','Albania','Good',14,'Europe','Tirana')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (2,'2022-07-21','Algeria','Moderate',65,'Africa','Algiers')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (3,'2022-07-21','Andorra','Moderate',55,'Europe','Andorra la Vella')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (4, '2022-07-21','Angola','Unhealthy for Sensitive Groups',113,'Africa','Luanda')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (5, '2022-07-21','Argentina','Moderate',63,'South America','Buenos Aires')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (6, '2022-07-21','Armenia','Moderate',76,'Asia','Yerevan')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (7, '2022-07-21','Australia','Moderate',56,'Oceania','Canberra')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (8, '2022-07-21','Austria','Good',45,'Europe','Vienna')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (9, '2022-07-21','Azerbaijan','Good',12,'Asia','Baku')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (10, '2022-07-21','Bahrain','Unhealthy',165,'Asia','Manama')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (11,'2022-07-21','Bangladesh','Unhealthy for Sensitive Groups',141,'Asia','Dhaka')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (12, '2022-07-21','Belarus','Good',13,'Europe','Minsk')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (13, '2022-07-21','Belgium','Moderate',61,'Europe','Brussels')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (14, '2022-07-21','Belize','Good',28,'North America','Belmopan')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (15, '2022-07-21','Bermuda','Good',12,'North America','Hamilton')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (16, '2022-07-21','Bolivia','Good',9,'South America','Sucre')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (17, '2022-07-21','Bosnia and Herzegovina','Moderate',58,'Europe','Sarajevo')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (18, '2022-07-21','Brazil','Moderate',67,'South America','Brasilia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (19, '2022-07-21','Brunei','Good',15,'Asia','Banda Seri Begawan')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (20, '2022-07-21','Bulgaria','Good',28,'Europe','Sofia')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

Function_Table = (21, '2022-07-21','Burkina Faso','Unhealthy for Sensitive Groups',118,'Africa','Ouagadougou')
cursor.execute("INSERT OR REPLACE INTO Function_Table VALUES(?,?,?,?,?,?,?)", Function_Table)
db.commit()

#Delete data(needs fixing or maybe put into separate file)
cursor.execute("DELETE FROM Function_Table WHERE AQ_Key = 1000") #change number to which key you want to delete (leave at 1000 to not delete anything)

#Select statment get data from Function_Table
cursor.execute("SELECT * FROM Function_Table")
Function_Table = cursor.fetchall()

# Loops through prints each row
for row in Function_Table:
    print(row)

cursor.execute("SELECT * FROM Status")
Status = cursor.fetchall()

# Loops through prints each row
for row in Status:
    print(row)