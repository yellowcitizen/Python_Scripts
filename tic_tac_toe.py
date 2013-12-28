#! /usr/bin/python
import random
import sys
board = [0,1,2,3,4,5,6,7,8]

def show():
  print board[0],'|',board[1],'|',board[2]
  print '-----------'
  print board[3],'|',board[4],'|',board[5]
  print '-----------'
  print board[6],'|',board[7],'|',board[8]

show()
def checkLine(char, spot1, spot2, spot3):
  if board[spot1] == char and board[spot2] == char and board[spot3] == char:
    return True

def checkAll(char):
  if checkLine(char, 0, 1, 2):
    return True
  if checkLine(char, 1, 4, 7):
    return True
  if checkLine(char, 2, 5, 8):
    return True
  if checkLine(char, 6, 7, 8):
    return True
  if checkLine(char, 3, 4, 5):
    return True
  if checkLine(char, 0, 3, 6):
    return True
  if checkLine(char, 2, 4, 6):
    return True
  if checkLine(char, 0, 4, 8):
    return True

while True:
  input = raw_input("Select a spot: ")
  input = int(input)

  if board[input] != 'x' and board[input] != 'o':
    board[input] = 'x'
    #check
    if checkAll('x') == True:
      print '--- X WINS ---'
      show()
      sys.exit()
      break

    while True:

      random.seed()
      op = random.randint(0,8)
      if board[op] != 'o' and board[op] != 'x':
        board[op] = 'o'
        if checkAll('o') == True:
          print '--- O WINS ---'
          show()
          sys.exit()
          break

        break;

  else:
    print 'This spot is taken!'

  show()
