########True##########
Names={"Yusof","Bozorg","Danish","Nazir"}
version2={"Yusof","Bozorg","Danish",}
version3=Names.issuperset(version2)
print(version3)
#######false#########
Names={"Yusof","Bozorg","Danish","Nazir"}
version2={"Soraj","samir","roman","Nazir"}
version3=Names.issuperset(version2)
print(version3)