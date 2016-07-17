# -*- coding: utf-8 -*-
import codecs
import os.path

stack = []
labels = dict()
line_number = 0

# Функции отвечающие за работу команд языка

def RunTimeError():
    print("Гррр! Рыф! Роггрр: %s!"%(line_number+1))
    return 1
def CompilationError():
    print("Гррр! Вофр! Роггрр: %s!"%(line_number+1))
    return 1

def dog_sum(values):
    if len(values) > 0: CompilationError()
    if len(stack) > 1: 
        stack.append(stack.pop(-1)+stack.pop(-1))
        return 0
    else: return RunTimeError()

def dog_sub(values):
    if len(values) > 0: CompilationError()
    if len(stack) > 1: 
        stack.append(stack.pop(-1)-stack.pop(-1))
        return 0
    else: return RunTimeError()    

def dog_mult(values):
    if len(values) > 0: CompilationError()
    if len(stack) > 1: 
        stack.append(stack.pop(-1)*stack.pop(-1))
        return 0
    else: return RunTimeError()   

def dog_div(values):
    if len(values) > 0: CompilationError()
    if len(stack) > 1: 
        stack.append(stack.pop(-1)//stack.pop(-1))
        return 0
    else: return RunTimeError()     

def dog_input(values):
    if len(values) > 0: CompilationError()
    value = input("<< ").split()
    if value.isdigit(): stack.append(int(value))
    else: return RunTimeError()
    return 0

def dog_output(values):
    if len(values) > 0: CompilationError()
    if len(stack) > 0: print(stack[-1],end = "")
    return 0

def dog_chrin(values):
    if len(values) > 0: CompilationError()
    value = input("<< ")
    for ch in value: stack.append(ord(ch))
    return 0 

def dog_chrout(values):
    if len(values) > 0: CompilationError()
    try:
        print(chr(stack[-1]), end = "")
    except:
        print("?")
    return 0

def dog_push(values):
    for value in values:
        if value.isdigit(): 
            stack.append(int(value))
        else: return CompilationError()
    return 0

def dog_del(values):
    if len(values) > 0: CompilationError()
    if stack: stack.pop(-1)
    return 0

def dog_stack(values):
    if len(values) > 0: CompilationError()
    print("HEAD <<",stack[::-1])
    return 0    

def dog_flip(values):
    if len(values) > 0: CompilationError()
    global stack
    if len(stack) > 1: stack += [stack.pop(-1),stack.pop(-1)]
    return 0

def dog_flip_all(values):
    if len(values) > 0: CompilationError()
    global stack
    stack = stack[::-1]
    return 0

def dog_goto(values):
    global line_number
    if len(values) == 1 and labels.get(values[0]) is not None and stack:
        if stack[-1] != 0: line_number = labels[values[0]]
        return 0
    else: return CompilationError()

def dog_label(values):
    if len(values) == 1:
        if labels.get(values[0]) is None: labels[values[0]] = line_number
        return 0
    else: return CompilationError()

def reset():
    global line_number, stack, labels
    stack = []
    labels = dict()
    line_number = 0    
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
"тряф!": dog_del,
"руф!": dog_flip,
"раф!" : dog_flip_all,
"рав?": dog_stack,
"рых": dog_goto,
"хыр" : dog_label,
}


# Функция убирает все что не нужно интепретатору (символы переноса, табуляцию комментариии)
def line_format(line):
    line = line.strip()
    comment_chr = ";"
    special_chrs = ["\n","\t","\v"]
    frmt_line = ""
    space = False
    for ch in line:
        if ch == comment_chr: break
        elif space and ch == " ":
            frmt_line += " "
            space = False
        elif ch not in special_chrs:
            frmt_line += ch
            space = True
    return frmt_line.split() if frmt_line else None


def run(code):
    global line_number
    while line_number < len(code):
        line = line_format(code[line_number])
        if line is not None: 
            (command, values) = line[0], line[1:]
            if cmd.get(command) is not None: 
                if cmd[command](values):
                    reset()
                    return 1
            
            else: return CompilationError()
        line_number += 1
    reset()
    return 0

def main():
    print("Doglang v1.1")
    while True:
        print("\n==================")
        file_name = input("< ")
        file = codecs.open(file_name,"r","utf-8")
        run(file.readlines())
        file.close()
        
if __name__ == "__main__": main()
