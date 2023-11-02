import os
from dotenv import load_dotenv
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def Filtering_Chat2(user_input):
    load_dotenv()

    os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    sys_prompt = PromptTemplate(
        input_variables=["treatment"], 
        template="""
        당신은 작가이며, 아래 주어진 원칙을 잘 지켜 답변해야 한다.

        0. 답변은 한글로 한다.

        1. 입력글 스토리 트리트먼트(요약)를 단계로 나누어야 한다. 
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        | 단계 | 주요맥락  |
        | --- | ------ |
        1-1. 단계는 스토리의 기본 구조인 발단, 전개, 위기, 절정, 결말 총 5개이다. 
        1-2. 각 단계의 주요 맥락에 대해 서술해야 한다.

        2. 단계 별로 감정 스코어(1~5점)를 매긴다. 
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        | 단계 | 감정  | 스코어 |
        | --- | ------ | ------- |
        2-1. 단계 5개와 감정 5개이므로 총 25개가 작성되어야 한다.
        2-1. 평가항목은 행복, 슬픔, 분노, 두려움, 불안, 혐오이다.
        기쁨 (Joy) - 즐겁고 만족스러운 감정으로, 드라마에서는 주인공들이 성공하거나 사랑을 이룰 때 표현된다.
        슬픔 (Grief) - 안타깝고 우울한 감정으로, 드라마에서는 주인공등이 이별하거나 상처를 입을 때 표현된다.
        분노 (Anger) - 화를 내고 불쾌한 감정으로, 드라마에서는 주인공들이 배신하거나 억울한 상황에 놓일 때 표현된다.
        불안 (Anxiety) - 걱정스럽고 긴장된 감정으로, 드라마에서는 주인공들이 위험한 상황에 놓이거나 미래를 예측할 수 없을 때 표현된다.
        혐오 (Disgust) - 불쾌하고 불쾌한 감정으로, 드라마에서는 주인공들이 불쾌하거나 더러운 상황에 놓일 때 표현된다.


        3. 전체적인 감정 스코어(1~5점)를 매긴다. 
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        |감정 | 스코어  | 판단근거 |
        | --- | ------ | ------- |
        3-1. 평가항목은 2-1과 같다.
        3-2. 스코어 하나마다 판단 근거는 개조식 (글을 쓸 때 짧게 끊어서 중요한 요점이나 단어를 나열하는 방식)으로 1문장 써야한다.
        
        입력글:{treatment}
        """
    )
    
     # )
    system_message_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)

    storyteller_prompt: PromptTemplate = PromptTemplate(
        input_variables=["treatment"], 
        template="{treatment}을 가지고 딱 정해진 답변만 해줘"
    )
    storyteller_message_prompt = HumanMessagePromptTemplate(prompt=storyteller_prompt)

    chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, storyteller_message_prompt])

    # create the chat model
    chat_model: AzureOpenAI = AzureOpenAI(deployment_name = "gpt35", max_tokens=3000)

    # Create the LLM chain
    chain: LLMChain = LLMChain(llm=chat_model, prompt=chat_prompt)

    prediction_msg: dict = chain.run(
        treatment=user_input[0],
    )

    return prediction_msg