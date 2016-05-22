import sqlite3
from urllib import request
import re

coon = sqlite3.connect('emaildb.sqlite')
cur = coon.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

data = request.urlopen('http://www.pythonlearn.com/code/mbox.txt')
for line in data:
    if not line.startswith(b'From:'): continue
    line = line.decode('utf-8')
    org = re.findall('@(.+)', line)[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    try:
        row = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    except:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))

coon.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print()
print("Counts:")
for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])

cur.close()
