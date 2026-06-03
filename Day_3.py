vijay=["Gilli","Master","Pokiri","Shajahan","Leo","Sarkar","Jilla","Badhiri","Nanban","Kushi"]
suriya=["Karuppu","Kaka kaka","Friends","Vel","Anjaan","Ayan","Ghajini","Singham","Mass","Jai Bhim"]
karthi=["Siruthai","Paiya","Thozha","Viruman","Dev","Paruthiveeran","Madras","Kashmora","Sulthan","Meiyazhagan"]
choice=input("Please enter top x number (maximum 10):")
actor=input("Enter the actor name(vijay,suriya,karthi):")
if actor.lower()==vijay:
  for i in range(choice):
    print(i+1,vijay[i])
if actor.lower()==suriya:
  for i in range(choice):
    print(i+1,suriya[i])
if actor.lower()==karthi:
  for i in range(choice):
    print(i+1,karthi[i])
