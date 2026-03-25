'''
Important Components Of Langchain =>

                                            DATA SOURCE -> PDF
                                                    ↑↓
                                            GENERATIVE AI 
                                                    ↑↓
                                            Queries / Answer
                                                

RAG - Retrieval Augmented Generation

*1. DATA SOURCE       ==>>       2. SPLITTING       ==>>           3. EMBEDED            ==>>        4. STORE [VECTOR DATABASE]
- Data Ingestion               - Text Splitter                - Text -> Vector                 - FAISS, Pinecone, Weaviate, ASTRADB ChromaDB, Milvus, Redis
- Langchain                    - Into Chunks                  - means-> [1,3.2,4.2]            - Query to get context info

     -------------------------------->
    ↑                                 ↓
*QUESTIONS =>    RETRIEVE =>         PROMPT Template =>        LLM        =>       ANSWER
                    ↓
                Retrival Chain


- User questions will be search from the vector store
- and relevant context will be retrieved and then prompt will be created with the retrieved context and question and then LLM will generate the answer based on the prompt.


Retrival Chain => It is a interface, responsible for quering vector store DB
And we will get CONTEXT INFO.

With Context info and prompt template and will give to LLM model to get my output response.

Definition of RAG =>
Retrieval-Augmented Generation (RAG) is an AI framework that improves LLM accuracy by retrieving data from external,
trusted sources (documents, databases) before generating a response.

How it Works: RAG connects an LLM to external knowledge bases. When a user asks a question, the system retrieves
relevant data and feeds it into the model along with the prompt, allowing it to produce a, accurate, informed answer.

'''