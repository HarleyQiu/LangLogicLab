from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import UnstructuredFileLoader
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):
    loader = UnstructuredFileLoader(pdf_path)
    return loader.load()


docs = load_pdf('./messari-report-crypto-theses-for-2023.pdf')

print(f'您的数据中有 {len(docs)} 个文档')
print(f'您的文档中有 {len(docs[0].page_content)} 个字符')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

print(f'现在您有 {len(split_docs)} 个文档')

llm = OpenAI(temperature=0)
chain = load_summarize_chain(llm, chain_type="stuff", verbose=True)

input_docs = split_docs[:10]
summaries = chain.run(input_documents=input_docs)
