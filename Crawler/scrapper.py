'''
Crawler para sacar IPs de myip.ms
v1 -> 16MAY, JC
v2 -> 18MAY, JC
'''


import random
import urllib2
import cookielib
import re
import time
import socks
import socket
import os
import subprocess


class CustomRequest(object):
	# Constructor
	def __init__(self):
		# Headers
		self.hdr_userAgent = ''
		self.hdr_accept = ''
		self.hdr_acceptLanguage = ''
		self.hdr_referer = ''
		self.hdr_connection = ''
		# Other settings
		self.html_content = ''
		# I am not a robooot
		self.randomize()
			

	# Returns the HTML content in a string
	def getHTML(self, url):
		body = StringIO() # needs something to acts liek a buffer
		petition = pycurl.Curl()
		# Target
		petition.setopt(pycurl.URL, url)
		# Headers
		c.setopt(pycurl.HTTPHEADER, 
				[
				'User-Agent: ' + self.hdr_userAgent,
				'Accept: ' + self.hdr_accept,
				'Accept-Language: ' + self.hdr_acceptLanguage,
				'Referer: ' + elf.hdr_referer,
				'Connection: ' + self.hdr_connection,
				])
		# Forcing IPv4
		c.setopt(c.IPRESOLVE, c.IPRESOLVE_V4)
		# Pointing results
		c.setopt(c.WRITEFUNCTION, body.write)
		# Enabling TOR
		c.setopt(pycurl.PROXY, "127.0.0.1")
		c.setopt(pycurl.PROXYPORT, 9050)
		c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
		# Go TOR!
		c.perform()
		c.close()

		return body.getvalue()


	# Returns a boolean. Checks if the limit have been reached 
	def shouldIStop(self):
		regex = ('You have already viewed the maximum number of Myip.ms pages per day' + # no user
			'|' + # or
		 	'The maximum daily number of Myip.ms pages per day has already been viewed from your IP address' #logged user
		 	) 
		regex_c = re.compile(regex)
		if re.search(regex_c, self.html_content): #not NONE
			print ">> Maximum request per day regex match!"
			return True
		return False

	
	# Randomize the headers content within some prefixed lists
	def randomize(self):
		# http://www.useragentstring.com/
		userAgent_list = [
			"Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; RW; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",
			"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",
			"Mozilla/5.0 (X11; U; Linux i686; ru; rv:33.2.3.12) Gecko/20120201 SeaMonkey/8.2.8",
			"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20120501 Firefox/12.0 SeaMonkey/2.9.1 Lightning/1.4",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20120502 SeaMonkey/2.9.1",
			"Mozilla/5.0 (Windows NT 6.1 WOW64 rv:12.0) Gecko/20120429 Firefox/12.0 SeaMonkey/2.9.1",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
			"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
			"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
			"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
			"Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
			"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
			"Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.8pre) Gecko/20070928 Firefox/2.0.0.7 Navigator/9.0RC1",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.8pre) Gecko/20070928 Firefox/2.0.0.7 Navigator/9.0RC1",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.8pre) Gecko/20071001 Firefox/2.0.0.7 Navigator/9.0RC1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:2.0b4) Gecko/20100818",
			"Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
			"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
			"Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
			"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36"
		]
		acceptLanguage_list = [
			"en",
			"da",
			"en-gb",
			"es-es",
			"de",
			"it",
			"es-mx",
			"pt-br",
		]
		acceptLanguage_req = "en-us"
		referer_list = [
			"https://myip.ms/",
			"https://www.myip.ms/browse/comp_browseragents/Computer_Browser_Agents.html",
			"https://www.myip.ms/view/best_hosting/IND/Best_Hosting_in_India.html",
			"https://www.myip.ms/view/web_hosting/21643",
			"https://www.myip.ms/view/best_hosting/USA/Best_Hosting_in_USA.html",
			"https://www.myip.ms/view/best_hosting/JPN/Best_Hosting_in_Japan.html"
		]				
		accept_list = ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"] # should be improved...
		connection_list = ["keep-alive", "close"]

		# Headers
		self.hdr_userAgent = random.choice(userAgent_list)
		self.hdr_accept = random.choice(accept_list)
		self.hdr_referer = random.choice(referer_list)
		self.hdr_connection = random.choice(connection_list)
		self.hdr_acceptLanguage = acceptLanguage_req
		for i in range(1, random.randint(1,3)): # up to 3 random languages with random quantifiers
			self.hdr_acceptLanguage += ( ', ' + random.choice(acceptLanguage_list) 
				+ ';q=' + str(random.uniform(0.1, 0.9))[:3] # the preference quantifier 
				) 					
		
		return
	

	# Returns a set of IPv6 addresses found in the html
	def xtractMyipms(self):
		# RegEx
		regex = ("[a-f0-9]{1,4}" + r":" +
				"[a-f0-9]{0,4}" + r":" +
				"[a-f0-9]{0,4}" + r":" +
				"[a-f0-9]{0,4}" + r":" +
				"[a-f0-9]{0,4}" + r":" +
				"[a-f0-9]{0,4}" + r":" +
				"[a-f0-9]{1,4}"
				)
		regex_c = re.compile(regex)

		ip_list = re.findall(regex_c, self.html_content) #list of regex results througth the html				
		return set(ip_list) # as the set can't have dups, this will do the thing...


# Append the set to a file, returns none
def appendIPs(myset, f_name):
	f = open(f_name, 'a')
	for i in myset:
		f.write(i + '\n')
	f.close()
	return

			
if __name__=="__main__":
	url_base = "https://www.myip.ms/browse/comp_ip6/" #1, 2, 3...
	ip_file = 'myipms.txt'
	total_myipms = 20063 #16MAY
	first_page = 48 #16MAY
	last_page = total_myipms
	# Set TOR 			
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
	socket.socket = socks.socksocket
	# Print IP
	curl_out = subprocess.check_output(['curl','icanhazip.com'], shell=False).strip()
	print "Current IP, new IP: " + curl_out
	# Go for it!
	for i in range(first_page, last_page):
		rq = CustomRequest()
		opener = rq.openCon()
		rq.getHTML(opener, url_base + str(i))
		print "Working on page ", i
		# Avoid banning
		if rq.shouldIStop():
			os.system('sudo service tor restart')
			time.sleep(1)
			# Print IP
			curl_out = subprocess.check_output(['curl','icanhazip.com'], shell=False).strip()
			print "TOR restarted, new IP: " + curl_out						
		else:
			appendIPs(rq.xtractMyipms(), ip_file)
		





