def encrypt(message, keyword):
  matrix = createEncMatrix(len(keyword), message)
  keywordSequence = getKeywordSequence(keyword)

  ciphertext = ""
  for num in range(len(keywordSequence)):
    pos = keywordSequence.index(num + 1)
    for row in range(len(matrix)):
      if len(matrix[row]) > pos:
        ciphertext += matrix[row][pos]
  return ciphertext


def createEncMatrix(width, message):
  r = 0
  c = 0
  matrix = [[]]
  for pos, ch in enumerate(message):
    matrix[r].append(ch)
    c += 1
    if c >= width:
      c = 0
      r += 1
      matrix.append([])

  return matrix


def getKeywordSequence(keyword):
  sequence = []
  for pos, ch in enumerate(keyword):
    previousLetters = keyword[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence


def decrypt(message, keyword):
  matrix = createDecrMatrix(getKeywordSequence(keyword), message)

  plaintext = ""
  for r in range(len(matrix)):
    for c in range(len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def createDecrMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = int(len(message) / width)
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height, len(message))

  pos = 0
  for num in range(len(keywordSequence)):
    column = keywordSequence.index(num + 1)

    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1

  return matrix


def createEmptyMatrix(width, height, length):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      if totalAdded >= length:
        return matrix
      matrix[r].append('')
      totalAdded += 1
  return matrix


print('1- For encrypt\n'
      '2- For decrypt\n')
choice = int(input('Please, Enter your choice: '))

if choice == 1:
  plain_text = input('Please, enter your text: ')
  key = input('Please, Enter the key: ')
  print('The encrypted text is: ', encrypt(plain_text, key))
elif choice == 2:
  cipher_text = input('Please, enter your text: ')
  key = input('Please, Enter the key: ')
  print('The plain text is: ', decrypt(cipher_text, key))
else:
  print('Your choice is not exist')

  
#print(encrypt('Germany seeks an alliance', 'norse'))
#print(decrypt('aealeGnenieyk ar sanms lc', 'norse'))
# 'The nose is pointing down and the houses are getting bigger' 'analyst'
