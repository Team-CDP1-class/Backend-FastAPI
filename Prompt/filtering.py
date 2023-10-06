import os
import sys
import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def Filtering(user_input):
    os.environ['OPENAI_API_KEY'] = ""
    llm = OpenAI(temperature=0.1)
    
    prompt = PromptTemplate(
        input_variables=["premise", "setting","characters","outline"], 
        template="""당신은 작가이며, 아래 주어진 원칙을 잘 지켜 답변해야 합니다.

        0. 답변은 한글로 한다.

        1. 입력 전제, 설정, 등장인물, 개요와 관련 있는 키워드를 정해야 합니다.
        1-1. 키워드는 1문장으로 총 5개를 나열해야 한다.
        1-2. 키워드 하나마다 정한 판단 근거가 필요하다.
        1-3. 입력에 적혀 있지 않는 내용을 키워드로 정하지 아니한다.
        1-4. 키워드의 예시는 '아버지의 불륜','실패의 중요성','정치 부패에 대한 사회적 메시지', '인간관계에 대한 고민' 이 있다.
        1-5. 키워드는 주제, 교훈, 흐름, 분위기, 결말 등 다양한 내용이 될 수 있다.


        2. 키워드와 대체적으로 관련 있는 문학을 정해야 합니다.
        2-1. 문학은 총 3개가 작성되어야 한다.
        2-2. 문학 하나마다 정한 판단 근거가 필요하다.

        3. 키워드 하나마다 2번에서 정한 모든 문학과 유사도를 백분율로 정해야합니다.
        3-1. 키워드 5개와 문학 3개이므로 총 15개의 유사도가 필요하다.
        3-2. 유사도 하나마다 판단 근거가 필요하다.
                
        전제: {premise}
        설정: {setting}
        등장인물: character Portrait
        {characters}
        개요: outline the main plot points of the story.
        {outline}
        """
    )
    memory=ConversationBufferMemory()
    # memory = ConversationKGMemory(llm=llm)
    # memory.save_context
    # ({"input":
    #     ["새로운 법학 졸업생은 직업을 시작하기 위해 집으로 돌아왔지만, 부서진 사법 체계와 싸웁니다.",
    #     "그 이야기는 미국의 작은 마을을 배경으로 합니다.",
    #     "characters: 1.리자 터너(Liza Turner)는 22살의 여성입니다. 2.페이튼 터너(Peyton Turner)는 리자(Liza)의 누나입니다",
    #     "outline: 1. 라이즈 터너는 로스쿨을 졸업합니다. 2.그녀는 그녀의 직업을 시작하기 위해 고향으로 돌아옵니다. 3.그녀는 망가진 사법 체계의 현실과 싸웁니다."]},
            
    # {"output":"""
    #     1. 키워드와 판단 근거:

    #     (1) 법학 졸업과 진로 시작에 대한 도전 (Law Career Struggles)
    #     근거: 주어진 premise와 outline에 따르면, 주인공 Liza가 법학 졸업 후 고향으로 돌아가 법조인으로서의 경력을 시작하면서 직면하는 어려움이 핵심적인 플롯 포인트임.

    #     (2) 작은 미국 마을에서의 이야기 (Small Town Narrative)
    #     근거: 설정이 미국의 작은 마을로 주어졌으며, 이곳에서 법조인으로서의 경력 시작과 이에 따른 고민이 전개됨.

    #     (3)자매 간의 인간관계 (Sisterly Relationship)
    #     근거: 주인공 Liza의 언니인 Peyton Turner가 캐릭터로 주어졌으며, 이들 간의 인간관계가 중요한 플롯 포인트로 다뤄질 것으로 예상됨.

    #     (4)부패한 법체계에 대한 심각한 문제의식 (Awareness of Corrupt Justice System)
    #     근거: 주어진 premise에서 법체계의 문제에 대한 심각한 어려움을 겪는 것이 강조되어 있으므로, 이러한 문제에 대한 인식과 대응이 흐름의 핵심이 될 것임.

    #     (5)도전과 성장의 과정 (Journey of Challenge and Growth)
    #     근거: 주인공 Liza가 법조인으로서의 경력을 시작하며 직면하는 어려움을 극복하고 成長 (성장)하는 과정이 주요 흐름임.

    #     2. 관련 문학:

    #     (1)도전과 정의에 대한 사회적 비판을 다룬 '그랩 더 돈' (Grab the Money)
    #     근거: '그랩 더 돈'은 법조인의 도전과 부패한 사회체계에 대한 비판을 주제로 다룸.

    #     (2)작은 공동체에서 벌어지는 인간 이야기 '데드 엔드 타운' (Dead End Town)
    #     근거: '데드 엔드 타운'은 작은 마을의 고립된 환경에서 벌어지는 인간 이야기를 다루고 있음.

    #     (3)자매 간의 복잡한 관계를 풀어내는 '손목에 묶인 유대' (Ties Bound on the Wrist)
    #     근거: '손목에 묶인 유대'는 가족 간의 관계와 도전을 주제로 다루며, 자매 간의 인간관계를 중심으로 풀어내고 있음.
        
    #     3. 유사도와 판단 근거 :

    #     (1)법학 졸업과 진로 시작에 대한 도전 (Law Career Struggles)

    #     '그랩 더 돈'과 유사한 점: 주인공의 법조인으로서의 도전과 어려움을 다룸. 70%
    #     '데드 엔드 타운'과 유사한 점: 작은 마을에서 법조인으로서의 진로 시작에 대한 어려움을 다룸. 60%
    #     '손목에 묶인 유대'와 유사한 점: 주인공의 진로에 대한 도전과 자매 간의 관계를 다룸. 50%

    #     (2)작은 미국 마을에서의 이야기 (Small Town Narrative)

    #     '그랩 더 돈'과 유사한 점: 작은 마을의 고립된 환경에서 벌어지는 이야기를 다룸. 80%
    #     '데드 엔드 타운'과 유사한 점: 작은 마을의 설정과 관련된 이야기를 중점으로 다룸. 90%
    #     '손목에 묶인 유대'와 유사한 점: 작은 마을에서의 인간관계를 중심으로 다룸. 70%

    #     (3)자매 간의 인간관계 (Sisterly Relationship)

    #     '그랩 더 돈'과 유사한 점: 자매 간의 복잡한 관계를 다루며, 이에 대한 해결을 시도함. 75%
    #     '데드 엔드 타운'과 유사한 점: 작은 마을에서의 인간관계 중 자매 간의 관계를 중심으로 다룸. 70%
    #     '손목에 묶인 유대'와 유사한 점: 주인공의 자매와의 관계에 중점을 두고 다룸. 90%

    #     (4)부패한 법체계에 대한 심각한 문제의식 (Awareness of Corrupt Justice System)

    #     '그랩 더 돈'과 유사한 점: 부패한 법체계에 대한 심각한 문제의식을 갖고, 이를 해결하려고 시도함. 80%
    #     '데드 엔드 타운'과 유사한 점: 법체계의 문제에 대한 인식을 갖고, 작은 마을에서 이를 해결하려는 시도를 함. 70%
    #     '손목에 묶인 유대'와 유사한 점: 부패한 법체계에 대한 인식과 이에 대한 대응을 다루며, 이를 통해 자매 간의 관계도 발전시킴. 60%
        
    #     (5)도전과 성장의 과정 (Journey of Challenge and Growth)

    #     '그랩 더 돈'과 유사한 점: 주인공의 도전과 성장 과정을 다룸. 90%
    #     '데드 엔드 타운'과 유사한 점: 작은 마을에서의 어려움을 극복하며 성장하는 과정을 다룸. 80%
    #     '손목에 묶인 유대'와 유사한 점: 주인공의 도전과 성장 과정을 자매 간의 관계와 연결지어 다룸. 85%
    #     """})
    print(*memory)
    conversation_with_kg = ConversationChain(
        llm=llm,
        verbose=True,
        prompt=prompt,
        memory=memory
    )

    return conversation_with_kg.predict(input=user_input)