def reverse_list(l):
    'return a list with the reverse order of l'
    res = []
    for i in reversed(range(0, len(l))):
        res.append(l[i])
    return res


def reverse_list(l):
  return l[::-1]


def reverse_list(l):
  """return a list with the reverse order of l"""
  return list(reversed(l))


def reverse_list(l):
  l.reverse()
  return l

print(reverse_list(xx))

