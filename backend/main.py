from vectorDB import VectorDBConstructor

data_source = "basler" # Need to variablise as an input arg from the command line
pdf_path = "../pdf/"+data_source
embedding = "openai" # Need to variablise as an input arg from the command line
db = "chroma" # Need to variablise as an input arg from the command line

if __name__ == "__main__":
    vector_db_constructor = VectorDBConstructor(
        data_source=data_source,
        pdf_path=pdf_path, 
        embedding=embedding, 
        db=db
        )
    pdf_list = vector_db_constructor.create_pdf_list(pdf_path=pdf_path)
    pdf_read = vector_db_constructor.read_pdf(pdf_list, data_source=data_source)
    pdf_chunk = vector_db_constructor.chunk_pdf(pdf_read)
    pdf_vector = vector_db_constructor.create_vectorDB(
        pdf_chunk, 
        data_source=data_source, 
        embedding=embedding, 
        db=db)
