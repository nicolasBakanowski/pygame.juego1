import sqlite3

conect = sqlite3.connect ("BASE2.db")
cur = conect.cursor( )
cur.execute("SELECT * FROM JUGADOR ORDER BY puntaje DESC")
tupla = cur.fetchall()
print(tupla)
conect.commit()
conect.close()