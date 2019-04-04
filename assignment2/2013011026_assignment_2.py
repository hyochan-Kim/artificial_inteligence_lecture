# -*- coding: utf-8 -*-

import math
from konlpy.tag import Okt


okt=Okt() # konlpy를 태그별로 분류할 때 twitter로 했더니 ubuntu에서 okt로 하라고 하여 Okt로 하였습니다.
bad_Noun={} #dictionary를 이용하여 명사 형용사 동사를 {'단어',사용 횟수}의 식으로 저장하였습니다.
good_Noun={}
bad_Adjective={}
good_Adjective={}
bad_Verb={}
good_Verb={}
sum_good_Noun=0 #사용된 명사, 형용사, 동사의 수인데, 만족한 사람과 불만족의 사람으로 나누었습니다.
sum_good_Adjective=0
sum_good_Verb=0
sum_bad_Noun=0
sum_bad_Adjective=0
sum_bad_Verb=0

fr=open("ratings_train.txt","r") #파일을 열고
line = fr.readline() #쓰이지 않는 첫번째 줄을 읽고
lines = fr.readlines() #두번째 줄부터 몽땅 읽어온 후
fr.close()
for line in lines: #줄을 나누어 for문을 돌렸습니다.
	tokens = okt.pos(line)
	if (tokens[len(tokens)-2][0]=='0'): #해당 줄이 만족인지 아닌지를 확인하여 경우를 나누었고
		for (first,second) in tokens :
			if second=='Noun' : #품사가 명사일 경우, 
				sum_bad_Noun+=1 #불만족 명사의 수를 늘리고
				if first in bad_Noun.keys() : #해당하는 단어에 대한 dict가 있다면 
					bad_Noun[first]+=1 #사용 횟수를 1 늘리고,
				else : #없다면
					bad_Noun[first]=1 #dict를 새로 추가해주는 식입니다.
				
		
			if second=='Adjective' :
				sum_bad_Adjective+=1
				if first in bad_Adjective.keys() :
					bad_Adjective[first]+=1
				else :
					bad_Adjective[first]=1
				
			if second=='Verb' :
				sum_bad_Verb+=1
				if first in bad_Verb.keys() :
					bad_Verb[first]+=1
				else :
					bad_Verb[first]=1
	
	
	
	if (tokens[len(tokens)-2][0]=='1'):
		for (first,second) in tokens :
			if second=='Noun' :
				sum_good_Noun+=1
				if first in good_Noun.keys() :
					good_Noun[first]+=1
				else :
					good_Noun[first]=1
				
		
			if second=='Adjective' :
				sum_good_Adjective+=1
				if first in good_Adjective.keys() :
					good_Adjective[first]+=1
				else :
					good_Adjective[first]=1
				
			if second=='Verb' :
				sum_good_Verb+=1
				if first in good_Verb.keys() :
					good_Verb[first]+=1
				else :
					good_Verb[first]=1


#이렇게 만족 불만족별 단어 사용 통계를 구한 후,

fr=open("ratings_test.txt","r")

line = fr.readline()
lines = fr.readlines()
fr.close()

fw=open("ratings_result.txt","w")
fw.write(line)

for line in lines:
	line = line[0:len(line)-1]
	fw.write(line)
	tokens = okt.pos(line)
	p1=0 #각 문장에 대한 만족 확률과
	p2=0 #불만족 확률인데, 분모가 너무 커져서 0이되는 언더플로우를 막기 위하여 log를 이용하여, 초기값이 1이 아닌 0입니다.
	for (first,second) in tokens :
		good=0
		bad=0;
		if second=='Noun' : #test하는 문장의 단어가 명사이면서
			if first in good_Noun.keys() : #그 단어가 기존에 좋은 단어로 쓰인 적이 있으면
				good=good_Noun[first]  #그 사용 횟수를 good에 저장.
			if first in bad_Noun.keys() :  #마찬가지로 불만족 단어로 쓰인 적이 있으면
				bad=bad_Noun[first]    #그 사용 횟수를 bad에 저장.
			if(good!=0 and bad!=0) : #매 단어마다 0이 아닌 경우로 분류를 하여, 확률값 p1,p2에 곱해(해당 식은 log이므로 +입니다)주어 naive bayes classfication을 위한 수식을 구함.
				p1 += math.log2(good/sum_good_Noun)
				p2 += math.log2(bad/sum_bad_Noun)
			if(good==0 and bad!=0) :
				p1 += math.log2(1/sum_good_Noun)
				p2 += math.log2(bad/sum_bad_Noun)
			if(good!=0 and bad==0) :
				p1 += math.log2(good/sum_good_Noun)
				p2 += math.log2(1/sum_bad_Noun)
			
				
			
		if second=='Adjective' :
			if first in good_Adjective.keys() :
				good=good_Adjective[first]
			if first in bad_Adjective.keys() :
				bad=bad_Adjective[first]
			if(good!=0 and bad!=0) :
				p1 += math.log2(good/sum_good_Adjective)
				p2 += math.log2(bad/sum_bad_Adjective)
			if(good==0 and bad!=0) :
				p1 += math.log2(1/sum_good_Adjective)
				p2 += math.log2(bad/sum_bad_Adjective)
			if(good!=0 and bad==0) :
				p1 += math.log2(good/sum_good_Adjective)
				p2 += math.log2(1/sum_bad_Adjective)
			

		if second=='Verb' :
			if first in good_Verb.keys() :
				good=good_Verb[first]
			if first in bad_Verb.keys() :
				bad=bad_Verb[first]
			if(good!=0 and bad!=0) :
				p1 += math.log2(good/sum_good_Verb)
				p2 += math.log2(bad/sum_bad_Verb)
			if(good==0 and bad!=0) :
				p1 += math.log2(1/sum_good_Verb)
				p2 += math.log2(bad/sum_bad_Verb)
			if(good!=0 and bad==0) :
				p1 += math.log2(good/sum_good_Verb)
				p2 += math.log2(1/sum_bad_Verb)
	
	goodp=(sum_good_Noun+sum_good_Adjective+sum_good_Verb)/(sum_good_Noun+sum_good_Adjective+sum_good_Verb+sum_bad_Noun+sum_bad_Adjective+sum_bad_Verb) # 구해진 확률에 전체 단어 중 만족 단어의 비율을 구해주고,
	badp=(sum_bad_Noun+sum_bad_Adjective+sum_bad_Verb)/(sum_good_Noun+sum_good_Adjective+sum_good_Verb+sum_bad_Noun+sum_bad_Adjective+sum_bad_Verb)
	p1 += math.log2(goodp) #이를 확률로 더해준 후
	p2 += math.log2(badp)
	if p1 >= p2 : #원래 식은 p1/(p1+p2) >= 1/2 이나, 이 수식은 log로 진행할 시에, 분모가 0이될 우려 또는 부호에 의해 부등호가 바뀔 우려가 있어서, 해당 식을 풀이한 p1>=p2로 진행함.
		fw.write(" 1\n")
	if p1 < p2 :
		fw.write(" 0\n")


fw.close() # 파일을 닫음
