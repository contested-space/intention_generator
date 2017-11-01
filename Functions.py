from random import random
import sys
from wx import Point

def generate():
  s = 'S'
  loop = 1;
  while (loop == 1):
    #print " before createNext: " + str
    s += createNext(s[-1])
    
    if s[-1] == '0':
      loop = 0
  return s

def extend(p):
  a = 0.1 #low prob for debug
  if (random() < a):
    return '[' + generate() + ']'
  else:
    return ''

def createNext(c):
  p = random()
  if c == 'S':
    if p < 0.4 :
      return extend(p) + 'P'
    elif p < 0.7 :
      return extend(p) + 'E'
    elif p < 0.95 :
      return extend(p) + 'A'
    else:
      return extend(p) + '0'
  elif c == 'P':
    if p < 0.1 :
      return extend(p) + 'S'
    elif p < 0.6 :
      return extend(p) + 'A'
    elif p < 0.8 :
      return extend(p) + 'C'
    else:
      return extend(p) + '0'
  elif c == 'E':
    if p < 0.2 :
      return extend(p) + 'S'
    elif p < 0.4 :
      return extend(p) + 'P'
    elif p < 0.7 :
      return extend(p) + 'A'
    elif p < 0.9:
      return extend(p) + 'C'
    else:
      return extend(p) + '0'
  elif c == 'A':
    if p < 0.2 :
      return extend(p) + 'E'
    elif p < 0.8 :
      return extend(p) + 'C'
    else:
      return extend(p) + '0'
  elif c == 'C':
    if p < 0.7 :
      return extend(p) + 'S'
    elif p < 0.8 :
      return extend(p) + 'P'
    elif p < 0.9 :
      return extend(p) + 'E'
    elif p < 0.95:
      return extend(p) + 'A'
    else:
      return extend(p) + '0'
  else:
   return '0'


"""
def store(str, mat, i, j, level):
  if (len(str) > 0):
    if(str[0] == '['):
      if mat[i][j+level] != '-':
        store(str, mat, i, j, level + 1)
      else:
        store(str[1:], mat, i, j, level)
    elif(str[0] == ']'):
      if (level > 0):
        store(str, mat, i, j, level - 1)
      else:
        store(str[1:], mat, i, j - 1, level)
    else:
      mat[i][j+level] = str[0]
      store(str[1:], mat, i + 1 , j, level)
"""


#receives a 2d matrix filled with '-' characters, stores the l-system in it

"""
def store(s, mat):
  i = 0
  j = 0
  level = 0
  subLength = [0 for x in range(len(mat))]
  for c in s:
    if c == '[':
      while (j + level < len(mat[0]) and mat[i][j+level] != '-'):
        level += 1
      j += 1
      i -= 1
    elif c == ']':
      while(level > 0 and j + level < len(mat[0]) and mat[i][j+level] == '-'):
        level -= 1
      j -= 1
      i -= subLength[j]
      subLength[j] = 0
    else:
      mat[i][j+level] = c
      i += 1
      if level > 0:
        print 'I HAPPEN'
        subLength[j] +=1
"""

class Concept:
  def __init__(self, c = None, parent = None, precedent = None):
    self.concept = c
    self.parent = parent
    self.child = None
    self.next = None
    self.precedent = None
    self.pos = Point()

  def setPos(self, p):
    self.pos = p

  def setConcept(self, concept):
    self.concept = concept

  def getConcept(self):
    return self.concept

  def getChild(self):
    return self.child

  def setChild(self, child):
    if self.child == None:
      self.child = child
      self.child.setParent(self)
      #print 'SETCHILD ACTIVE'

  def setPrecedent(self, precedent):
    if self.precedent == None:
      self.precedent = precedent
      self.precedent.setNext(self)

  def setNext(self, next):
    if self.next == None:
      self.next = next
      self.next.setPrecedent(self)

  def getParent(self):
    return self.parent

  def getPrecedent(self):
    return self.precedent

  def getNext(self):
    return self.next

  def getFirstParent(self):
    if self.parent == None and self.precedent != None:
      return self.getPrecedent().getFirstParent()
    elif self.parent != None:
      return self.parent
    else:
     return None


  def setParent(self, parent):
    if self.parent == None:
      self.parent = parent
      #self.getParent().setChild(self)



  def makeStructure(self, s):
    if len(s) > 0:
      if s[0] == '[':
        self.setChild(Concept())
        #print 'setChild :' + s[1]
        self.getChild().makeStructure(s[1:])
        #print 'child: ' + self.getChild().getConcept()
      elif s[0] == ']':
        self.getFirstParent().setNext(Concept())
        #print 'setNext' + s[1]
        self.getFirstParent().getNext().makeStructure(s[1:])
      else:
        self.setConcept(s[0])
        #print 'setConcept' + s[0]
        if len(s) > 1 and s[1] != '[' and s[1] != ']':
          self.setNext(Concept())
          #print 'setNext: ' + s[1]
          self.getNext().makeStructure(s[1:])
        elif len(s) > 1 and s[1] == '[':
          self.makeStructure(s[1:])
        elif len(s) > 1 and s[1] == ']':
          self.makeStructure(s[1:])
        



def printStructure(concept, i, j):  
  if concept != None:
    if concept.getConcept() != None:
      sys.stdout.write(concept.getConcept())
      if concept.getNext() != None:
        printStructure(concept.getNext(), i , j)
      if concept.getChild() != None:
        print
        for x in range(i):
          sys.stdout.write(' ')
        printStructure(concept.getChild(), i + 1, j)
    else:
      print 'end of tree'



  



"""
      print 'i' + str(i)
      print 'j' + str(j)
      print "j + level" + str(j + level)
      print mat[i][j+level]
      print len(mat[0])
"""


#mat = [['-' for x in range(100)] for x in range(100)]


#str =  generate()

#s = 'S[SPEAC]PEA[SPA[SPACE]CE]C'

#s = 'S[PA[PA]C]C'

#store(str, mat, 0, 0, 0)
#store(s, mat)


#a = Concept()
#a.makeStructure(s)

#print 'a.getConcept(): ' + a.getConcept()
#print 'a.getChild().getConcept(): ' + a.getChild().getConcept()
#print a.getChild().getPrecedent().getConcept()
#print 'a.getNext().getConcept(): ' + a.getNext().getConcept()

#printStructure(a, 0, 0)
#print
#print s
#print s[1:]




"""
for y in range(len(mat)):
  for x in range(len(mat[0])):
    if (mat[x][y] !='0'):
      sys.stdout.write(mat[x][y])
    else:
      sys.stdout.write(' ')
  print ''

print s

print mat[0][0]

"""


