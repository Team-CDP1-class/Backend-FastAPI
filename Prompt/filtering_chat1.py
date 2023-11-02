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


def Filtering_Chat1(user_input):
    load_dotenv()

    os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    sys_prompt = PromptTemplate(
        input_variables=["premise", "setting","characters","outline"], 
        template="""
        당신은 작가이며, 아래 주어진 원칙을 잘 지켜 답변해야 한다.

        0. 답변은 한글로 한다.

        1. 입력 premise, setting, characters, outline와 관련 있는 키워드를 정해야 한다.
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        | 키워드 | 판단근거 |
        | --- | ------ |
        1-1. 키워드는 5단어 이내로 조합하여 총 5개가 작성되어야 한다.
        1-2. 키워드 하나마다 정한 판단근거는 개조식 (글을 쓸 때 짧게 끊어서 중요한 요점이나 단어를 나열하는 방식)으로 1문장 써야한다.
        1-3. 키워드의 예시는 '아버지의 불륜','실패의 중요성','정치 부패에 대한 사회적 메시지', '인간관계에 대한 고민' 이 있다.
        1-4. 키워드는 주제, 교훈, 흐름, 분위기, 결말 등 다양한 내용이 될 수 있지만, 어느 문학에나 적용되는 추상적인 키워드를 정해서는 안 된다.


        2. 키워드와 전체적으로 관련 있는 문학을 정해야 한다.
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        | 문학 | 판단근거 |
        | --- | ------ |
        2-1. 문학은 총 3개가 작성되어야 한다.
        2-2. 문학 하나마다 정한 판단근거는 개조식 (글을 쓸 때 짧게 끊어서 중요한 요점이나 단어를 나열하는 방식)으로 1문장 써야한다.

        3. 키워드와 모든 문학과의 유사도를 백분율(정해진 수를 100의 비율로 나타내는 것)로 정해야 한다.
        형식은 반드시 다음과 같은 1개의 Markdown table만으로 작성한다.
        | 키워드 | 유사 문학 | 유사도 | 판단근거 |
        | ---- | --- | ---- | ------ |
        3-1. 키워드 5개에 문학이 3개이므로 총 5*3=15개가 작성되어야 한다.
        3-2. 유사도 하나마다 정한 판단근거는 개조식 (글을 쓸 때 짧게 끊어서 중요한 요점이나 단어를 나열하는 방식)으로 1문장 써야한다.
        3-3. 유사도는 '키워드 1("")과 문학 1("")과의 유사도 : 60%','키워드 1("")과 문학 2("")과의 유사도: 50%', '키워드 1("")과 문학 3("")과의 유사도 : 40%', '키워드 2("--")과 문학 1("--")과의 유사도 : 90%', '키워드 2("--")과 문학 2("--")과의 유사도 : 50%', '키워드 2("--")과 문학 3("--")과의 유사도 : 80%' 형태로 출력되어야 한다.  

        전제: {premise}
        설정: {setting}
        등장인물: character Portrait
        {characters}
        개요: outline the main plot points of the story.
        {outline}
        """
    )
    
     # )
    system_message_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)

    storyteller_prompt: PromptTemplate = PromptTemplate(
        input_variables=["premise", "setting", "characters", "outline"], 
        template="{premise}, {setting}, {characters}, {outline}을 가지고 작가라는 원칙에 맞게 대답해줘"
    )
    storyteller_message_prompt = HumanMessagePromptTemplate(prompt=storyteller_prompt)

    chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, storyteller_message_prompt])

    # create the chat model
    chat_model: AzureOpenAI = AzureOpenAI(deployment_name = "gpt35", max_tokens=3000)

    # Create the LLM chain
    chain: LLMChain = LLMChain(llm=chat_model, prompt=chat_prompt)

    prediction_msg: str = chain.run(
        premise=user_input[0],
        setting=user_input[1],
        characters=user_input[2],
        outline=user_input[3]
    )

    return prediction_msg