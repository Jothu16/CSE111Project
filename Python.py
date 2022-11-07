import sqlite3

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

cursor.execute("DROP TABLE Current_AQ_Info")
cursor.execute("DROP TABLE Users")
cursor.execute("DROP TABLE Continent")
cursor.execute("DROP TABLE Country")
cursor.execute("DROP TABLE Capital_City")
cursor.execute("DROP TABLE History")
cursor.execute("DROP TABLE Status")
db.commit()

#cursor.execute("""CREATE TABLE Current_AQ_Info(
    #AQ_Key INTEGER PRIMARY KEY,
    #Date TEXT,
    #Country TEXT,
    #Status TEXT,
    #AQI_Value TEXT,
    #Continent TEXT,
    #Capital City TEXT
    #)""")

cursor.execute("""CREATE TABLE Current_AQ_Info(
     AQ_Key INTEGER PRIMARY KEY,
     Date TEXT,
     AQI_Value INTEGER,
     City_Key INTEGER,
     User_Key INTEGER
     )""")

cursor.execute("""CREATE TABLE Users(
     User_Key INTEGER PRIMARY KEY,
     First_Name TEXT,
     Last_Name TEXT
     )""")

cursor.execute("""CREATE TABLE Continent(
     Cont_Key INTEGER PRIMARY KEY,
     Name TEXT
     )""")

cursor.execute("""CREATE TABLE Country(
     Country_Key INTEGER PRIMARY KEY,
     Cont_Key Integer,
     Name TEXT
     )""")

cursor.execute("""CREATE TABLE Capital_City(
     City_Key INTEGER PRIMARY KEY,
     Cont_Key Integer,
     Country_Key Integer, 
     Name TEXT
     )""")

#cursor.execute("""CREATE TABLE History(
    #History_Key INTEGER PRIMARY KEY,
    #Date TEXT,
    #Country TEXT,
    #Status TEXT,
    #AQI_Value TEXT,
    #Continent TEXT,
    #Capital City TEXT
    #)""")
cursor.execute("""CREATE TABLE History(
    History_Key INTEGER PRIMARY KEY,
    Date TEXT,
    AQI_Value INTEGER,
    City_Key INTEGER
    )""")

cursor.execute("""CREATE TABLE Status(
     Status_Key INTEGER PRIMARY KEY,
     Description TEXT,
     Threshold_Lower INTEGER,
     Threshold_Upper INTEGER
     )""")

#Populate Status Table
Status = (1, 'Good', 0, 50)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (2, 'Moderate', 51, 100)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (3, 'Unhealthy for Sensitive Groups', 101, 150)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (4, 'Unhealthy', 151, 200)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (5, 'Very Unhealthy', 201, 300)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

Status = (6, 'Very Unhealthy', 301, 999999)
cursor.execute("INSERT INTO Status VALUES(?,?,?,?)", Status)
db.commit()

#Populate User Table
User = (1,'Eric','Li')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

User = (2,'Harjot','Grewal')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

User = (3,'Chieh','Lin')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

User = (4,'Kiana','Kaslana')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

User = (5,'Mei','Raiden')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

User = (6,'Bronya','Zaychik')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", User)
db.commit()

#Populate Country Table
Country = (1, 1,'Albania')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (2, 2,'Algeria')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (3, 1,'Andorra')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (4, 2,'Angola')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (5, 3,'Argentina')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (6, 4,'Armenia')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (7, 5,'Australia')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (8, 1,'Austria')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (9, 4,'Azerbaijan')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (10, 4,'Bahrain')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (11, 4,'Bangladesh')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (12, 1,'Belarus')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (13, 1,'Belgium')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (14, 6,'Belize')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (15, 6,'Bermuda')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (16, 3,'Bolivia')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (17, 1,'Bosnia and Herzgovinia')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (18, 3,'Brazil')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (19, 4,'Brunei')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (20, 1,'Bulgaria')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

Country = (21, 2,'Burkina Faso')
cursor.execute("INSERT INTO Country VALUES(?,?,?)", Country)
db.commit()

#Populate Continent Table
Continent = (1,'Europe')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

Continent = (2,'Africa')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

Continent = (3,'South America')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

Continent = (4,'Asia')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

Continent = (5,'Oceania')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

Continent = (6,'North America')
cursor.execute("INSERT INTO Continent VALUES(?,?)", Continent)
db.commit()

#Populate Capitol Table
Capital_City = (1, 1, 1,'Tirana')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (2, 2, 2,'Algiers')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (3, 1, 3,'Andorra la Vella')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (4, 2, 4,'Luanda')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (5, 3, 5,'Buenos Aires')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (6, 4, 6,'Yerevan')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (7, 5, 7,'Canberra')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (8, 1, 8,'Vienna')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (9, 4, 9,'Baku')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (10, 4, 10,'Manama')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (11, 4, 11,'Dhaka')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (12, 1, 12,'Minsk')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (13, 1, 13,'Burssels')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (14, 6, 14,'Belomopan')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (15, 6, 15,'Hamilton')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (16, 3, 16,'Sucre')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (17, 1, 17,'Sarajevo')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (18, 3, 18,'Brasilia')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (19, 4, 19,'Branda Seri Begawan')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (20, 1, 20,'Sofia')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()

Capital_City = (21, 2, 21,'Ouagadougou')
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", Capital_City)
db.commit()


# Add Current_AQ_Info and History to the table and commit these changes to the database
Current_AQ_Info = (1, '2022-07-21', 14, 1, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (1, '2022-07-21', 14, 1)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (2, '2022-07-21', 65, 2, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (2, '2022-07-21', 65, 2)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (3, '2022-07-21', 55, 3, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (3, '2022-07-21', 55, 3)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (4, '2022-07-21', 113, 4, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (4, '2022-07-21', 113, 4)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (5, '2022-07-21', 63, 5, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (5, '2022-07-21', 63, 5)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (6, '2022-07-21', 76, 6, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (6, '2022-07-21', 76, 6)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (7, '2022-07-21', 56, 7, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (7, '2022-07-21', 56, 7)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (8, '2022-07-21', 45, 8, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (8, '2022-07-21', 45, 8)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (9, '2022-07-21', 12, 9, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (9, '2022-07-21', 12, 9)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (10, '2022-07-21', 165, 10, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (10, '2022-07-21', 165, 10)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (11, '2022-07-21', 141, 11, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (11, '2022-07-21', 141, 11)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (12, '2022-07-21', 13, 12, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (12, '2022-07-21', 13, 12)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (13, '2022-07-21', 61, 13, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (13, '2022-07-21', 61, 13)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (14, '2022-07-21', 28, 14, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (14, '2022-07-21', 28, 14)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (15, '2022-07-21', 12, 15, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (15, '2022-07-21', 12, 15)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (16, '2022-07-21', 9, 16, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (16, '2022-07-21', 9, 16)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (17, '2022-07-21', 58, 17, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (17, '2022-07-21', 58, 17)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (18, '2022-07-21', 67, 18, 3)
cursor.execute("INSERT  INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (18, '2022-07-21', 67, 18)
cursor.execute("INSERT  INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (19, '2022-07-21', 15, 19, 4)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (19, '2022-07-21', 15, 19)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (20, '2022-07-21', 28, 20, 5)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (20, '2022-07-21', 28, 20)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

Current_AQ_Info = (21, '2022-07-21', 118, 21, 6)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
History = (21, '2022-07-21', 118, 21)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
db.commit()

#Delete data(needs fixing or maybe put into separate file)
cursor.execute("DELETE FROM Current_AQ_Info WHERE AQ_Key = 1000") #change number to which key you want to delete (leave at 1000 to not delete anything)

#Update file
cursor.execute("UPDATE Current_AQ_Info SET Date = '2022-07-22' WHERE Date = '2022-07-21'")
db.commit()

#Select statment get data from Current_AQ_Info
cursor.execute("SELECT * FROM Current_AQ_Info")
output = cursor.fetchall()

# Loops through prints each row
for row in output:
    print(row)

#cursor.execute("SELECT * FROM Status")
#Status = cursor.fetchall()

# Loops through prints each row
#for row in Status:
    #print(row)

cursor.execute("""SELECT Country.Name, Status.Description FROM Current_AQ_Info, Status, Capital_City, Country
                    WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
                    AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
                    AND Current_AQ_Info.City_Key = Capital_City.City_Key
                    AND Capital_City.Country_Key = Country.Country_Key""")
output = cursor.fetchall()
for row in output:
    print(row)
