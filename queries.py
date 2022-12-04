import sqlite3
import math

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

#count amount of history entries and user entries
cursor.execute("""SELECT COUNT(History.History_Key) FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users""")
#max_user_key = cursor.fetchone()[0]
#max_hist_key = cursor.fetchone()[0]
#print(max_user_key, max_hist_key)

#count the amount of countries and their capital cities and their entries(city count = country count since country can only have 1 capital)
cursor.execute("SELECT COUNT(Capital_City.City_Key) FROM Capital_City")
#max_country_key = max_city_key = max_aq_key = cursor.fetchone()[0]
#print(max_country_key, max_city_key, max_aq_key)

#get current userkey
name = ('Bronya', 'Zaychik')
cursor.execute("SELECT Users.User_Key FROM Users WHERE Users.First_Name = ? AND Users.Last_Name = ?", name)
user_key = cursor.fetchone()[0]
#print(user_key)

#add new user - copy paste this and change variables to make work with other tables
#max_user_key += 1
new_user = ('Florin', 'Rusu')
cursor.execute("INSERT INTO Users(First_Name, Last_Name) VALUES(?,?)", new_user)
db.commit()

#delete user
first_name = 'Florin'
last_name = 'Rusu'
delete_user = (first_name, last_name)
cursor.execute("DELETE FROM Users WHERE Users.First_Name = ? AND Users.Last_Name = ?", delete_user)
#cursor.execute("UPDATE Users SET User_Key = User_Key - 1 WHERE User_Key >= ?", [max_user_key])
db.commit()
#max_user_key -= 1

#add new country
#max_country_key += 1
country = 'United States'
continent = 'North America'
cursor.execute("SELECT Cont_Key FROM Continent WHERE Name = ?", [continent])
cont_key = cursor.fetchone()[0]

new_country = (cont_key, country)
cursor.execute("INSERT INTO Country(Cont_Key, Name) VALUES(?,?)", new_country)
db.commit()

#add new city
#max_city_key += 1
capital = 'Washington D.C.'
country = 'United States'
cursor.execute("SELECT Country_Key FROM Country WHERE Name = ?", [country])
country_key = cursor.fetchone()[0]

continent = 'North America'
cursor.execute("SELECT Cont_Key FROM Continent WHERE Name = ?", [continent])
cont_key = cursor.fetchone()[0]

new_city = (country_key, capital)
cursor.execute("INSERT INTO Capital_City(Country_Key, Name) VALUES(?,?)", new_city)
db.commit()

#delete country
country = 'United States'
cursor.execute("DELETE FROM Country WHERE Country.Name = ?", [country])
#cursor.execute("UPDATE Country SET Country_Key = Country_Key - 1 WHERE Country_Key >= ?", [max_country_key])
db.commit()
#max_country_key -= 1

#delete city
capital = 'Washington D.C.'
cursor.execute("DELETE FROM Capital_City WHERE Capital_City.Name = ?", [capital])
##cursor.execute("UPDATE Capital_City SET City_Key = City_Key - 1 WHERE City_Key >= ?", [max_city_key])
db.commit()
#max_city_key -= 1

#Delete data relating to a city - copy paste this segment and change some names to make work with other tables
selected_city = 'Ouagadougou'
cursor.execute("SELECT Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = ?", [selected_city])
output = cursor.fetchone()[0]
cursor.execute("DELETE FROM Current_AQ_Info WHERE Current_AQ_Info.City_Key = ?", [output])
#cursor.execute("UPDATE Current_AQ_Info SET AQ_Key = AQ_Key - 1 WHERE AQ_Key >= ?", [max_aq_key])
#max_aq_key -= 1
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
date = '2022-07-22'
cursor.execute("SELECT Capital_City.City_Key FROM Capital_City WHERE Capital_City.Name = ?", [selected_city])
city_key = cursor.fetchone()[0]
#print(city_key)
new_AQI_value = 69
updated_values = (date, new_AQI_value, city_key)
cursor.execute("UPDATE Current_AQ_Info SET Date = ?, AQI_Value = ? WHERE City_Key = ?", updated_values)
User_AQ = (city_key, user_key, city_key, date)
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
db.commit()
#update history with new entry
#max_hist_key += 1
new_history = (new_date, new_AQI_value, city_key)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", new_history)
cursor.execute("SELECT MAX(History_Key) FROM History")
hist_key = cursor.fetchone()[0]
Hist_Stat = (hist_key, math.ceil(new_AQI_value / 50), city_key)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

#add new entry to current aq database
#max_aq_key += 1
city_key = 21
AQI_value = 120
date = '2022-07-22'
new_entry = (date, AQI_value, city_key)
cursor.execute("INSERT INTO Current_AQ_Info(Date, AQI_Value, City_Key) VALUES(?,?,?)", new_entry)
cursor.execute("SELECT MAX(AQ_Key) FROM Current_AQ_Info")
aq_key = cursor.fetchone()[0]
User_AQ = (aq_key, user_key, city_key, date)
cursor.execute("INSERT INTO UserEdits VALUES(?,?,?,?)", User_AQ)
db.commit()
#max_hist_key += 1
new_history = (date, AQI_value, city_key)
cursor.execute("INSERT INTO History(Date, AQI_Value, City_Key) VALUES(?,?,?)", new_history)
cursor.execute("SELECT MAX(History_Key) FROM History")
hist_key = cursor.fetchone()[0]
Hist_Stat = (hist_key, math.ceil(AQI_value / 50), city_key)
cursor.execute("INSERT INTO HistoryStatus VALUES(?,?,?)", Hist_Stat)
db.commit()

#Select statment get data from Current_AQ_Info
cursor.execute("SELECT * FROM Current_AQ_Info")
output = cursor.fetchall()
# Loops through prints each row
#for row in output:
     #print(row)

#count all edits made by users form lowest to highest
cursor.execute("""SELECT Users.First_Name, Users.Last_Name, COUNT(UserEdits.User_Key) as cnt
                    FROM Users
                    INNER JOIN UserEdits ON UserEdits.User_Key = Users.User_Key
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
                    FROM History, HistoryStatus, Status
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE History.History_Key = HistoryStatus.History_Key
                    AND Status.Status_Key = HistoryStatus.Status_Key
                    GROUP BY Capital_City.Name, Status.Description
                    ORDER BY Capital_City.Name, Status.Threshold_Lower""")
output = cursor.fetchall()
#for row in output:
    #print(row)

#find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed
cursor.execute("""SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE HistoryStatus.Status_Key = 1
                    AND History.History_Key = HistoryStatus.History_Key
                  INTERSECT
                  SELECT DISTINCT Capital_City.Name FROM History, HistoryStatus
                    INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                    WHERE HistoryStatus.Status_Key = 2
                    AND History.History_Key = HistoryStatus.History_Key""")
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
                    FROM History, HistoryStatus, Status, Capital_City, (SELECT Capital_City.Name as cities
                                             FROM History, Status, HistoryStatus
                                             INNER JOIN Capital_City ON History.City_Key = Capital_City.City_Key
                                             WHERE History.History_Key = HistoryStatus.History_Key
                                             AND Status.Status_Key = HistoryStatus.Status_Key
                                             GROUP BY Capital_City.Name
                                             HAVING COUNT(DISTINCT Status.Description) > 1
                                             ORDER BY Capital_City.Name, Status.Threshold_Lower) AS cities_with_change
                    WHERE History.History_Key = HistoryStatus.History_Key
                    AND HistoryStatus.Status_Key = Status.Status_Key
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