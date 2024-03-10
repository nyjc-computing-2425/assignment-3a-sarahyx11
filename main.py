nric = input('Enter an NRIC number: ')

letter = 'S', 'T', 'F', 'G'
ST_alphabet = 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'
FG_alphabet = 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K'

d1, d2, d3, d4, d5, d6, d7 = nric[1:8]

if nric[0] in letter and nric[1:8].isdigit() and nric[-1].isalpha() and len(
    nric) == 9:

  sum = (int(d1)*2 + int(d2)*7 + int(d3)*6 + int(d4)*5 + int(d5)*4 + int(d6)*3 + int(d7)*2)

  if nric[0] == "T" or nric[0] == "G":
    sum += 4

  remainder = sum % 11

  if nric[0] == "S" or nric[0] == "T":
    checkdigit = ST_alphabet[remainder]
  else:
    checkdigit = FG_alphabet[remainder]

  if nric[-1] == checkdigit:
    print("NRIC is valid.")
  else:
    print("NRIC is invalid.")

else:
  print("NRIC is invalid.")
