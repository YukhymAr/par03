#1
text = input("Enter a text: ")
alletters = 0
digits = '0123456789'
alldigits = 0
allspace = 0
golosni = 'аіеєиіїуоюя'
counter_golosni = 0
space = " "
letters = 'йцукенгшщзхїфівапролджєячсмить'
for i in text:
    if i in digits:# метод перевіряе чи мае цифри
        alldigits += 1
    if i in letters:
        alletters += 1
    if i in space:
        allspace += 1
    if i in golosni:
        counter_golosni += 1
words = text.split()
word_count = len(words)

print("Слів:", word_count)
print("Літер:" , alletters)
print("Чисел:" , alldigits)
print("Пробілів:" , allspace)
print("Голосні:" , counter_golosni)

#2
text = input()
words = text.split()

result = []
result.append(words[0])
result.append(words[1][0])
result.append(words[2][0])
text_new = ".".join(result).title()
print(text_new)

#3
word1 = input("Enter a word").lower().replace(" ","")
word2 = input("Enter another word").lower().replace(" ","")


annagram =  len(word1) == len(word2)

if annagram:
    for i in word1:
        if word1.count(i) != word2.count(i):
            annagram = False
            break

if annagram:
    print("Рядки е аннаграмою")
else:
    print("Не є анаграммами")