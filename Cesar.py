code = 3 #shift amount
AL = ("abcdefghijklmnopqrstuvwxyz") #allowed alphabet
encr = ("") 
Klartext = ("abcdefghijklmnopqrs2tuvwxyz") #text to be encrypted
print(Klartext)
Klartext = Klartext.lower() #since only lowercase is allowed
for i in Klartext:
	if i in AL:
		if i != " ":
			encr += AL[(AL.index(i) + code)%26]
		else:
			encr += " "
	else:
		encr += i
print(encr)
