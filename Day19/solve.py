import regex
from functools import lru_cache


def get_input(f):
  f.seek(0)
  rules, messages = f.read().split("\n\n")
  rules_map = {}
  for rule in rules.split("\n"):
    i, content = rule.split(": ")
    if content.startswith('"'):
      rules_map[i] = [eval(content)]
    content = content.split(' | ')
    rules_map[i] = [c.split() for c in content]
  return rules_map, messages.split("\n")


def part(f, p):
  p = p == 2
  rules_map, messages = get_input(f)

  @lru_cache
  def compile(rule, p2=False):
    if p2:
      if rule == "8":
        return f"{compile('42', p2)}+"
      if rule == "11":
        rule_42 = compile("42", p2)
        rule_31 = compile("31", p2)
        return f"(?P<boi>{rule_42}(?&boi)?{rule_31})"
    if rule not in rules_map:
      return rule[1]
    acc = []
    for i in rules_map[rule]:
      x = "".join(compile(j, p2) for j in i)
      acc.append(x)
    return "(" + "|".join(acc) + ")"

  r = regex.compile(compile("0", p))
  return sum(r.fullmatch(msg) is not None for msg in messages)


with open("input.txt") as f:
  print(part(f, 1))
  print(part(f, 2))
