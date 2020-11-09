def int_func(word):
    small = word[0]
    big = chr(ord(small) - ord('a') + ord('A'))
    return big + word[1:]


sent = input('Введите слово или строку из маленьких латинских букв').split()
res = []
for word in sent:
    res.append(int_func(word))
print(' '.join(res))
