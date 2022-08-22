#Indexage
# nom[start:stop:step]

nom = "Quentin Saenz"

zone1 = nom[:7]
zone2 = nom[8:]
zone3 = nom[::2]
zone4 = nom[::-1]

print(zone4)

#Slice
#slice(start:stop:step)

site1 = "https://www.matias.ma/nsfw/"
site2 = "https://www.google.fr/"

#slice = slice(8,-9)
slice = slice(8, -1)
print(site1[slice])
print(site2[slice])
