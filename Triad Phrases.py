def is_triad_phrase(ch):
  tableOfAllWords=ch.split()
  dictionnary=["LAND","ERE"]
  test=True
  for item in tableOfAllWords:
    tableOfTwoWords=["",""]
    for i in range(1,len(item)+1):
      if i%2!=0:
        tableOfTwoWords[0]=tableOfTwoWords[0]+item[i-1]
      else:
        tableOfTwoWords[1]=tableOfTwoWords[1]+item[i-1]
    if tableOfTwoWords[0] not in dictionnary or  tableOfTwoWords[1] not in dictionnary:
      test=False
  return test
print(is_triad_phrase("studied theories"))