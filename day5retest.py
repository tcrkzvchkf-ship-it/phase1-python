numbers = [5, 12, 3, 8, 19, 7, 14, 2, 11, 6]

great = [n for n in numbers if n > 8]
multi = [n * 2 for n in numbers]
total = 0
for n in numbers:
    total += n
    

print(great)
print(multi)
print(total)


#Challenge 2



def avg_perclass(class_avg):
    total = 0
    for n in class_avg.values():
        total += n
    return total/len(class_avg)

class_avg = {
    "Vasu": 90,
    "piyu": 75,
    "raj": 85,
    "kalpana": 75,
    "paresh": 85
}

print(avg_perclass(class_avg))

#Challenge 3

def group_contacts(contacts):
    gmail = []
    other = []
    for key, value in contacts.items():

        if value["email"].endswith("@gmail.com"):
            gmail.append(key)
        else:
            other.append(key)
    return gmail, other




contacts = {
    "Vasu": {"phone": "123-345-5457", "email": "vas@gmail.com" },
    "Piyu": {"phone": "123-345-5457", "email": "piyu@gmail.com" },
    "raj": {"phone": "123-345-5457", "email": "raj@gmail.com" },
    "Kalpana": {"phone": "123-345-5457", "email": "kal@hotmail.com" },
    "Karan": {"phone": "123-345-5457", "email": "kar@hotmail.com" },
}


gmail, other = group_contacts(contacts)
print(f"Gmail contacts: {gmail}")
print(f"Other contacts: {other}")


