'''
This programm perform a brut force attack to the SHA-512 file based on a given
dictionary
'''
import crypt
import re

def testPass(cryptPass):
  matchObject = re.match(r'\$6\$(.*)\$.*',cryptPass)
  if matchObject:
    salt = matchObject.group(1)
  else:
    print "  [-]the given password is not sha-512"
    return
  dictFile = open('dictionary.txt')
  for word in dictFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word,'$6$'+salt)
    if (cryptWord == cryptPass):
      print "  [+]Found password: " + word + '\n'
      return
  print "[-]password not found"
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
