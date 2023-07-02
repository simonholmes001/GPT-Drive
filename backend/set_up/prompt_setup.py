from langchain.prompts.prompt import PromptTemplate

class Prompt:

    def __init__(self):
        pass

    def set_query(self):
        query="""
        What is a regional compliance officer? 
        Please provide as much information as possible and be VERY COMPLETE with your answer
        """
        return query
    
    def set_prompt_template(self):
        prompt_template = """
            You are an assitant for a large company. The company has many core procedure documents, and you use these core procedure documents
            when answering employee queries. These core procedure docuemnts are provided to you as CONTEXT.
            Please provide as much information as possible.

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