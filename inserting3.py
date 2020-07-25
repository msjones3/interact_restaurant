import sqlite3

insertionSQLstring = """
INSERT OR REPLACE INTO menu (num, title, category, description, price, calories)
  VALUES (3, "Buffalo Burger", "burger", "Out of stock", -1.00, 920)
"""

try:
  db = sqlite3.connect('restaurant.db')
  cursor = db.cursor()
  cursor.execute(insertionSQLstring)
  db.commit()
  print("Database changes made. Open in DB Browser for SQLite to see changes.") 
  
except Exception as error_msg:
  db.rollback()
  print("An error occured:", error_msg)
  
finally:
  db.close()
