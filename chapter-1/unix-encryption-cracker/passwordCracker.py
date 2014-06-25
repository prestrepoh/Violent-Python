'''
This programm performs a brute-force attack to Unix encryption, based on a given
dictionary
'''
import crypt

def testPass(cryptPass):
  salt = cryptPass[0:2]
  dictFile = open('dictionary.txt')
  for word in dictFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word,salt)
    if (cryptWord == cryptPass):
      print "Found password" + word + '\n'
      return
  print "password not found \n"
  return

def main():
  passFile = open('passwords.txt')
  for line in passFile.readlines():
    if ":" in line:
      user = line.split(':')[0]
      cryptPass = line.split(':')[1].strip(' ')
      print "cracking password for: " + user
      testPass(cryptPass)

if __name__ == "__main__":
  main()
