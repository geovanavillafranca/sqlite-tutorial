import sqlite3
import sys


def printDB():

    try:
        result = theCursor.execute("SELECT ID, FName,LName, Age,"
                                   "Address, Salary, HireDate FROM Employees")

        for row in result:
            print("ID: ", row[0])
            print("FName: ", row[1])
            print("LName: ", row[2])
            print("Age: ", row[3])
            print("Address: ", row[4])
            print("Salary: ", row[5])
            print("HireDate: ", row[6])

    except sqlite3.OperationalError:
        print("Table doesn't exist")

    except:
        print("Couldn't retrieve Data from Database")


db_conn = sqlite3.connect('test.db')

print('Banco criado')

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE IF NOT EXISTS Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                    "FName TEXT NOT NULL, LName TEXT NOT NULL,"
                    "Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    db_conn.commit()
except sqlite3.OperationalError:
    print("Table couldn't be created")

print('Table created')

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                " VALUES ('Derek', 'Banas', 41, '123 Main St', 50000, date('now')) ")

db_conn.commit()

printDB()

try:
    db_conn.execute("UPDATE Employees SET Address = '121 Main St' WHERE ID=1")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be Updated")

printDB()

'''
try:
    db_conn.execute("DELETE FROM Employees WHERE ID=1")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be Deleted")


printDB()

db_conn.rollback()
'''

try:
    db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOG DEFAULT NULL")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't Add column")


theCursor.execute("PRAGMA TABLE_INFO(Employees)")
rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rowNames)

theCursor.execute("SELECT COUNT(*) FROM Employees")

num0fRows = theCursor.fetchall()

print("Total Rows: ", num0fRows[0][0])

theCursor.execute("SELECT SQLITE_VERSION()")

print("SQLite Version: ", theCursor.fetchone())

with db_conn:
    db_conn.row_factory = sqlite3.Row

    theCursor = db_conn.cursor()

    theCursor.execute("SELECT * FROM Employees")

    rows = theCursor.fetchall()

    for row in rows:
        print(f'{row["FName"]} {row["LName"]}')

with open('dump.sql', 'w') as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)



db_conn.close()

print('Banco fechado')


