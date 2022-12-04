import sqlite3
import math

db = sqlite3.connect("newdb.sqlite")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS Current_AQ_Info")
cursor.execute("DROP TABLE IF EXISTS Users")
cursor.execute("DROP TABLE IF EXISTS Continent")
cursor.execute("DROP TABLE IF EXISTS Country")
cursor.execute("DROP TABLE IF EXISTS Capital_City")
cursor.execute("DROP TABLE IF EXISTS History")
cursor.execute("DROP TABLE IF EXISTS Status")
cursor.execute("DROP TABLE IF EXISTS UserEdits")
cursor.execute("DROP TABLE IF EXISTS HistoryStatus")
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
     City_Key INTEGER
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

cursor.execute("""CREATE TABLE UserEdits(
     AQ_Key INTEGER,
     User_Key INTEGER,
     City_Key INTEGER,
     Date TEXT
     )""")

cursor.execute("""CREATE TABLE HistoryStatus(
     History_Key INTEGER,
     Status_Key INTEGER,
     City_Key INTEGER
     )""")

#Populate Status Table
Status = ('Good', 0, 50)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

Status = ('Moderate', 51, 100)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

Status = ('Unhealthy for Sensitive Groups', 101, 150)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

Status = ('Unhealthy', 151, 200)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

Status = ('Very Unhealthy', 201, 300)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

Status = ('Maroon', 301, 999999)
cursor.execute("INSERT INTO Status(Description, Threshold_Lower, Threshold_Upper) VALUES(?,?,?)", Status)
db.commit()

#Populate User Table
User = ('Eric','Li')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

User = ('Harjot','Grewal')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

User = ('Chieh','Lin')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

User = ('Kiana','Kaslana')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

User = ('Mei','Raiden')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

User = ('Bronya','Zaychik')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", User)
db.commit()

#Populate Country Table
Country = (1,'Albania')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (2,'Algeria')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Andorra')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (2,'Angola')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (3,'Argentina')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (4,'Armenia')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (5,'Australia')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Austria')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (4,'Azerbaijan')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (4,'Bahrain')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (4,'Bangladesh')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Belarus')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Belgium')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (6,'Belize')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (6,'Bermuda')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (3,'Bolivia')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Bosnia and Herzgovinia')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (3,'Brazil')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (4,'Brunei')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (1,'Bulgaria')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

Country = (2,'Burkina Faso')
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", Country)
db.commit()

#Populate Continent Table
#Continent = 'Europe'
cursor.execute("INSERT INTO Continent(Name) VALUES('Europe')")
db.commit()

#Continent = 'Africa'
cursor.execute("INSERT INTO Continent(Name) VALUES('Africa')")
db.commit()

#Continent = 'South America'
cursor.execute("INSERT INTO Continent(Name) VALUES('South America')")
db.commit()

#Continent = 'Asia'
cursor.execute("INSERT INTO Continent(Name) VALUES('Asia')")
db.commit()

#Continent = 'Oceania'
cursor.execute("INSERT INTO Continent(Name) VALUES('Oceania')")
db.commit()

#Continent = 'North America'
cursor.execute("INSERT INTO Continent(Name) VALUES('North America')")
db.commit()

#Populate Capitol Table
Capital_City = (1,'Tirana')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (2,'Algiers')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (3,'Andorra la Vella')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (4,'Luanda')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (5,'Buenos Aires')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (6,'Yerevan')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (7,'Canberra')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (8,'Vienna')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (9,'Baku')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (10,'Manama')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (11,'Dhaka')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (12,'Minsk')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (13,'Burssels')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (14,'Belomopan')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (15,'Hamilton')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (16,'Sucre')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (17,'Sarajevo')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (18,'Brasilia')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (19,'Branda Seri Begawan')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (20,'Sofia')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

Capital_City = (21,'Ouagadougou')
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", Capital_City)
db.commit()

# Add Current_AQ_Info and History to the table and commit these changes to the database
Current_AQ_Info = ('2022-07-21', 14, 1)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (1, 1, 1, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 14, 1)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (1, 1, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 65, 2)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (2, 2, 2, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 65, 2)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (2, 2, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 55, 3)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (3, 3, 3, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 55, 3)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (3, 2, 3)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 113, 4)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (4, 1, 4, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 113, 4)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (4, 3, 4)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 63, 5)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (5, 2, 5, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 63, 5)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (5, 2, 5)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 76, 6)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (6, 3, 6, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 76, 6)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (6, 2, 6)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 56, 7)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (7, 1, 7, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 56, 7)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (7, 2, 7)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 45, 8)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (8, 2, 8, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 45, 8)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (8, 1, 8)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 12, 9)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (9, 3, 9, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 12, 9)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (9, 1, 9)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 165, 10)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (10, 1, 10, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 165, 10)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (10, 4, 10)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 141, 11)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (11, 2, 11, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 141, 11)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (11, 3, 11)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 13, 12)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (12, 3, 12, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 13, 12)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (12, 1, 12)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 61, 13)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (13, 1, 13, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 61, 13)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (13, 2, 13)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 28, 14)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (14, 2, 14, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 28, 14)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (14, 1, 14)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 12, 15)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (15, 3, 15, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 12, 15)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (15, 1, 15)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 9, 16)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (16, 1, 16, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 9, 16)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (16, 1, 16)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 58, 17)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (17, 2, 17, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 58, 17)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (17, 2, 17)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 67, 18)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (18, 3, 18, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 67, 18)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (18, 2, 18)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 15, 19)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (19, 4, 19, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 15, 19)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (19, 1, 19)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 28, 20)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (20, 5, 20, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 28, 20)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (20, 1, 20)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = ('2022-07-21', 118, 21)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", Current_AQ_Info)
User_AQ = (21, 6, 21, '2022-07-21')
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
History = ('2022-07-21', 118, 21)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", History)
Hist_Stat = (21, 3, 21)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()


#Check implementation in assignments for many to many
#Need Intermediate table (such as partsupp)
#Table where city with different statuses
#history sohuld have primary key
#each histroy should correspond to city and/or status key
#Many to many will always have 2 foreign keys
#Need to have table connecting history and status 

#standalone table connecting histoy and status with history key and status key
# city 1, history key 1, status key 1
# city 2, history key 2, status key 1
# city 1, history key 3, status key 2
# ement count: 20