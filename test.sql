SELECT COUNT(History.History_Key) as total FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users;

                  SELECT Users.First_Name, Users.Last_Name, COUNT(UserEdits.User_Key) as cnt
                    FROM Users
                    INNER JOIN UserEdits ON UserEdits.User_Key = Users.User_Key
                    GROUP BY Users.First_Name, Users.Last_Name
                    ORDER BY cnt;

SELECT Cont_Key FROM Continent WHERE Name = 'North America';
INSERT INTO Country(Cont_Key, Name) VALUES('6','United States');

select City_Key FROM Capital_City WHERE Capital_City.Name = 'Tirana';

SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= 0
                    AND Current_AQ_Info.AQI_Value <= 50;

                    SELECT DISTINCT Capital_City.Name FROM Current_AQ_Info, Status
                    INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                    WHERE Current_AQ_Info.AQI_Value >= 51
                    AND Current_AQ_Info.AQI_Value <= 100;


SELECT User_Key FROM Users WHERE User_Key = 10;