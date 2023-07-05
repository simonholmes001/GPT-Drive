from langchain.chains.question_answering import load_qa_chain

class Chain:
    def __init__(self, llm, chain_type, prompt):
        self.llm = llm
        self.chain_type = chain_type
        self.prompt = prompt

    def never_break_the_langchain(self, llm, chain_type, prompt):
        chain = load_qa_chain(llm=self.llm, chain_type=self.chain_type, prompt=self.prompt)
        return chain        
    



# NEW CHAIN TYPE TO TRY FROM https://python.langchain.com/docs/modules/chains/popular/vector_db_qa

# from langchain.chains.question_answering import load_qa_chain
# qa_chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff") SAME AS CHAIN ABOVE
# qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever())

# query = "What did the president say about Ketanji Brown Jackson"
# qa.run(query)

# qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(), return_source_documents=True)

# ======================================================================

# query = "What did the president say about Ketanji Brown Jackson"
# result = qa({"query": query})

# result["result"]

# " The president said that Ketanji Brown Jackson is one of the nation's top legal minds, a former top litigator in private practice and a former federal public defender from a family of public school educators and police officers, and that she has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans."


# result["source_documents"]