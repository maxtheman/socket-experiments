import socket
import optparse

host_name = "www.google.com"

print socket.gethostbyname(host_name)

usage = 'usage: %prog -H <target host> -p <target port>'

parser = optparse.OptionParser(usage=usage)
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options,args) = parser.parse_args()
target_host = options.tgtHost
target_port = options.tgtPort
if (target_host == None) or (target_port == None):
	print parser.usage
	exit(0)