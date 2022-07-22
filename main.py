Cities_new = open("Cities_new.txt", "r", encoding="ANSI")
Streets_new = open("Streets_new.txt", "r", encoding="ANSI")
Zipcodes_new = open("Zipcodes_new.txt", "r", encoding="ANSI")
x = open("all.txt", "w", encoding="utf8")
city = ""
streets=""
mikud=""
numhouse=""

# {"city","street","numhouse","mikud"
y = Cities_new.read()
d = Streets_new.read()
b = Zipcodes_new.read()
y = y.split("\n")
d = d.split("\n")
b = b.split("\n")
for d1 in range(len(b)):
    numhouse=b[d1].split(",")[3]
    mikud=b[d1].split(",")[6]
    for i in range(len(y)):
        if y[i].split(",")[0] in b[d1].split(",")[0]:
            city = y[i].split(",")[2].replace('"', "")

    try:
        for j in range(len(d)):
            if d[j].split(",")[2] in b[d1].split(",")[2]:
                streets=d[j].split(",")[4].replace('"', "")
    except:
          pass
    print(city+","+streets+","+numhouse+","+mikud)
    x.write(city+","+streets+","+numhouse+","+mikud+"\n")
