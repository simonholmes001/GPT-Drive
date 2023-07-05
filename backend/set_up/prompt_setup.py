from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class Prompt:
    def __init__(self):
        pass
    def set_query(self):
        query="""
        Who approved for the FCP document on Gifts and Entertainment?
        """
        return query
    def set_prompt_template(self):
        prompt_template = """
            You are an assitant for a large company. The company has many core procedure documents, and you use these core procedure documents
            when answering employee queries. These core procedure docuemnts are provided to you as CONTEXT.


            If you do not know the answer, just say I do not knowm DO NOT TRY AND MAKE THINGS UP!
            
            Use bullet points as much as possible.
            
            ---------------------------------------------------------
            CONTEXT: {context}
            ---------------------------------------------------------
            
            Question: {question}
            Lets think step by step before each answer. In your answer, provide references for all pdf documents that are 
            used to reply to the question: ANSWER"""
        return prompt_template
    def set_template_structure(self, prompt_template):
        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
            )
        return prompt

class ChatModelPrompt:
    def __init__(self):
        pass
    def set_few_shot_prompt(self):
        example_human = SystemMessagePromptTemplate.from_template(
            "Am I allowed to fly business class?", additional_kwargs={"name": "example_user"}
        )
        example_ai = SystemMessagePromptTemplate.from_template(
            """
            Based on the provided context, here is the answer to the question "Am I allowed to fly business class?" with references to the relevant documents:

            1. General Rule: Economy class is the standard for all flights (restrictive bookings) (5.2 Airline Class of Service)
            - Reference: Document 5.2 Airline Class of Service

            2. Exceptions for Senior Managers for long haul international flights longer than 6 hours:
            - Business class is allowed for former Senior Managers for long haul international flights longer than 6 hours (5.2 Airline Class of Service)
            - Reference: Document 5.2 Airline Class of Service

            3. Special circumstances with authorization of the relevant EVP:
            - Business class may be allowed for Senior Managers in rare circumstances when it is cheaper than Economy Class or premium economy for long haul (Context)
            - Business class may be allowed if it is the only remaining class available on a flight and the travel is urgent to support operational issues (Quality issue, mandatory last-minute customer meeting) (Context)
            - Reference: Context

            4. Specific rules defined by EVPs:
            - EVPs may define more specific rules within their unit (Context)
            - When those rules are less stringent than the general rule, all flying requests will have to be validated by the EVP (Context)
            - Reference: Context

            5. Prohibited travel options:
            - First-class travel is prohibited (Context)
            - Chartered flights and blacklisted airlines are prohibited (Context)
            - Reference: Context

            In summary, whether you are allowed to fly business class depends on your role and the specific circumstances. As a general rule, economy class is the standard for all flights. However, for long haul international flights longer than 6 hours, former Senior Managers may be allowed to fly business class. There may also be exceptions and specific rules defined by EVPs. It is important to refer to the relevant documents and consult with your line manager or the corporate mandated travel agency for further clarification and approval.

            References:
            - Document 5.2 Airline Class of Service
            - Context
            """, additional_kwargs={"name": "example_assistant"}
                    )
        return example_human, example_ai
    def set_prompt_structure(self, query, template, example_human, example_ai):
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = query
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, example_human, example_ai, human_message_prompt]
        )

        return chat_prompt

class SelectorPrompt:
    def __init__(self):
        pass

    def set_synopsis_chain(self):
        template = """
            You are an analyst who analysis in-coming user requests and then filters the request to the appropriate service,
            to get the best possible reply to the users' question. 

            Given the subject of the user's request, it is your job to pass this request / question on to the next appropriate service.

            Subject: {subject}
            Available Services: {services}
            Analyst: The best possible service from the list of available {serivces} concernign this {subject} is as follows:
        """
        llm = OpenAI(temperature=0.3)
        prompt_template = PromptTemplate(input_variables=["subject", "services"], template=template)
        synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="service")

        return synopsis_chain