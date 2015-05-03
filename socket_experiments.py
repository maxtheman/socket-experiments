import socket as skt
import optparse

host_name = "www.google.com"

print socket.gethostbyname(host_name)

usage = 'usage: %prog -H <target host> -p <target port>'

#command line script usage
# -H is the target host eg 'wwww.google.com'
# -p is the target port eg 80
parser = optparse.OptionParser(usage=usage)
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options,args) = parser.parse_args()
target_host = options.tgtHost
target_port = options.tgtPort
if (target_host == None) or (target_port == None):
	print parser.usage
	exit(0)
	
def connection_scan(target_host, target_port):
	try:
		connect_socket = skt.socket(AF_INET, SOCK_STREAM)
		connect_socket.connect((target_host, target_port))
		print'[+]%d/tcp open' % target_port
		connect_socket.close()
	except:
		print '[-]%d/tcp closed' % target_port