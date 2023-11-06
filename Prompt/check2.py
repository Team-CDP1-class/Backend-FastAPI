# -*- coding: utf-8 -*-
from filtering2 import Filtering2
import json
import re

#def Check2(user_input):
for tries in range(5):
    isFlag = False
    isoverallFlag = False
    alpha = r"[가-힣\s,.]+"

    answer = Filtering2(["""소년은 개울가에서 소녀를 보게 되지만, 말도 제대로 못 붙이는 내성적인 성격이다. 어느 날, 소녀가 그런 소년에게 조약돌을 던져 관심을 나타내고, 소년은 이를 소중히 간직한다. 그러나 소극적으로 소녀를 피하기만 하던 소년은 소녀의 제안으로 함께 산에 놀러 간다. 논밭을 지나 산마루까지 오르면서 아늑하고 평화로운 가을 날의 시골 정취 속에 둘 사이는 더욱 가까워진다. 
                   산을 내려올 때 갑자기 소나기를 만난 소년과 소녀는 원두막과 수숫단 속에서 비를 피한다. 비가 그친 뒤, 돌아오는 길에 도랑물이 불어서 소년은 소녀를 업고 건너며, 둘 사이는 더욱 친밀해진다. 그 후 한동안 만나지 못﻿하다가 다시 소녀를 만난 소년은 소녀의 옷에 진 얼룩을 보고 부끄러워한다. 
                   그리고 소녀는 그 동안 아팠으며, 곧 이사를 가게 되었다는 말을 듣게 된다. 소년은 마지막으로 한 번 소녀를 만나려고 애를 태우다가 소녀가 이사 가기로 한 전날 밤 잠결에 부모의 이야기를 통해 소녀가 죽었으며, 소년과의 추억이 깃든 옷을 그대로 입혀서 묻어 달라는 말을 남겼다는 사실을 알게 된다."""])
    print(answer)
    if("|" not in answer):
        continue

    split_answer = re.split(r"//|\||:|\n", answer)
    a = []
    for x in range(len(split_answer)):
        if(split_answer[x].strip()!="" and split_answer[x].strip()!="\\n"):
            a.append(split_answer[x].strip())
    for x in range(2):
        a.append("")
    print(a)

    stageTreatmentAnalysis = {}
    emotionResult = []
    stageResult = []
    overallResult = []

    for x in range(len(a)-2):
        emotionResultContent = {}
        stageResultContent = {}
        overallResultContent = {}
        if(a[x] == "판단근거"):
            isoverallFlag = True
        if(a[x] =="발단" or a[x] == "전개" or a[x] == "위기" or a[x] == "절정" or a[x] == "결말"):
            if(a[x+2].isdecimal()):
                emotionResultContent['emotion'] = a[x+1]
                emotionResultContent['score'] = int(a[x+2])
                emotionResult.append(emotionResultContent)
                if(len(emotionResult) == 5):
                    for i in range(len(stageResult)):
                        if(a[x] in stageResult[i]['stage']):
                            stageResult[i]['emotionResult'] = emotionResult
                            emotionResult = []
            elif(bool(re.match(alpha, a[x+1]))):
                stageResultContent['stage'] = a[x]
                stageResultContent['summary'] = a[x+1]
                stageResult.append(stageResultContent)
            else:
                isFlag = True
                break
        elif((a[x]=="기쁨" or a[x]=="슬픔" or a[x]=="분노" or a[x]=="불안" or a[x]=="혐오") and isoverallFlag == True):
            if(a[x+1].isdecimal()):
                overallResultContent['emotion'] = a[x]
                overallResultContent['score'] = int(a[x+1])
                overallResultContent['reason'] = a[x+2]
                overallResult.append(overallResultContent)
                if(len(overallResult) == 5):
                    break
            else:
                isFlag =True
                break

    if(isFlag == False and len(stageResult) ==5 and len(stageResult[0]['emotionResult']) == 5 and len(overallResult) == 5):
        print(isFlag, len(stageResult), len(stageResult[0]['emotionResult']), len(overallResult))  
        stageTreatmentAnalysis['stageResult'] = stageResult
        stageTreatmentAnalysis['overallResult'] = overallResult       
        break
    else:
        print(isFlag, len(stageResult), len(overallResult)) 
        

print(stageTreatmentAnalysis)
json_stageTreatmentAnalysis = json.dumps(stageTreatmentAnalysis)

#return json_stageTreatmentAnalysis


