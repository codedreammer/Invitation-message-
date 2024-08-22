names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

extra_names = [input("Enter a friends's name : ")]
extra_names2 = [input("Enter a friends's name : ")]

all_names = names + names1 + extra_names + extra_names2

for name in all_names:
    print(f"{name .title()}! You are invited to the party on saturday. ")

