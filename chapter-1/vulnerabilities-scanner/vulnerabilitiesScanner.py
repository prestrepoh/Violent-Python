import socket
import os
import sys
'''
This programm gets banners from an ip range in certain ports, and then
compares it with a text file to search for vulnerabilities
'''

#Function to get the banner from an ip in a given port
def getBanner(ip,port):
  try:
    socket.setdefaulttimeout(2)
    s = socket.socket()
    s.connect((ip,port))
    banner = s.recv(1024)
    return banner
  except:
    return

#Function to compare a given banner with known vunerabilities
def checkVulnerabilities(banner,filename):
  f = open(filename,'r')
  for line in f.readlines():
    if line.strip('\n') in banner:
      print '  Vulnerability found: ' + banner.strip('\n')

def main():
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
      print '[-] ' + filename + 'does not exist'
      exit(0)
    if not os.access(filename,os.R_OK):
      print '[-]' + filename + 'access denied'
      exit(0)
  else:
    print '[-] Usage: ' + str(sys.argv[0]) + '<vuln filename>'
    exit(0)

  print "hello world"
  ip = "192.168.56.101"
  port = 22
  banner = "banner4"
  portList = [21,22,25,80,110,443]
  for x in range(101,105):
    ip = "192.168.56." + str(x)
    for port in portList:
      print 'checking ' + ip + ':' + str(port)
      banner = getBanner(ip,port)
      if banner:
        print '  banner found:' + banner.strip('\n')
        checkVulnerabilities(banner,filename)

if __name__ == '__main__':
  main()
