########True##########
Names={"Yusof","Bozorg","Danish","Nazir"}
version2={"Yusof","Bozorg","Danish",}
version3=version2.issubset(Names)
print(version3)
#######false#########
Names={"Yusof","Bozorg","Danish","Nazir"}
version2={"Soraj","samir","roman","Nazir"}
version3=version2.issubset(Names)
print(version3)