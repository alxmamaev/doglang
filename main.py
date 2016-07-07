# -*- coding: utf-8 -*-
stack = []

def Error():
    print("Error!")

def dog_sum(values):
    if len(stack) > 1: stack.append(stack.pop(-1)+stack.pop(-1))
    else: Error()

def dog_sub(values):
    if len(stack) > 1: stack.append(stack.pop(-1)-stack.pop(-1))
    else: Error()    

def dog_mult(values):
    if len(stack) > 1: stack.append(stack.pop(-1)*stack.pop(-1))
    else: Error()   

def dog_div(values):
    if len(stack) > 1: stack.append(stack.pop(-1)//stack.pop(-1))
    else: Error()     

def dog_input(values):
    value = input("<< ")
    if value.isdigit(): stack.append(int(value))
    else: Error()
    
def dog_output(values):
    if len(stack) > 0: print(">>",stack.pop(-1))

cmd = {
"тяф!":dog_input,
"гав!":dog_output,
"вов!": dog_sum,
"ваф!": dog_sub,
"ряф!": dog_mult,
"вуф": dog_div
}

def parser(ln):
    ln = ln.split()
    if ln:
        (command, values) = ln[0], ln[1] if len(ln) > 1 else ""
        if cmd.get(command) is not None:
            cmd.get(command)(values)
    else: Error()

while True:
    parser(input())