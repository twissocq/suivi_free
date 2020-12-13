i=0
etat = []
protocole = []
mode = [] 
debit = [] 
snr = [] 
atten = []
FEC = []
CRC = []
HEC = []

protocole2 = []
mode2= []
upload= []
download= []
snr_down= []
snr_up= []
atten_down= []
atten_up= []
FEC_down= []
FEC_up= []
CRC_down= []
CRC_up= []
HEC_down= []
HEC_up= []
# 
# protocole2 = ["protocole"]
# mode2= ["mode"]
# upload= ["upload"]
# download= ["donwload"]
# snr_down= ["snr_down"]
# snr_up= ["snr_up"]
# atten_down= ["attenuation descendante"]
# atten_up= ["attenuation montante"]
# FEC_down= ["FEC_download"]
# FEC_up= ["FEC_upload"]
# CRC_down= ["CRC_download"]
# CRC_up= ["CRC_upload"]
# HEC_down= ["HEC_download"]
# HEC_up= ["HEC_upload"]

while i<141:
	string="C:/Users/Thibaut Wissocq/Desktop/free/file_"+str(i)+".txt"
	mon_fichier = open(string,'r')
	for lignes in mon_fichier:
		# print lignes
	#	if "  Etat                           " in lignes:
	#		print str(lignes)
	#		etat.append(str(lignes)
		if "Protocole" in lignes:
			# print str(lignes)
			protocole.append(lignes)
		elif "Mode      " in lignes:
			# print str(lignes)
			mode.append(lignes)
		elif "ATM" in lignes:
			# print str(lignes)
			debit.append(lignes)
		elif "Marge de bruit" in lignes:
			# print str(lignes)
			snr.append(lignes)
		elif "nuation" in lignes:
			# print str(lignes)
			atten.append(lignes)
		elif "FEC" in lignes:
			# print str(lignes)
			FEC.append(lignes)			
		elif "CRC" in lignes:
			# print str(lignes)
			CRC.append(lignes)	
		elif "HEC" in lignes:
			# print str(lignes)
			HEC.append(lignes)
	i+=1



for len in range(1,140):
	str2 = protocole[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	str2.append(" ")
	protocole2.append(str2[1])

	str2 = mode[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	mode2.append(str2[1])
	
	str2 = debit[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	download.append(float(str2[1].rstrip(' kb/s')))
	upload.append(float(str2[2].rstrip(' kb/s')))
	
	str2 = snr[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	snr_down.append(str2[1].rstrip(' dB'))
	snr_up.append(str2[2].rstrip(' dB'))
	
	str2 = atten[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	atten_down.append(str2[1].rstrip(' dB'))
	atten_up.append(str2[2].rstrip(' dB'))
	
	str2 = FEC[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	FEC_down.append(str2[1])
	FEC_up.append(str2[2])
	
	str2 = HEC[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	HEC_down.append(str2[1])
	HEC_up.append(str2[2])
	
	str2 = CRC[len].rstrip('\n').split('  ')
	for i in range(str2.count('')):
		str2.remove('')
	CRC_down.append(str2[1])
	CRC_up.append(str2[2])

liste = [protocole2, mode2, download, upload, snr_down, snr_up, atten_down, atten_up, FEC_down, FEC_up, HEC_down, HEC_up, CRC_down, CRC_up]

import csv

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(liste)


import matplotlib.pyplot as plt
plt.plot(download, 'ro')
plt.show()