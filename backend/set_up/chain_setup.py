from langchain.chains.question_answering import load_qa_chain

class Chain:
    def __init__(self, llm, chain_type, prompt, memory):
        self.llm = llm
        self.chain_type = chain_type
        self.prompt = prompt
        self.memory = memory

    def never_break_the_langchain(self, llm, chain_type, prompt, memory):
        chain = load_qa_chain(llm=self.llm, chain_type=self.chain_type, prompt=self.prompt)
        return chain        