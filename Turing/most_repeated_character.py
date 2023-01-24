import functools
def solution (s: list):
  values: dict = {}
  for i in s:
    if not i.isnumeric():
      values[i] = values[i] + 1 if i in values else 1
  max_value = None
  for value in values:
    if not max_value:
      max_value = value
      continue
    if values[value] > values[max_value]:
      max_value = value

  return max_value

if __name__ == '__main__':
    output = solution('aaaaAAAA1234RRAAAAARRrrrr0r0rabasfs')
    print(output)