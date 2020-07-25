import sqlite3

insertionSQLstring = """
INSERT INTO menu (num, title, category, description, price, calories)
  VALUES (?, ?, ?, ?, ?, ?)
"""

dumpling_desc = "Steamed pork dumplings with Szechwan dipping sauce."
soup_desc = "Caramelized onions simmered in au jus topped with a crouton and melted Swiss."
cheeseburger_desc = "White cheddar, lettuce, tomatoes, red onions and pickles."

lots_of_new_foods = [
  (21, "Steamed Dumplings", "entree", dumpling_desc, 11.95, 590),
  (22, "French Onion Soup", "entree", soup_desc, 9.95, 590),
  (23, "Cheeseburger", "burger", cheeseburger_desc, 10.00, 820)
]

try:
  db = sqlite3.connect('restaurant.db')
  cursor = db.cursor()
  
  #bulk execute INSERT query:
  cursor.executemany(insertionSQLstring, lots_of_new_foods)
  db.commit()
  print("Database changes made. Open in DB Browser for SQLite to see changes.") 
  
except Exception as error_msg:
  db.rollback()
  print("An error occured:", error_msg)
  
finally:
  db.close()