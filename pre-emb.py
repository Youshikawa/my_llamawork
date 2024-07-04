# from langchain.document_loaders import UnstructuredFileLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.huggingface import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS

# filepath="/home/yzc/llamawork/YuLiao.txt"
# loader=UnstructuredFileLoader(filepath)
# docs=loader.load()
# print(docs)
# # #打印一下看看，返回的是一个列表，列表中的元素是Document类型
# text_splitter=RecursiveCharacterTextSplitter(chunk_size=1500,chunk_overlap=50)
# docs=text_splitter.split_documents(docs)
# # print(docs[0])
# import os
# embeddings=HuggingFaceEmbeddings(model_name="/home/yzc/llamawork/text2vec-large-chinese", model_kwargs={'device': 'cuda'})
# #如果之前没有本地的faiss仓库，就把doc读取到向量库后，再把向量库保存到本地
# if os.path.exists("/home/yzc/llamawork/my_faiss_store.faiss")==True:
#     vector_store=FAISS.from_documents(docs,embeddings)
#     vector_store.save_local("/home/yzc/llamawork/my_faiss_store.faiss")
# #如果本地已经有faiss仓库了，说明之前已经保存过了，就直接读取
# else:
#     vector_store=FAISS.load_local("/home/yzc/llamawork/my_faiss_store.faiss",embeddings=embeddings)
# #注意！！！！
# #如果修改了知识库（knowledge.txt）里的内容
# #则需要把原来的 my_faiss_store.faiss 删除后，重新生成向量库


import os
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# 文件目录和路径
file_dir = "/home/yzc/doc_preprocess/book1"  # 替换为实际文件目录路径

# 获取所有txt文件的路径
file_paths = [os.path.join(file_dir, f) for f in os.listdir(file_dir) if f.endswith('.txt')]
file_dir = "/home/yzc/doc_preprocess/book2"
file_paths.extend([os.path.join(file_dir, f) for f in os.listdir(file_dir) if f.endswith('.txt')])
# 加载所有文件内容
docs = []
for filepath in file_paths:
    loader = UnstructuredFileLoader(filepath)
    docs.extend(loader.load())  # 将每个文件的文档添加到docs列表中

# 初始化嵌入模型
embeddings = HuggingFaceEmbeddings(model_name="/home/yzc/llamawork/text2vec-large-chinese", model_kwargs={'device': 'cuda'})

# 向量数据库文件路径
faiss_path = "/home/yzc/llamawork/my_faiss_store.faiss"

# 创建或加载向量数据库
if not os.path.exists(faiss_path):
    # 如果本地没有向量数据库，则创建一个新的
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local(faiss_path)
else:
    # 如果本地已经有向量数据库，则加载它
    vector_store = FAISS.load_local(faiss_path, embeddings=embeddings, allow_dangerous_deserialization=True)

# 注意，如果知识库（例如 knowledge.txt）里的内容修改了
# 则需要把原来的 my_faiss_store.faiss 删除后，重新生成向量库
