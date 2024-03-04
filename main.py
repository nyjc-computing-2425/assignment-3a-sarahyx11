nric = input('Enter an NRIC number: ')

letter = ['S', 'T', 'F', 'G']
digit = '1234567'
weight = [2, 7, 6, 5, 4, 3, 2]
ST_alphabet = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
FG_alphabet = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']

if nric[0] in letter and nric[1:8].isdigit() and nric[-1].isalpha() and len(
    nric) == 9:
  d1, d2, d3, d4, d5, d6, d7 = map(int, nric[1:8])
  sum = (d1 * weight[digit.find(str(d1))] + d2 * weight[digit.find(str(d2))] +
         d3 * weight[digit.find(str(d3))] + d4 * weight[digit.find(str(d4))] +
         d5 * weight[digit.find(str(d5))] + d6 * weight[digit.find(str(d6))] +
         d7 * weight[digit.find(str(d7))])
  if nric[0] == "T" or nric[0] == "G":
    sum = sum + 4
  remainder = sum % 11
  if nric[0] == "S" or nric[0] == "T":
    checkdigit = ST_alphabet[remainder]
  else:
    checkdigit = FG_alphabet[remainder]
  if nric[-1] == checkdigit:
    print("Nric format is valid.")
  else:
    print("Nric format is invalid.")
else:
  print("Nric format is invalid.")
print(sum)
print(remainder)
print(checkdigit)
