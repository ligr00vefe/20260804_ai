def printList(pList):
  for data in pList:
    print(data, end='\t')
  print()


with open('../source/singer1.csv', 'r', encoding='cp949') as inFp:
  # inStr = inFp.readline()
  # print(inStr, end="")
  # inStr = inFp.readline()
  # print(inStr, end="")
  # header = inFp.readline()
  # print(type(header))
  # header = header.strip()
  # header_list = header.split(',')
  # printList(header_list)
  for inStr in inFp:
    inStr = inStr.strip()
    row_list = inStr.split(',')
    # print(type(row_list)) # <class 'list'>
    printList(row_list)
