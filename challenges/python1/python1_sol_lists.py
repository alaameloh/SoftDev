# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:38:34 2018

@author: alaameloh
"""

import sys
from itertools import groupby
from operator import itemgetter
f = open(str(sys.argv[1]))
#f = open("auth.log")
output = list()  # IP, nb_success, nb_users_success, nb_failed, nb_users_failed
raw_data = f.readlines()
for i in range(len(raw_data)):
	if len(raw_data[i].split()) > 10 :
		raw_data[i] = raw_data[i].split()
		raw_data[i]=[raw_data[i][10],raw_data[i][5],raw_data[i][8]]
		
raw_data.sort(key=lambda x : x[0])
#grouping over IPs
for key, group in groupby(raw_data, itemgetter(0)):
	nb_status=0
	#grouping over connection status (failed or success)
	accepted = list()
	failed = list()
	accepted_users = set()
	failed_users = set()
	for key2,group2 in groupby(group, itemgetter(1)):
		nb_status+=1
		for elem in group2:
			if key2 == 'Accepted' : 
				accepted.append(elem[1])
				accepted_users.add(elem[2])
			if key2 == 'Failed' : 
				failed.append(elem[1])
				failed_users.add(elem[2])
	if len(accepted) and len(failed)> len(accepted):
		print(key,'-',len(failed),'failed for',len(failed_users),'users -',len(accepted),'accepted for',len(accepted_users),'users',)	