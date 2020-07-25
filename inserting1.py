import sqlite3

insertionSQLstring = """
INSERT INTO menu (num, title, category, description, price, calories)
  VALUES (?, ?, ?, ?, ?, ?)
"""

try:
  db = sqlite3.connect('restaurant.db')
  cursor = db.cursor()
  cursor.execute("SELECT num + 1 FROM menu ORDER BY num DESC LIMIT 1") #next available number

  #set up parameters for INSERT:
  num = cursor.fetchone()[0]
  title = input("Title: ")
  category = input("Category: ")
  description = input("Discription: ")
  price = float(input("Price ($): "))
  calories = int(input("Calories: "))

  #execute INSERT query, and write changes to disk:
  cursor.execute(insertionSQLstring,(num, title, category, description, price, calories))
  db.commit()
  print("Database changes made. Open in DB Browser for SQLite to see changes.") 
  
except Exception as error_msg:
  #rollback important for database integrity, incase erroneous data was saved:
  db.rollback()
  print("An error occured:", error_msg)
  
finally:
  db.close()
