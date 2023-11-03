# -*- coding: utf-8 -*-
from filtering1 import Filtering1
import json
import re

#def Check1(user_input):
for tries in range(5):
    isFlag = False
    alpha = r"[가-힣\s,.'-]+"
    decimal = r"[0-9%]+"
    literal = r"[\"가-힣0-9a-zA-Z\s,.()'-]+"
    answer = Filtering1(["소년과 소녀의 운명을 연결하는 우연한 만남과 갈등",
        "한 시골 마을, 개울가와 산, 가을 계절",
        """1. 소년 (내성적이고 소극적)
           2. 소녀 (행동적이고 활발)
           3. 소년의 부모 """,
        """1. 소년과 소녀는 우연한 만남으로 개울가에서 처음 마주침.
           2. 소녀는 소년에게 조약돌을 던져 관심을 표현하고, 소년은 그를 소중히 간직함.
           3. 소년은 소녀와 함께 산에 놀러 가는 제안을 받아들임.
           4. 두 사람은 산을 오르며 더 가까워짐.
           5. 소나기를 만나 원두막에서 시간을 보내며 더 친밀해짐.
        """])
    print(answer)
    if("|" not in answer ):
         continue
    
    split_answer = re.split(r"//|\||:|\n", answer)
    a = []
    for x in range(len(split_answer)):
        if(split_answer[x].strip()!="" and split_answer[x].strip()!="\\n"):
            a.append(split_answer[x].strip())
    for x in range(8):
        a.append("")
    print(a)

    storyCardAnalysis = {}
    keywords = []
    similarStory = []
    similarity = []

    for x in range(len(a)-8):
        print(x, a[x])
        if(a[x]=="키워드"):
            for i in range(0,10,2):
                if(bool(re.match(alpha, a[x+4+i])) and bool(re.match(alpha, a[x+4+(i+1)])) ):
                    keywordsContent = {}
                    keywordsContent['keword'] = a[x+4+i]
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
                    print(x, i)
                    isFlag = True
                    break
    if(isFlag == False and len(keywords) == 5 and len(similarStory) == 3 and len(similarStory[2]['similarity']) == 5):
        print(isFlag, len(keywords), len(similarStory), len(similarStory[0]['similarity']))
        storyCardAnalysis['keywords'] = keywords
        storyCardAnalysis['similarStory'] = similarStory
        break
    else:
        print(isFlag, len(keywords), len(similarStory))

print(storyCardAnalysis)  
json_storyCardAnalysis = json.dumps(storyCardAnalysis)
#return json_storyCardAnalysis