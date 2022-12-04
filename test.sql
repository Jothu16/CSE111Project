SELECT COUNT(History.History_Key) as total FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users