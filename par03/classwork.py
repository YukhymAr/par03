name = "Ivan"
city = "Kyiv"
message = "Hello World"

print(len(message)) # повертае кількість символів
print(name(8))
print(name(-1))
print(message(len(message) - 1))
print(city(10))
text = input()
print(text(0))

if len(text) > 0:
    print(text(0))
else:
    print("рядок порожній")

print(text{:2})
print(text{2:5})
print(text[::3]) # через один
print(text[::-1])
# text{3} = "3"
# print(text) - error
print(text.upper()) # велики
text = text.upper()
print(text)
print(text.lower()) # меньшим
print(text.capitalize()) # всі крім першої
print(text.title()) # всі великі
text = "      pyton      programming      "
print(text.lstrip()) #видале пробіл зліва
print(text.rstrip()) #видале пробіл зправа
print(text.strip()) #видале пробіл загалом крі посередині
login = 'admin'
user_login = input('Enter your login name: ')
if user_login.strip().lower() == login:
    print('Login Successful')


text = "pyton"

for char in text:
    print(char)

password = "123qwerty123"
digits = 0
letters = 0
for i in password:
    if i.isdigit():# метод перевіряе чи мае цифри
        digits += 1
    if i.isalpha():
        letters += 1
print(digits)
print(password.isalpha()) # чи е літери
print(password.isdigit()) # чи цифри
print(password.isalnum()) # або цифри або літери

text = input("Enter your text: ").lower().strip()
golosni = 'аіеєиіїуоюя'
counter_golosni = 0
for i in text:
    if i in golosni:
        counter_golosni += 1
print(counter_golosni)

text = "Привіт     світ"
words = text.split()
print(words)

text_new = " ".join(words) # який елемент буде між двоа предметами тобто обернене до split
print(text_new)

text = "Python is easy to learn"
new_text = text.replace("Python", "JavaScript")
print(new_text)

word ="Дід "
word_norm =word.strip().lower()
if word_norm == word_norm[::-1]:
    print('Паліндром')
else:
    print("НЕ ПАЛІНДРОМ")

text = "world"

print(text.find("o"))
print(text.count("l"))

email = "teacher.ivan.komarov@gmail.com"
if email.lower().endswith(("@gmail.com")): #.startswith
    print("у тебе гуглівська пошта")