from langchain.chains.question_answering import load_qa_chain

from mosaicml_set_up import MosaicmlSetUp

# Device set-up
device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

# Parameters for mosaicml
model_type = ["mosaicml/mpt-30b-chat"]
task_types = ["text_generation"]

model = "mosaicml-30B" # Choices are "mosaicml-30B", "openai", "ChatOpenAI" -> TO DO: make into a command line variable

if __name__ == "__main__":

    if model == "mosaicml-30B":
        mosaicml_setup = MosaicmlSetUp(
            device=device,
            model_type=model_type[0], 
            task_type=task_type[0]
            )
        model_setup = mosaicml_setp.model_setup(device=device, model_type=model_type)
        stopping_criteria = mosaicml.stopping_criteria()
        llm = mosaicml.generate_text(task_type=task_type, stopping_criteria=stopping_criteria)

    if model == "openai":
        pass

    if model == "ChatOpenAI":
        pass

    print("\n")
    print("--- START ---")
    print("\n")
    print(f"Model type: {model}")
    print("\n")
    chain = load_qa_chain(llm=llm, chain_type=parameters[1], prompt=PROMPT)
    chain.run(input_documents=docs, question=query, products=products, language_one=language_one, language_two=language_two,
          language_three=language_three, return_only_outputs=True, memory=memory, verbose=True)
    print("\n")
    print("--- FIN ---")
    print("\n")