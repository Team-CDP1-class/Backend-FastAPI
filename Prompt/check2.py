from filtering2 import Filtering2
import json
import re

'''
answer1 = Filtering1(["어린 마법사 해리포터는 11번째 생일에 자신이 마법사이며 호그와트 마법 학교에 입학했다는 것을 알게 됩니다. 그는 마법 여행을 시작하면서 자신의 과거를 밝혀내고, 한때 부모님을 죽인 어둠의 마법사와 마주하며, 선과 악의 싸움을 벌이는 마법 세계에서 자신의 중요한 역할을 깨닫게 됩니다.",
        "이 이야기는 주로 호그와트 마법 학교에 초점을 맞추고 있는 비마법계와 평행한 마법의 세계를 배경으로 합니다. 스코틀랜드에 위치한 이 학교는 마법에 걸린 복도, 움직이는 계단, 숨겨진 통로, 그리고 마법의 생물들로 가득 차 있습니다. 다른 중요한 장소로는 버로우, 디아곤앨리, 호그스미드, 그리고 금지되는 금단의 숲이 있습니다.",
        """1. 해리는 이마에 번개 모양의 상처를 가진 어린 마법사로, 어린 시절 어둠의 마법사 볼드모트가 공격한 잔해입니다. 그는 마법 세계를 위협하는 어둠의 힘에 맞서 싸우기 위해 노력하는 용기, 충성심, 도덕적 나침반으로 유명합니다.
        2. 헤르미온느는 매우 총명하고 지략이 풍부한 마녀로 지식을 중시하며 항상 배우기를 열망합니다. 그녀는 해리의 가장 가까운 친구 중 한 명이며 해리가 마법의 세계를 항해할 수 있도록 돕는 데 결정적인 역할을 합니다.
        3. 론(Ron)은 해리의 충성스럽고 마음씨 좋은 대규모 마법 가족의 가장 친한 친구입니다. 그는 유머, 용감함, 그리고 그들의 모험 동안 항상 해리의 곁을 지켜주는 변함없는 충성심으로 알려져 있습니다.""",
        """1. 해리포터는 11번째 생일에 자신이 마법사라는 것을 알게 되고 호그와트 마법학교의 열쇠와 땅의 수호자인 해그리드에 의해 마법의 세계에 소개됩니다.
        2. 그는 마법의 기차인 호그와트 급행열차에 탑승하여 호그와트로 향하며, 그곳에서 그리핀도르 하우스로 분류되어 헤르미온느와 론과 강한 유대감을 형성합니다.
        3. 학년 내내 해리는 마법사의 돌 뒤에 숨겨진 미스터리를 풀고 권력으로 돌아가려는 볼드모트의 음모를 발견합니다.
        4. 클라이맥스에서 해리는 볼드모트와 맞서서 그의 계획을 실패시키고 일시적으로 그를 패퇴시키고, 어둠의 마법사와의 전투의 시작을 알립니다.
        """])
print("############################################################################################################")
print(answer1)
print("############################################################################################################")
'''
def Check2(user_input):
    for tries in range(5):
        isFlag = False
        isoverallFlag = False
        alpha = r"[가-힣\s,.]+"

        answer = Filtering2(user_input)
        if("|" not in answer):
            continue
        split_answer = re.split(r"//|\||:|\n", answer)
        a = []
        for x in range(len(split_answer)):
            if(split_answer[x].strip()!=""):
                a.append(split_answer[x].strip())
        a.append("")
        a.append("")

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
                if(a[x+1].isdigit()):
                    overallResultContent['emotion'] = a[x]
                    overallResultContent['score'] = int(a[x+1])
                    overallResultContent['reason'] = a[x+2]
                    overallResult.append(overallResultContent)
                    if(len(overallResult) == 5):
                        break
                else:
                    isFlag =True
                    break
        print(isFlag, len(overallResult), len(stageResult))  
        if(isFlag == False and len(stageResult)==5 and len(overallResult) == 5):
            stageTreatmentAnalysis['stageResult'] = stageResult
            stageTreatmentAnalysis['overallResult'] = overallResult       
            break

    print(stageTreatmentAnalysis)
    json_stageTreatmentAnalysis = json.dumps(stageTreatmentAnalysis)

    return json_stageTreatmentAnalysis

