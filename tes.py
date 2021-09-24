import mysql.connector, geocoder

g = geocoder.ipinfo('me')
lat = g.lat
lng = g.lng

mydb = mysql.connector.connect(
  host="host",
  user="user",
  password="password",
  database="your_db"
)

cursor = mydb.cursor()

sql = "SELECT name, distance as jarak_km FROM ( SELECT * ,(((acos(sin(( %s * pi() / 180)) * sin(( `latitude` * pi() / 180)) + cos(( %s * pi() /180 )) * cos(( `latitude` * pi() / 180)) * cos((( %s - `longitude`) * pi()/180)))) * 180/pi()) * 60 * 1.1515 * 1.609344) as distance FROM hospital_list) myTable WHERE distance <= 150 LIMIT 25;"

cursor.execute(sql,(lat,lat,lng))

myresult = cursor.fetchall()

for x in myresult:
  print(x)
