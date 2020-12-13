import time
import urllib2
import re
import copy

#Pas de temps en sec
step = 30
#Duree totale de l'analyse en sec
duree = 18000

suivi = open("suivifree.txt", "a")
suivi.write("Date - Protocole - Debit (kb/s) - SNR(dB) - attenuation(dB)- FEC - CRC - HEC \n")# % (date, debit))#, snr, FEC, CRC, HEC))
suivi.close

print 'Debut'
i=0
while i <duree/30:
	brut = urllib2.urlopen('http://192.168.0.254/pub/fbx_info.txt') 
	contenu = brut.read()
	debit = re.search(".*ATM.*", contenu).group().split()[2] 
	prot = re.search(".*Protocole.*", contenu).group().split()
	prot.append('')
	protocole = prot[1]
	snr = re.search(".*Marge de bruit.*", contenu).group().split()[3] 
	attenuation	= re.search(".*nuation.*", contenu).group().split()[1] 
	FEC = re.search(".*FEC.*", contenu).group().split()[1] 
	CRC = re.search(".*CRC.*", contenu).group().split()[1] 
	HEC = re.search(".*HEC.*", contenu).group().split()[1] 
	date = time.strftime("%c")#"%Y %m %d %H %%http %M %S")

	suivi = open("suivifree.txt", "a")
	suivi.write("%s - %s - %s - %s - %s - %s - %s - %s\n" % (date, protocole, debit, snr, attenuation, FEC, CRC, HEC))
	suivi.close
	time.sleep(step)
	i+=1
print("Fin")