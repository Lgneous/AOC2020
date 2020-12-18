import sys


with open("sys.argv[1]) as f:
  content = f.read().split('\n')

op = {
  '+': lambda x,y: x+y,
  '*': lambda x,y: x*y
}

def tokenizer(s):
  s = s.replace('(', ' ( ').replace(')', ' ) ').split()
  return list((s))

def parse(s, precedence=False):
  rpn = []
  operators = []
  for i in s:
    if i.isnumeric():
      rpn.append(int(i))
    if i == '(':
      operators.append(i)
    if i == ')':
      while operators[-1] != '(':
        rpn.append(operators.pop())
      operators.pop()
    if i in {'+', '*'}:
      if operators and operators[-1] in {'+', '*'} and (not precedence or operators[-1] >= i):
        rpn.append(operators.pop())
      operators.append(i)
  while operators:
    rpn.append(operators.pop())
  return rpn

def eval(rpn):
  stack = []
  for i in rpn:
    if i in {'+', '*'}:
      stack.append(op[i](stack.pop(), stack.pop()))
    else:
      stack.append(i)
  return stack[-1]

def part1(s):
  return eval(parse(tokenizer(s)))

def part2(s):
  return eval(parse(tokenizer(s), True))

print(sum(map(part1, content)))
print(sum(map(part2, content)))
