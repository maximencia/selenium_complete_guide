# -*- coding: utf-8 -*-
import string,random
import re
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
b=False
while not b:
    i=i+1
    print(i)
    if i==10:
        b=True

text="http://localhost/litecart/admin/?app=catalog&doc=edit_product&category_id=0&product_id=7"
text2=re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
text3=re.sub(r'http:\/\/localhost\/litecart\/admin\/\?app=catalog\&doc=edit_product\&', '_', text, flags=re.IGNORECASE)
text4=re.sub(r'\&', '_', text3, flags=re.IGNORECASE)
text5=re.sub(r'=', '_', text4, flags=re.IGNORECASE)
print (text3)
print (text4)
print (text5)

print (u'ГОТОВО')

# # content of test_expectation.py
# import pytest
# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 42),
# ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
#


#!/usr/bin/env python
import random

words =  ["Alex", "Kate", "Love", "World", "Peace", "Putin","World2", "Peace2", "Putin2",]
unique_words = list(set(words))
random.shuffle(unique_words) # shuffle using default Mersenne Twister generator
random.SystemRandom().shuffle(unique_words)  # OS-provided generator
print("\n".join(unique_words))
print
print (unique_words[0])
print (unique_words[1])
print (unique_words[2])
