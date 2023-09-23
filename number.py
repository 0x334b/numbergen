import random # https://github.com/callsta

def generator(provider, amount):
    indosat = ['62815', '62816', '62855', '62856', '62857', '62858']
    telkomsel = ['0811', '0812', '0813', '0821', '0852', '0853']
    axiata = ['0817', '0818', '0819', '0859', '0877', '0878', '0879'] 
    smartfreen = ['0881', '0882'] 
    three = ['0899', '0898', '0896', '0897']
    if provider == "indosat":
        provider_list = indosat
    elif provider == "telkomsel":
        provider_list = telkomsel
    elif provider == "axiata":
        provider_list = axiata
    elif provider == "smartfreen":
        provider_list = smartfreen
    elif provider == "three":
        provider_list = three
    else:
        print("Invalid provider.")
        return
    try:
        amount = int(amount)
    except ValueError:
        print("Amount should be a valid number.")
        return

    for _ in range(amount):
        ListA = random.choice(provider_list)
        randomA = random.randint(1000, 9999)
        randomB = random.randint(1000, 9999)
        print(f"{ListA}-{randomA}-{randomB}")
    print("Successfully generated", amount)


zz = '''
[       INDONESIA NUMBER GENERATOR         ]
-> indosat
-> telkomsel
-> axiata
-> smartfreen
-> three
-> exit
'''
print(zz)
user = input("Input (example: indosat) => ")
amount = input("Amount => ")
prov = ["indosat", "telkomsel", "axiata", "smartfreen", "three"]
if user in prov:
    generator(user, amount)
elif user == "exit":
    print("Thanks for using this tool.")
else:
    print("Enter a valid provider.")
