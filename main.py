# -*- coding: utf-8 -*-
import codecs

stack = []
labels = dict()
code = []
line_number = 0

# Функции отвечающие за работу команд языка

def Error():
    print("Гррр!")
    
def dog_sum(value):
    if len(stack) > 1: stack.append(stack.pop(-1)+stack.pop(-1))
    else: Error()

def dog_sub(value):
    if len(stack) > 1: stack.append(stack.pop(-1)-stack.pop(-1))
    else: Error()    

def dog_mult(value):
    if len(stack) > 1: stack.append(stack.pop(-1)*stack.pop(-1))
    else: Error()   

def dog_div(value):
    if len(stack) > 1: stack.append(stack.pop(-1)//stack.pop(-1))
    else: Error()     

def dog_input(value):
    input_value = input("<< ")
    if input_value.isdigit(): stack.append(int(input_value))
    else: Error()
    
def dog_output(value):
    if len(stack) > 0: print(">>",stack[-1])
    
def dog_chrout(value):
    try:
        print(chr(stack[-1]), end = "")
    except:
        print("?")

def dog_chrin(value):
    value = input("<< ")
    for ch in value:
        stack.append(ord(ch))

def dog_push(value):
    if value.isdigit(): stack.append(int(value))
    else: Error()

def dog_get(value):
    if stack: stack.pop(-1)

def dog_stack(value):
    print("HEAD <<",stack[::-1])

def dog_flip(value):
    global stack
    if len(stack) > 1: stack += [stack.pop(-1),stack.pop(-1)]
    else: Error()

def dog_flip_all(value):
    global stack
    stack = stack[::-1]

def dog_label(value):
    if value and labels.get(value) is None: labels[value] = line_number
    else: Error()

def dog_goto(value):
    global line_number
    if value and labels.get(value) is not None and stack:
        if stack[-1] != 0: line_number = labels[value]
    else: Error()

def dog_exit(value):
    print()
    print("==================")
    input()
    exit()

# Словарь, ассоцирующий команду с функцией.     
cmd = {
"тяв!": dog_input,
"гав!": dog_output,
"тяф!": dog_chrin,
"гаф!": dog_chrout,
"вов!": dog_sum,
"ваф!": dog_sub,
"ряф!": dog_mult,
"вуф!": dog_div,
"тряв!":dog_push,
"тряф!": dog_get,
"руф!": dog_flip,
"раф!" : dog_flip_all,
"рав?": dog_stack,
"хыр": dog_label,
"рых": dog_goto,
"рюх.": dog_exit

}

# Парсер разделяет строку на две части, это команда и ее значения
# команда сверяется с ассоциативным массивом функций, и выполняет функцию ассоциированную с ней. 
def parser(ln):
    ln = ln.strip().split()
    if ln:
        (command, value) = ln[0], ln[1] if len(ln) > 1 else ""
        if cmd.get(command) is not None:
            cmd.get(command)(value)
        else: Error()
    else: Error()

# Читаем по строчно команды и отправляем их в парсер
def run_code():
    global line_number
    print("==================")
    while line_number < len(code): 
        parser(code[line_number])
        line_number += 1

# В редакторе мы зыписываем все введенные строки в массив code, до тех пор пока не введут команду означающую конец программы. Программа запустится.
def editor():
    print("==================")
    global code, line_number
    line = ""
    while line != "рюх.":
        line = input(str(line_number)+": ")
        code.append(line)
        line_number += 1
    line_number = 0
    run_code()

# В редакторе мы читаем файл и записываем все строки в массив code, и запускаем программу с помощью функции run_code
def read_file():
    print("==================")
    file_name = input("Гав, рыв гыррр: ")
    file = codecs.open(file_name,"r","utf-8")
    line = ""
    while line != "рюх.":
        line = file.readline().strip()
        code.append(line)
    file.close()
    run_code()
    print("==================")

# Здесь мы ждем команды: что необходимо запустить редактор или интерпретатор фалов
def main():
    while True:
        comand = input()
        if comand == "груг!": editor()
        elif comand == "рыв!": read_file()
        else: Error()

if __name__ == "__main__": main()
