import sqlite3

db = sqlite3.connect("newdb.db")
cursor = db.cursor()

cursor.execute("""SELECT COUNT(History.History_Key) FROM History 
                  UNION 
                  SELECT COUNT(Users.User_Key) FROM Users""")
max_user_key = cursor.fetchone()[0]
max_hist_key = cursor.fetchone()[0]
print(max_user_key, max_hist_key)