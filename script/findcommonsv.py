#!/usr/bin/python

import pandas as pd 
import StringIO 
import collections as cl
import Queue
import sys
import getopt



def findoverlaps(*args):

	
	allpos=sum([sum(x,()) for x in args],())


	allpos_index=sorted(range(len(allpos)), key=lambda x: allpos[x])

	
	allpos_sorted=sorted(allpos)
	
	
	current=0
	
	allgroups=[]
	eachgroup=[]
	
	last_coordi=-10001
	for index,coordi in zip(allpos_index,allpos_sorted):
		
		
		sv_index=index/2
		
		if sv_index*2==index:
			
			if current>0:
				dis=0
			
			else:
				dis=coordi-last_coordi
				
			if dis<=5000:
				
				eachgroup.append(sv_index)
				current=current+1
			
			else:
				
				allgroups.append(eachgroup)
				eachgroup=[sv_index]
				current=1
							
		else:
			
			current=current-1
		
		last_coordi=coordi
		
	allgroups.append(eachgroup)


	
	return allgroups
	


def organize(inputfile):
	
	t=pd.read_csv(inputfile, sep='\s+',names=['SmapEntryID', 'QryContigID', 'RefcontigID1', 'RefcontigID2', 'QryStartPos', 'QryEndPos', 'RefStartPos', 'RefEndPos', 'Confidence', 'Type', 'XmapID1', 'XmapID2', 'LinkID', 'QryStartIdx', 'QryEndIdx', 'RefStartIdx', 'RefEndIdx', 'Zygosity', 'Genotype', 'GenotypeGroup', 'RawConfidence', 'RawConfidenceLeft', 'RawConfidenceRight', 'RawConfidenceCenter'], comment='#')


	t=t.loc[(t['RefcontigID2']<23) & (t['Type']=='deletion')]
	
	chroms=list(t['RefcontigID2'])
	
	starts=[float(x) for x in list(t['RefStartPos'])]

	ends=[float(x) for x in list(t['RefEndPos'])]

	pos=[(min(x),max(x)) for x in zip(starts,ends)]

	
	allchroms=cl.defaultdict(list)
	
	for chrom,posi in zip(chroms, pos):
		
		allchroms[chrom].append(posi) 
		
	return allchroms
		
	

def findcommonsv(*args):
	
	
	num=len(args)

	allchroms_name=set(sum([x.keys() for x in args],[]))
	
	commons=0

	samples=[0 for x in xrange(num-1)]
	for chrom in allchroms_name:
	
		l0=[len(x[chrom]) for x in args]

		l0=[sum(l0[:(i+1)]) for i in xrange(len(l0))]
	
		overlaps=findoverlaps(*tuple([x[chrom] for x in args]))


		indexes=[[len([k for k in l0 if k<=y]) for y in x] for x in overlaps]
		overlap_index=[len(set(x)) for x in indexes]

		if num>=3:
			nocontrol=[x for x in indexes if len(x)>0 and num-1 not in x]
		else:
			nocontrol=[x for x in indexes]


		for i in xrange(num-1):
			samples[i]=samples[i]+len([x for x in nocontrol if i in x])

		commons=commons+len([x for x in nocontrol if len(set(x))==2])

	
	return samples, commons
		


def main(inputfiles):
	
	allchroms=[organize(inputfile) for inputfile in inputfiles]


	results,commons=findcommonsv(*tuple(allchroms))

	print 100*commons/min(results),results,commons


if __name__=='__main__':
	
	inputcontrol=''
	
	opts,args=getopt.getopt(sys.argv[1:],"c:f:")
	
	for op, value in opts:
		
		if op=='-c':
			inputcontrol=value
		if op=='-f':
			inputfiles=value

	inputfiles=(inputfiles+' '+inputcontrol).split()
	
	main(inputfiles)


