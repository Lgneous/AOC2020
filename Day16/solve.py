import sys


with open(sys.argv[1]) as f:
  content = f.read()

fields_, your_ticket, tickets = content.split("\n\n")

fields = []
for field in fields_.split('\n'):
  _, field = field.split(": ")
  ranges = field.split(" or ")
  pair_range = []
  for r in ranges:
    min, max = r.split('-')
    pair_range.append(range(int(min), int(max)+1))
  fields.append(pair_range)

def to_ticket(s):
  return list(map(int, s.split(',')))

your_ticket = to_ticket(your_ticket.split('\n')[1])

tickets = list(map(to_ticket, tickets.split('\n')[1:]))

def is_maybe_valid(fields, ticket):
  for value in ticket:
    for field in fields:
      if value in field:
        break
    else:
      return False
  return True

error = 0
fields_temp = [x for y in fields for x in y]
for ticket in tickets:
  for v in ticket:
    for field in fields_temp:
      if v in field:
        break
    else:
      error += v
print(error)

class TupleUnion(tuple):
  def __contains__(self, key):
    return key in self[0] or key in self[1]

nb_fields = len(ticket)
tickets = list(filter(lambda x: is_maybe_valid(fields_temp, x), tickets))

fields_order = fields
fields = {TupleUnion(x): list(range(nb_fields)) for x in fields}

for range, cols in fields.items():
  to_del = []
  for i in cols:
    for ticket in tickets:
      if ticket[i] not in range:
        to_del.append(i)
  for i in to_del:
    cols.remove(i)
  
fields = list(map(list, fields.items()))
fields.sort(key=lambda t: len(t[1]))

used_col = set()
for field in fields:
  for val in field[1]:
    if val not in used_col:
      field[1] = val
      used_col.add(val)
      break

fields = dict(fields)
acc = 1
for field in fields_order[:6]:
  acc *= your_ticket[fields[TupleUnion(field)]]
print(acc)
