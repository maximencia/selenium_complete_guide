# -*- coding: utf-8 -*-
import string,random
a = 3
b = 5
r = 0  # Чтобы было, чем заполнять
mas = []
for i in range(a):
    mas.append([])
    for j in range(b):
        mas[i].append(r)
        r += 1  # Чтобы заполнялось не одно и тоже

print(mas)
print ((mas[0][2    ]))

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains): return random.choice(domains)

def get_random_name(letters, length): return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length): return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def generate_mail(): return (generate_random_emails(1, 7))

p=generate_mail();
print (p)