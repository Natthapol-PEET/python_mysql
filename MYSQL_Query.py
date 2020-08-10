import mysql.connector

# mydb = mysql.connector.connect(
#   host="35.247.164.240",
#   user="peet",
#   passwd="10042541",
#   database="testdb"
# )

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="peet",
  passwd="",
  database="testdb"
)

mycursor = mydb.cursor()

# Create table users
# sql = "CREATE TABLE users (\
#     id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
#     member_id CHAR(60) NOT NULL,\
#     status ENUM('1', '2', '3') NOT NULL,\
#     username VARCHAR(255) NOT NULL,\
#     PRIMARY KEY (id)\
# )"

# mycursor.execute(sql)

# -----------------------------------------------------------------------------
# Insert data to table users
# sql = "INSERT INTO users VALUES (NULL, %s, %s, %s);"
# val = ('b6040202424', '1', 'NATTHAPOL NONTHASRI')
# mycursor.execute(sql, val)
# mydb.commit()

# sql = "INSERT INTO users VALUES (NULL, %s, %s, %s);"
# val = ('a123456789', '2', 'PEET')
# mycursor.execute(sql, val)
# mydb.commit()

# sql = "INSERT INTO users VALUES (NULL, %s, %s, %s);"
# val = ('9999', '3', 'SOM')
# mycursor.execute(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# -----------------------------------------------------------------------------
# Create table bin
# sql = "CREATE TABLE bin (\
#     id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
#     img_name CHAR(60) NOT NULL,\
#     type ENUM('01', '02', '03', '04') NOT NULL,\
#     bin SMALLINT UNSIGNED NOT NULL,\
#     member_id CHAR(60) NOT NULL REFERENCES users(member_id),\
#     PRIMARY KEY (id)\
# );"

# mycursor.execute(sql)

# -----------------------------------------------------------------------------
# Insert data to table bin
# sql = "INSERT INTO bin VALUES (NULL, %s, %s, %s, %s);"
# val = ('PEET.png', '01', 1, 'b6040202424')
# mycursor.execute(sql, val)
# mydb.commit()

# sql = "INSERT INTO bin VALUES (NULL, %s, %s, %s, %s);"
# val = ('SOM.png', '02', 2, 'a123456789')
# mycursor.execute(sql, val)
# mydb.commit()

# -----------------------------------------------------------------------------
# Query data
# mycursor.execute("select * from bin;")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT b.*, u.username, u.status FROM users u INNER JOIN bin b \
#    ON b.member_id = u.member_id;"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)