# -*- coding: utf-8 -*-
import codecs

stack = []
labels = dict()
code = []
line_number = 0

def Error():
    input("Гррр!")
    exit()
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
    if len(stack) > 0: print(">>",stack.pop(-1))

def dog_push(value):
    if value.isdigit(): stack.append(int(value[1]))
    else: Error()

def dog_get(value):
    if stack: stack.pop(-1)

def dog_stack(value):
    print("HEAD <<",stack[::-1])

def dog_flip(value):
    global stack
    if len(stack) > 1: stack += [stack.pop(-1),stack.pop(-1)]
    else: Error()

def dog_label(value):
    if value and labels.get(value) is None: labels[value] = line_number
    else: Error()

def dog_goto(value):
    global line_number
    if value and labels.get(value) is not None:
        if stack[-1] == 0: line_number = labels[value]
    else: Error()

def dog_exit(value):
    input("==================")
    exit()
       
cmd = {
"тяф!":dog_input,
"гав!":dog_output,
"вов!": dog_sum,
"ваф!": dog_sub,
"ряф!": dog_mult,
"вуф!": dog_div,
"тряв!":dog_push,
"тряф!":dog_get,
"руф!":dog_flip,
"рав?":dog_stack,
"хыр": dog_label,
"рых":dog_goto,
"рюх.":dog_exit

}

def parser(ln):
    ln = ln.strip().split()
    if ln:
        (command, value) = ln[0], ln[1] if len(ln) > 1 else ""
        if cmd.get(command) is not None:
            cmd.get(command)(value)
        else: Error()
    else: Error()

def run_code():
    global line_number
    print("=====================")
    while line_number < len(code): 
        parser(code[line_number])
        line_number += 1

def editor():
    print("=====================")
    global code
    while line != "рюх.":
        line = input()
        code.append(line)
    run_code()
    
def read_file():
    print("=====================")
    file_name = input("Гав, рыв гыррр: ")
    file = codecs.open(file_name,"r","utf-8")
    line = ""
    while line != "рюх.":
        line = file.readline().strip()
        code.append(line)
    file.close()
    run_code()
    print("=====================")
def main():
    while True:
        comand = input()
        if comand == "груг!": editor()
        elif comand == "рыв!": read_file()
        else: Error()

if __name__ == "__main__": main()
