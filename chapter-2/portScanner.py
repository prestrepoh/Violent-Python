'''
Scann given host in given ports, and grabs its banner
'''
import optparse
import sys
from socket import *
from threading import *
screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
  try:
    connSkt = socket(AF_INET,SOCK_STREAM)
    connSkt.connect(tgtHost,tgtPort)
    connSkt.send('violentPython\r\n')
    results = connSkt.recv(100)
    screenLock.acquire()
    print '[+]%d/tcp open' ,tgtPort
    print '[+] ' + str(results)
    connSkt.close()
  except:
    screenLock.acquire()
    print '[-]%d/tcp closed',tgtPort
  finally:
    screenLock.release()
    connSkt.close()

def portScan(tgtHost,tgtPorts):
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print "[-] Cannot resolve '%s' : Unknown host",tgtHost
    return
  try:
    tgtName= gethostbyaddr(tgtIP)
    print '\n[+] Scan Results for: ' + tgtName[0]
  except:
    print 'n[+] Scan Results for: ' + tgtIP
  setdefaulttimeout(1)
  for tgtPort in tgtPorts:
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()
  print tgtPorts

def main():
  parser = optparse.OptionParser(sys.argv[0] + ' -H <taget host> -p <target port>')
  parser.add_option('-H' ,dest='tgtHost',type='string',help='specify target host')
  parser.add_option('-p',dest='tgtPort',type='string',\
  help='specify target port[s] separated by comma')
  (options, args) = parser.parse_args()
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort).split(',')
  if(tgtHost == None) | (tgtPorts[0] == None):
    print "usage: " + parser.usage
    exit(0)
  portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
  main()
