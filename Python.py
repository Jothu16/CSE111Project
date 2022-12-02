import sqlite3
import math

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

cursor.execute("DROP TABLE Current_AQ_Info")
cursor.execute("DROP TABLE Users")
cursor.execute("DROP TABLE Continent")
cursor.execute("DROP TABLE Country")
cursor.execute("DROP TABLE Capital_City")
cursor.execute("DROP TABLE History")
cursor.execute("DROP TABLE Status")
cursor.execute("DROP TABLE UserEdits")
cursor.execute("DROP TABLE HistoryStatus")
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

cursor.execute("""CREATE TABLE UserEdits(
     User_Key INTEGER,
     AQ_Key INTEGER,
     City_Key INTEGER
     )""")

cursor.execute("""CREATE TABLE HistoryStatus(
     Status_Key INTEGER,
     History_Key INTEGER,
     City_Key INTEGER
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

Status = (6, 'Maroon', 301, 999999)
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
User_AQ = (1, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (1, '2022-07-21', 14, 1)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (1, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (2, '2022-07-21', 65, 2, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (2, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (2, '2022-07-21', 65, 2)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (2, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (3, '2022-07-21', 55, 3, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (3, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (3, '2022-07-21', 55, 3)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (3, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (4, '2022-07-21', 113, 4, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (4, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (4, '2022-07-21', 113, 4)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (4, 3)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (5, '2022-07-21', 63, 5, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (5, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (5, '2022-07-21', 63, 5)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (5, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (6, '2022-07-21', 76, 6, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (6, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (6, '2022-07-21', 76, 6)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (6, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (7, '2022-07-21', 56, 7, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (7, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (7, '2022-07-21', 56, 7)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (7, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (8, '2022-07-21', 45, 8, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (8, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (8, '2022-07-21', 45, 8)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (8, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (9, '2022-07-21', 12, 9, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (9, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (9, '2022-07-21', 12, 9)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (9, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (10, '2022-07-21', 165, 10, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (10, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (10, '2022-07-21', 165, 10)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (10, 4)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (11, '2022-07-21', 141, 11, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (11, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (11, '2022-07-21', 141, 11)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (11, 3)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (12, '2022-07-21', 13, 12, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (12, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (12, '2022-07-21', 13, 12)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (12, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (13, '2022-07-21', 61, 13, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (13, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (13, '2022-07-21', 61, 13)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (13, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (14, '2022-07-21', 28, 14, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (14, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (14, '2022-07-21', 28, 14)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (14, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (15, '2022-07-21', 12, 15, 3)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (15, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (15, '2022-07-21', 12, 15)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (15, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (16, '2022-07-21', 9, 16, 1)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (16, 1)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (16, '2022-07-21', 9, 16)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (16, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (17, '2022-07-21', 58, 17, 2)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (17, 2)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (17, '2022-07-21', 58, 17)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (17, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (18, '2022-07-21', 67, 18, 3)
cursor.execute("INSERT  INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (18, 3)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (18, '2022-07-21', 67, 18)
cursor.execute("INSERT  INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (18, 2)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (19, '2022-07-21', 15, 19, 4)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (19, 4)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (19, '2022-07-21', 15, 19)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (19, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (20, '2022-07-21', 28, 20, 5)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (20, 5)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (20, '2022-07-21', 28, 20)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (20, 1)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

Current_AQ_Info = (21, '2022-07-21', 118, 21, 6)
cursor.execute("INSERT INTO Current_AQ_Info VALUES(?,?,?,?,?)", Current_AQ_Info)
User_AQ = (21, 6)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
History = (21, '2022-07-21', 118, 21)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", History)
Hist_Stat = (21, 3)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
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

#count amount of history entries and user entries
cursor.execute("""SELECT COUNT(History.History_Key) FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users""")
max_user_key = cursor.fetchone()[0]
max_hist_key = cursor.fetchone()[0]
#print(max_user_key, max_hist_key)

#count the amount of countries and their capital cities and their entries(city count = country count since country can only have 1 capital)
cursor.execute("SELECT COUNT(Capital_City.City_Key) FROM Capital_City")
max_country_key = max_city_key = max_aq_key = cursor.fetchone()[0]
#print(max_country_key, max_city_key, max_aq_key)

#get current userkey
name = ('Bronya', 'Zaychik')
cursor.execute("SELECT Users.User_Key FROM Users WHERE Users.First_Name = ? AND Users.Last_Name = ?", name)
user_key = cursor.fetchone()[0]
print(user_key)

#add new user - copy paste this and change variables to make work with other tables
max_user_key += 1
new_user = (max_user_key, 'Florin', 'Rusu')
cursor.execute("INSERT INTO Users VALUES(?,?,?)", new_user)
db.commit()

#delete user
first_name = 'Florin'
last_name = 'Rusu'
delete_user = (first_name, last_name)
cursor.execute("DELETE FROM Users WHERE Users.First_Name = ? AND Users.Last_Name = ?", delete_user)
cursor.execute("UPDATE Users SET User_Key = User_Key - 1 WHERE User_Key >= ?", [max_user_key])
db.commit()
max_user_key -= 1

#add new country
max_country_key += 1
country = 'United States'
continent = 'North America'
cursor.execute("SELECT Cont_Key FROM Continent WHERE Name = ?", [continent])
cont_key = cursor.fetchone()[0]

new_country = (max_country_key, cont_key, country)
cursor.execute("INSERT INTO Country VALUES(?,?,?)", new_country)
db.commit()

#add new city
max_city_key += 1
capital = 'Washington D.C.'
country = 'United States'
cursor.execute("SELECT Country_Key FROM Country WHERE Name = ?", [country])
country_key = cursor.fetchone()[0]

continent = 'North America'
cursor.execute("SELECT Cont_Key FROM Continent WHERE Name = ?", [continent])
cont_key = cursor.fetchone()[0]

new_city = (max_city_key, cont_key, country_key, capital)
cursor.execute("INSERT INTO Capital_City VALUES(?,?,?,?)", new_city)
db.commit()

#delete country
country = 'United States'
cursor.execute("DELETE FROM Country WHERE Country.Name = ?", [country])
cursor.execute("UPDATE Country SET Country_Key = Country_Key - 1 WHERE Country_Key >= ?", [max_country_key])
db.commit()
max_country_key -= 1

#delete city
capital = 'Washington D.C.'
cursor.execute("DELETE FROM Capital_City WHERE Capital_City.Name = ?", [capital])
cursor.execute("UPDATE Capital_City SET City_Key = City_Key - 1 WHERE City_Key >= ?", [max_city_key])
db.commit()
max_city_key -= 1

#Delete data relating to a city - copy paste this segment and change some names to make work with other tables
selected_city = 'Ouagadougou'
cursor.execute("SELECT Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = ?", [selected_city])
output = cursor.fetchone()[0]
cursor.execute("DELETE FROM Current_AQ_Info WHERE Current_AQ_Info.City_Key = ?", [output])
cursor.execute("UPDATE Current_AQ_Info SET AQ_Key = AQ_Key - 1 WHERE AQ_Key >= ?", [max_aq_key])
max_aq_key -= 1
#add compatibility with UserEdits
db.commit()

#Update file - date = new_date where date = old_date
new_date = '2022-07-22'
old_date = '2022-07-21'
dates = (new_date, old_date)
cursor.execute("UPDATE Current_AQ_Info SET Date = ? WHERE Date = ?", dates)
db.commit()

#update aqi value of a city - records user who did - check valid data later
selected_city = 'Tirana'
cursor.execute("SELECT Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = ?", [selected_city])
city_key = cursor.fetchone()[0]
print(city_key)
new_AQI_value = 69
updated_values = (new_AQI_value, user_key, city_key)
cursor.execute("UPDATE Current_AQ_Info SET AQI_Value = ?, User_Key = ? WHERE City_Key = ?", updated_values)
User_AQ = (city_key, user_key)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
db.commit()
#update history with new entry
max_hist_key += 1
new_history = (max_hist_key, new_date, new_AQI_value, city_key)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", new_history)
Hist_Stat = (max_hist_key, math.ceil(new_AQI_value / 50))
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

#add new entry to current aq database
max_aq_key += 1
city_key = 21
AQI_value = 120
date = '2022-07-22'
new_entry = (max_aq_key, date, AQI_value, city_key, user_key)
cursor.execute("INSERT INTO Current_AQ_Info VALUES (?,?,?,?,?)", new_entry)
User_AQ = (max_aq_key, user_key)
cursor.execute("INSERT INTO UserEdits VALUES(?,?)", User_AQ)
db.commit()
max_hist_key += 1
new_history = (max_hist_key, date, AQI_value, city_key)
cursor.execute("INSERT INTO History VALUES(?,?,?,?)", new_history)
Hist_Stat = (max_hist_key, math.ceil(AQI_value / 50))
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?)", Hist_Stat)
db.commit()

#Select statment get data from Current_AQ_Info
cursor.execute("SELECT * FROM Current_AQ_Info")
output = cursor.fetchall()
# Loops through prints each row
#for row in output:
     #print(row)

#count all edits made by users today form lowest to highest
cursor.execute("""SELECT Users.First_Name, Users.Last_Name, COUNT(Current_AQ_Info.User_Key) as cnt
                    FROM Current_AQ_Info
                    INNER JOIN Users ON Current_AQ_Info.User_Key = Users.User_Key
                    GROUP BY Users.First_Name, Users.Last_Name
                    ORDER BY cnt""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#print lowest and highest country's AQI Value
cursor.execute("""SELECT best_con.Name, MIN(best_aq.AQI_Value)
                    FROM Current_AQ_Info best_aq
                    INNER JOIN Capital_City best_city ON best_aq.City_Key = best_city.City_Key
                    INNER JOIN Country best_con ON best_city.Country_Key = best_con.Country_Key
                  UNION
                  SELECT worst_con.Name, MAX(worst_aq.AQI_Value)
                    FROM Current_AQ_Info worst_aq
                    INNER JOIN Capital_City worst_city ON worst_aq.City_Key = worst_city.City_Key
                    INNER JOIN Country worst_con ON worst_city.Country_Key = worst_con.Country_Key""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#print all cities with a "good" status
cursor.execute("""SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= 0
                    AND Current_AQ_Info.AQI_Value <= 50""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#print all countries with a "good" status
cursor.execute("""SELECT Country.Name FROM Current_AQ_Info, Capital_City, Country
                    WHERE Current_AQ_Info.City_Key = Capital_City.City_Key
                    AND Capital_City.Country_Key = Country.Country_Key
                    AND Capital_City.Name IN (SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                                                  INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                                                  WHERE Current_AQ_Info.AQI_Value >= 0
                                                  AND Current_AQ_Info.AQI_Value <= 50)""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#print all continents with a country with "good" status and how many
cursor.execute("""SELECT Continent.Name, COUNT(Country.Name) FROM Current_AQ_Info
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    INNER JOIN Country ON Capital_City.Country_Key = Country.Country_Key
                    INNER JOIN Continent ON Country.Cont_Key = Continent.Cont_Key
                    INNER JOIN (SELECT DISTINCT Capital_City.Name AS good_ones FROM Current_AQ_Info, Status
                                        INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                                        WHERE Current_AQ_Info.AQI_Value >= 0
                                        AND Current_AQ_Info.AQI_Value <= 50)
                         AS good_cities ON good_cities.good_ones = Capital_City.Name
                    GROUP BY Continent.Name""")
output = cursor.fetchall()
#for row in output:
    #print(row)

# Count the amount of entries for each status description
cursor.execute("""SELECT Status.Description, COUNT(Status.Description)
                    FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Capital_City.City_Key = Current_AQ_Info.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
                    AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
                    GROUP BY Status.Description
                    ORDER BY COUNT(Status.Description) DESC""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#Print the history of a city
selected_city = 'Tirana'
cursor.execute("""SELECT * FROM History WHERE History.City_key = (SELECT Capital_City.City_Key FROM Capital_City
                                                                      WHERE Capital_City.Name = ?)""", [selected_city])
output = cursor.fetchall()
#for row in output:
    #print(row)

#print average air quality and the average status of each continent
cursor.execute("""SELECT Continent.Name, Status.Description, AVG(Current_AQ_Info.AQI_Value) 
                    FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    INNER JOIN Country ON Capital_City.Country_Key = Country.Country_Key
                    INNER JOIN Continent ON Country.Cont_Key = Continent.Cont_Key
                    WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
                    AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
                    GROUP BY Continent.Name""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#count the amount of times each city had a certain status
selected_city = 'Tirana'
cursor.execute("""SELECT Capital_City.Name, Status.Description, COUNT(Status.Description)
                    FROM History, Status
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE History.AQI_Value >= Status.Threshold_Lower
                    AND History.AQI_Value <= Status.Threshold_Upper
                    GROUP BY Capital_City.Name, Status.Description
                    ORDER BY Capital_City.Name, Status.Threshold_Lower""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed
cursor.execute("""SELECT DISTINCT Capital_City.Name FROM History, Status
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE History.AQI_Value >= 0
                    AND History.AQI_Value <= 50
                  INTERSECT
                  SELECT DISTINCT Capital_City.Name FROM History, Status
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE History.AQI_Value >= 51
                    AND History.AQI_Value <= 100""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#find all cities except for unhealthy or worse cities
cursor.execute("""SELECT Capital_City.Name FROM Current_AQ_Info
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                  EXCEPT
                  SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= 101""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#print all cities that had changes in statuses and order by date
cursor.execute("""SELECT History.Date, Capital_City.Name, Status.Description
                    FROM History, Status, Capital_City, (SELECT Capital_City.Name as cities
                                             FROM History, Status
                                             INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                                             WHERE History.AQI_Value >= Status.Threshold_Lower
                                             AND History.AQI_Value <= Status.Threshold_Upper
                                             GROUP BY Capital_City.Name
                                             HAVING COUNT(DISTINCT Status.Description) > 1
                                             ORDER BY Capital_City.Name, Status.Threshold_Lower) AS cities_with_change
                    WHERE History.AQI_Value >= Status.Threshold_Lower
                    AND History.AQI_Value <= Status.Threshold_Upper
                    AND History.City_Key = Capital_City.City_Key
                    AND Capital_City.Name = cities_with_change.cities""")
output = cursor.fetchall()
#for row in output:
    #print(row)

# select all countries status
cursor.execute("""SELECT Country.Name, Status.Description FROM Current_AQ_Info, Status, Capital_City, Country
                    WHERE Current_AQ_Info.AQI_Value >= Status.Threshold_Lower
                    AND Current_AQ_Info.AQI_Value <= Status.Threshold_Upper
                    AND Current_AQ_Info.City_Key = Capital_City.City_Key
                    AND Capital_City.Country_Key = Country.Country_Key""")
output = cursor.fetchall()
#for row in output:
    #print(row)