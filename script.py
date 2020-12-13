import time
import urllib

print 'start'
i=0
while i<1000:
	string="C:/Users/Thibaut Wissocq/Desktop/free/file_"+str(i)+".txt"
	page=urllib.urlopen('http://192.168.0.254/pub/fbx_info.txt') 
	strpage=page.read()
	mon_fichier = open(string,'w')
	mon_fichier.write(strpage)
	mon_fichier.close()
	i=i+1
	i%10
	time.sleep(10)
