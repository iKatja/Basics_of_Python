'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''
from googletrans import Translator

with open('test_4_in.txt') as f_in, open('test_4_out.txt', 'w') as f_out:
    text = f_in.read()
f_out.write(Translator().translate(text, dest='ru').text)
