key = input('Yes?: ')


def print_me(string):
  print(string)


test_dict = {
  'fun': print_me,
  'foo': print_me
}

functionToCall = test_dict[key]

functionToCall(key)