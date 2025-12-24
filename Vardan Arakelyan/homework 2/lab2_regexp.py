import re

# task 1 done
sentence_task_1 = 'Contact us at support@example.com or sales@company.org for assistance. For personal inquiries, email john.doe123@university.edu.'
reg_1 = r'[\w.-]+@\w+\.[A-Za-z]{2,}'
#   + vor menak 1 hat cuyc chta ayl sax matchery, {2, } vor . ic heto 2 tar u avel lini
sol_1 = re.findall(reg_1, sentence_task_1)
print(sol_1)

# task 2 done
numbers_tel = '444-555-6666, 444-555-6667, 444-555-666, 444-555-66667, 444-555-66668 '
reg_2 = r'[0-9]{3}-[0-9]{3}-[0-9]{4}\b'
# {} u tivy nshanakuma ed erkarutyan vercni, \b dnum enq vor dranov verjana
sol_2 = re.findall(reg_2, numbers_tel)
print(sol_2)

# task 3 done
dates = 'Important dates: 25/12/2023, 01-01-2024, 31/05/2023, and 15-10-2024.'
reg_3 = r'[0-9]{2}[/|-][0-9]{2}[/|-][0-9]{4}\b'
sol_3 = re.findall(reg_3, dates)
print(sol_3)

# task 4 done
# erexeqy asecin iranqe chein karoxace dzez ein harcre, es el iranc harcreci )))
rep_text = 'The the quick brown fox jumps over the the lazy dog.'
reg_4 = r'\b(\w+)\s+\1\b'
sol_4 = re.finditer(reg_4, rep_text, flags=re.IGNORECASE)
sol_4 = [sol.group() for sol in sol_4]
print(sol_4)


# task 5 done
hashtags = 'Check out our new products: #Sale2024, #NewArrival, and #Discounts!'
reg_5 = r'#\w+\b'
sol_5 = re.findall(reg_5, hashtags)
print(sol_5)

# task 6
passwords = 'Password123, Secure456, weak, password, Password'
reg_pass = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'

# task 7 done
web = 'Visit our website at https://www.example.com or check out http://blog.example.org for updates.'
reg_7 = r'\w{4,5}://\S+'
sol_7 = re.findall(reg_7, web)
print(sol_7)

# task 8 done
space = 'This   text      has multiple spaces.'
sol_8 = re.sub(r'\s+', ' ', space)
print(sol_8)

# task 9
quoted = 'He said, "Hello, world!" and she replied, "Hi there!"'
reg_9 = r'"([^"]*)"'
sol_9 = re.findall(reg_9, quoted)
print(sol_9)

# task 10
ip = 'Valid: 192.168.1.1, 10.0.0.255 Invalid: 256.1.2.3, 192.168.01.1, 192.168.1 @adlsakjdla @fnsdcno, '
r_ip = r'\d{1,3}.{3}\d{1,3}'


