import os
from dotenv import load_dotenv
import langchain
import openai
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def Filtering(user_input):
    load_dotenv()

    os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    sys_prompt = PromptTemplate(
        input_variables=["premise", "setting","characters","outline"], 
        template="""
        당신은 작가이며, 아래 주어진 원칙을 잘 지켜 답변해야 합니다.

        0. 답변은 한글로 합니다.

        1. 입력 전제, 설정, 등장인물, 개요와 관련 있는 키워드를 정해야 합니다.
        1-1. 키워드는 1문장으로 총 5개를 나열해야 합니다.
        1-2. 키워드 하나마다 정한 판단 근거가 필요합니다.
        1-3. 입력에 적혀 있지 않는 내용을 키워드로 정하지 않습니다.
        1-4. 키워드의 예시는 '아버지의 불륜','실패의 중요성','정치 부패에 대한 사회적 메시지', '인간관계에 대한 고민' 이 있습니다.
        1-5. 키워드는 주제, 교훈, 흐름, 분위기, 결말 등 다양한 내용이 될 수 있습니다.


        2. 키워드와 대체적으로 관련 있는 문학을 정해야 합니다.
        2-1. 문학은 총 3개가 작성되어야 합니다.
        2-2. 문학 하나마다 정한 판단 근거가 필요합니다.

        3. 키워드 하나마다 2번에서 정한 모든 문학과의 유사도를 백분율로 정해야합니다.
        3-1. 키워드 5개와 문학 3개이므로 총 15개의 유사도가 필요합니다.
        3-2. 유사도 하나마다 판단 근거가 필요합니다.
                
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
        template="{premise}, {setting}, {characters}, {outline}을 가지고 판단해서 답변을 해줘!"
    )
    storyteller_message_prompt = HumanMessagePromptTemplate(prompt=storyteller_prompt)

    chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, storyteller_message_prompt])

    # create the chat model
    chat_model: AzureOpenAI = AzureOpenAI(deployment_name = "gpt35", max_tokens=2000)

    # Create the LLM chain
    chain: LLMChain = LLMChain(llm=chat_model, prompt=chat_prompt)

    prediction_msg: dict = chain.run(
        premise=user_input[0],
        setting=user_input[1],
        characters=user_input[2],
        outline=user_input[3]
    )

    print("#######################################")
    print(prediction_msg)
    print("#######################################")

    return ""