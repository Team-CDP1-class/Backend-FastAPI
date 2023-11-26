# -*- coding: utf-8 -*-
from filtering2 import Filtering2
import json
import re

def Check2(user_input):
    for tries in range(5):
        isFlag = False
        isoverallFlag = False
        alpha = r"[가-힣\s,.]+"

        answer = Filtering2([user_input[0]])
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
    return stageTreatmentAnalysis


