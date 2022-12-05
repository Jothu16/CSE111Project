SELECT COUNT(History.History_Key) as total FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users;

                  SELECT Users.First_Name, Users.Last_Name, COUNT(UserEdits.User_Key) as cnt
                    FROM Users
                    INNER JOIN UserEdits ON UserEdits.User_Key = Users.User_Key
                    GROUP BY Users.First_Name, Users.Last_Name
                    ORDER BY cnt