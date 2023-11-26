# -*- coding: utf-8 -*-
from filtering1 import Filtering1
import json
import re

def Check1(user_input):
    for tries in range(5):
        isFlag = False
        alpha = r"[가-힣\s,.'-]+"
        decimal = r"[0-9%]+"
        literal = r"[\"가-힣0-9a-zA-Z\s,.()'-]+"
        answer = Filtering1([user_input[0], user_input[1], user_input[2], user_input[3]])
        if("|" not in answer ):
            continue
        
        split_answer = re.split(r"//|\||:|\n", answer)
        a = []
        for x in range(len(split_answer)):
            if(split_answer[x].strip()!="" and split_answer[x].strip()!="\\n"):
                a.append(split_answer[x].strip())
        for x in range(8):
            a.append("")
        #print(a)

        storyCardAnalysis = {}
        keywords = []
        similarStory = []
        similarity = []

        for x in range(len(a)-8):
            #print(x, a[x])
            if(a[x]=="키워드"):
                for i in range(0,10,2):
                    if(bool(re.match(alpha, a[x+4+i])) and bool(re.match(alpha, a[x+4+(i+1)])) ):
                        keywordsContent = {}
                        keywordsContent['keyword'] = a[x+4+i]
                        keywordsContent['reason'] = a[x+5+i]
                        keywords.append(keywordsContent)
                    else:
                        isFlag = True
                        break 
            elif(a[x]=="문학작품"):
                for i in range(0,6,2):
                    if(bool(re.match(literal, a[x+4+i])) and bool(re.match(literal, a[x+4+(i+1)])) ):
                        similarStoryContent = {}
                        similarStoryContent['title'] = a[x+4+i]
                        similarStoryContent['story'] = a[x+5+i]
                        similarStory.append(similarStoryContent)
                    else:
                        isFlag = True
                        break
            elif(a[x]=="문학작품 이름"):
                for i in range(0,60,4):
                    if(bool(re.match(literal, a[x+8+i])) and bool(re.match(alpha, a[x+8+(i+1)])) and bool(re.match(decimal, a[x+8+(i+2)])) and bool(re.match(alpha, a[x+8+(i+3)]))):
                        similarContent = {}
                        similarContent['percent'] = int(a[x+8+(i+2)].replace("%",""))
                        similarContent['reason'] = a[x+8+(i+3)]
                        similarity.append(similarContent)
                        if(len(similarity) == 5):
                            for j in range(len(similarStory)):
                                if(a[x+8+i] in similarStory[j]['title']):
                                    similarStory[j]['similarity'] =  similarity
                                    similarity = []
                    else:
                        #print(x, i)
                        isFlag = True
                        break
        if(isFlag == False and len(keywords) == 5 and len(similarStory) == 3 and len(similarStory[2]['similarity']) == 5):
            #print(isFlag, len(keywords), len(similarStory), len(similarStory[0]['similarity']))
            storyCardAnalysis['keywords'] = keywords
            storyCardAnalysis['similarStory'] = similarStory
            break
        #else:
            #print(isFlag, len(keywords), len(similarStory))
    return storyCardAnalysis