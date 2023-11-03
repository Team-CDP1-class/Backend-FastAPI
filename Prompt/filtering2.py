import os
from dotenv import load_dotenv
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate


def Filtering2(user_input):
    load_dotenv()

    os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    llm = AzureOpenAI(deployment_name = "gpt35", max_tokens=2500)
    prompt = PromptTemplate(
        input_variables=["treatment"], 
        template="""
        당신은 작가이며, 아래 주어진 원칙을 잘 지켜 답변해야 한다.

        0. 답변은 한글로 하며, 함수 형태로 답변하지 않는다.

        1. 입력글 스토리 트리트먼트(요약)를 단계로 나누어야 한다. 
        형식은 반드시 다음과 같은 Markdown table만으로 작성한다.
        | 단계 | 주요맥락 |
        | --- | ------ |
        1-1. 단계는 스토리의 기본 구조인 발단, 전개, 위기, 절정, 결말 총 5개이다. 
        1-2. 각 단계의 주요 맥락에 대해 서술해야 한다.

        2. 단계별로 모든 평가항목에 대해 감정 스코어(정수 1점~5점)를 매긴다. 
        형식은 반드시 다음과 같은 Markdown table만으로 작성한다.
        | 단계 | 감정 | 스코어 |
        | --- | ------ | ------- |
        2-1. 단계 5개에 감정이 5개이므로 총 5*5 = 25개가 작성되어야 한다.
        2-2. 평가항목은 기쁨, 슬픔, 분노, 불안, 혐오이다.
        기쁨 - 즐겁고 만족스러운 감정으로, 드라마에서는 주인공들이 성공하거나 사랑을 이룰 때 표현된다.
        슬픔 - 안타깝고 우울한 감정으로, 드라마에서는 주인공등이 이별하거나 상처를 입을 때 표현된다.
        분노 - 화를 내고 불쾌한 감정으로, 드라마에서는 주인공들이 배신하거나 억울한 상황에 놓일 때 표현된다.
        불안 - 걱정스럽고 긴장된 감정으로, 드라마에서는 주인공들이 위험한 상황에 놓이거나 미래를 예측할 수 없을 때 표현된다.
        혐오 - 불쾌하고 불쾌한 감정으로, 드라마에서는 주인공들이 불쾌하거나 더러운 상황에 놓일 때 표현된다.

        3. 전체적으로 모든 평가항목에 대해 감정 스코어(정수 1점~5점)를 매긴다. 
        형식은 반드시 다음과 같은 Markdown table만으로 작성한다.
        | 감정 | 스코어 | 판단근거 |
        | --- | ------ | ------- |
        3-1. 평가항목은 2-1과 같지만, 새로 스코어를 매긴다.
        3-2. 스코어 하나마다 정한 판단근거는 판단 근거는 개조식 (글을 쓸 때 짧게 끊어서 중요한 요점이나 단어를 나열하는 방식)으로 1문장 써야한다.

        입력글:{treatment}

        다시 한번 언급하지만, |이 들어간 Markdown table로 작성해야 한다.
        """
    )

    prompt_formatted_str: str = prompt.format(
        treatment=user_input[0],
    )

    return llm.predict(prompt_formatted_str)