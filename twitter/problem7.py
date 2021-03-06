import operator
import csv
import sys
from datetime import datetime, date
hashtag1={}
minDate = datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
maxDate = datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
counter=0
keymarker=''

with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		insertdate=datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y")
		if insertdate<minDate:
			minDate=insertdate
		if insertdate>maxDate:
			maxDate=insertdate
		if row[0] in hashtag1.keys():	
			hashtag1[row[0]]+=1
		else:
			hashtag1[row[0]]=1

keymarker=max(hashtag1.iteritems(), key=operator.itemgetter(1))[0]
print keymarker+' tweeted the most\nDataset range: '+str(minDate.strftime("%B %d %Y, %H:%M:%S"))+' and '+str(maxDate.strftime("%B %d %Y, %H:%M:%S"))	
