from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma


class MyLLMConfiguration:
    def __init__(self, path):
        self.path = path
        self.data = self.load_data_from_file()
        self.split_data_from_file = self.split_data()
        self.vector_store_from_file = self.create_vector_from_data()
        self.ollama = self.initialize_ollama()
        self.qachain = self.initialize_qachain()

    def load_data_from_file(self):
        with open(self.path, 'r') as file:
            data = file.read()
            return data

    def split_data(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        # Create a Document object for each line in data
        documents = [MyLLMConfiguration.parse_document(line) for line in self.data.split('\n') if line.strip() != '']
        all_splits = text_splitter.split_documents(documents)
        return all_splits

    def create_vector_from_data(self):
        oembed = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
        vectorstore = Chroma.from_documents(documents=self.split_data_from_file, embedding=oembed)
        return vectorstore

    def initialize_ollama(self):
        return Ollama(
            base_url='http://localhost:11434',
            model="llama3"
        )

    def initialize_qachain(self):
        return RetrievalQA.from_chain_type(self.ollama, retriever=self.vector_store_from_file.as_retriever())

    @staticmethod
    def parse_document(line):
        fields = line.split(';')
        metadata = {}
        for field in fields:
            key_value = field.split(':', 1)
            if len(key_value) == 2:
                key, value = key_value
                metadata[key.strip()] = value.strip()
        return Document(page_content=line, metadata=metadata)

    def ask_question(self, question):
        return self.qachain.invoke({"query": question})


class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata


# Global variables
current_path = None
my_llm = None


def talk_via_ollama(path):
    global current_path
    global my_llm

    if current_path != path:
        print("Loading new data from file, wait for moment\n")
        current_path = path
        my_llm = MyLLMConfiguration(path)

    print(
        """Hi This is CodeTutor assistant here. You can ask me questions on availability of videos by topic. I can help you with whether such video exists or not.""")

    while True:
        question = input("Ask your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        response = my_llm.ask_question(question)
        print(response['result'])
        print("\n")

    return
