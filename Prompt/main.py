from check1 import Check1
from check2 import Check2
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class StorycardRes(BaseModel):
    premise : str
    setting : str
    characters : str
    outline : str

class StoryTreatment(BaseModel):
    contents : str

@app.get("/")
async def root():
    content = {"statusCode": 200, "data": "Hello World"}
    print(content)
    return JSONResponse(status_code=200, content=content, media_type="application/json")

@app.post("/api/analysis/storycard")
async def storycard_analysis(storycard : StorycardRes): 
    #result = Check1([storycard.premise, storycard.setting, storycard.characters, storycard.outline])
    result = {'keywords': [{'keyword': '어린 연인', 'reason': '두 주인공의 나이와 성격'}, {'keyword': '자연', 'reason': '전체적인 설정과 등장인물의 배경'}, {'keyword': '우연', 'reason': '두 주인공의 만남과 이로 인한 갈등'}, {'keyword': '사랑', 'reason': '두 주인공이 서로를 이해하면서 다가가는 과정'}, {'keyword': '가을', 'reason': '시간의 흐름과 배경 설정'}], 'similarStory': [{'title': '봄날은 간다 - 김동인', 'story': '주인공들의 은밀한 사랑', 'similarity': [{'percent': 50, 'reason': '두 주인공의 연령대와 감정의 변화'}, {'percent': 60, 'reason': '자연의 아름다움이 주는 애틋한 느낌'}, {'percent': 80, 'reason': '우연한 만남으로 시작되는 이야기'}, {'percent': 70, 'reason': '두 주인공의 서로에 대한 감정의 변화'}, {'percent': 40, 'reason': '계절감과 이야기의 배경으로 가을이 등장'}]}, {'title': '그리스인 조르바 - 니콜라이 보그다노프', 'story': '자연을 배경으로 한 인간의 감정 이야기', 'similarity': [{'percent': 20, 'reason': '작품의 주요 내용과는 거리가  있음'}, {'percent': 90, 'reason': '작품 전체가 자연을 배경으로 하며, 이를 지속적으로 강조함'}, {'percent': 40, 'reason': '우연한 만남은 없으나, 이를 대체하는 요소가 등장함'}, {'percent': 80, 'reason': '인간의 감정 변화를 주요 내용으로 다룸'}, {'percent': 50, 'reason': '계절감은 미미하게 등장함'}]}, {'title': '안나 카레니나 - 레프 톨스토이', 'story': '주인공 간의 첫 만남과 이를 통한 감정의 발전', 'similarity': [{'percent': 30, 'reason': '두 작품의 차이점이 큼'}, {'percent': 80, 'reason': '인간의 감정을 자연 속에서 다룸'}, {'percent': 70, 'reason': '우연한 만남이 이야기의 전개에 중요한 역할을 함'}, {'percent': 90, 'reason': '인간의 감정 변화를 주요 내용으로 다룸'}, {'percent': 90, 'reason': '이야기의 배 경이 가을로 설정되어 있음'}]}]}
    print("ANALSYS RESULT")
    print(result)

    if result: 
        req = {"statusCode":200, "data": result}
        return JSONResponse(status_code=200, content=req, media_type="application/json")
    else: 
        req = {"statusCode":404, "data": None}
        return JSONResponse(status_code=404, content=req, media_type="application/json")

@app.post("/api/analysis/storytreatment")
async def storytreatrment_analysis(storyTreatment : StoryTreatment):
    result = Check2([storyTreatment.contents])
    print("ANALSYS RESULT")
    print(result)

    if result: 
        req = {"statusCode":200, "data": result}
        return JSONResponse(status_code=200, content=req, media_type="application/json")
    else: 
        req = {"statusCode":404, "data": None}
        return JSONResponse(status_code=404, content=req, media_type="application/json")