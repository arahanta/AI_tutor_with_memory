from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from mem0 import Memory
import os
import warnings
from chromadb import Client

# Ignore all warnings
warnings.filterwarnings("ignore")


# Initialize ChromaDB client
client = Client()

# Configuration for memory and LLM
config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "test",
            "path": "db",  # Path to store the Chroma database
        }
    }
}

# Define the PersonalAITutor class
class PersonalAITutor:
    def __init__(self):
        """
        Initialize the PersonalAITutor with memory configuration and LLM client.
        """
        # Initialize memory using ChromaDB configuration
        self.memory = Memory.from_config(config)
        self.app_id = "app-1"

        # LLM Configuration (adjusted for correct usage)
        with open('secrete.txt', 'r') as file:
            Api_key = file.read().strip()
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=Api_key)
        
        self.prompt_template = PromptTemplate(
            input_variables=["input_text"],
            template="""
            You are an AI tutor. Your job is to help students with their questions across various subjects. 
            If the input is a question, provide a clear and concise answer. If the input is a casual greeting or non-question statement, 
            respond appropriately. 

            Instructions:
            1) If the input is a question, provide a clear and concise answer.
            - Include relevant information to ensure the student understands the topic.
            2) If the input is a casual greeting or non-question statement, respond appropriately without giving an educational answer.
    
            Input: {input_text}
            """
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def ask(self, question, user_id=None):
        """
        Ask a question to the AI, retrieve relevant memories, and store the conversation in memory.

        :param question: The question to ask the AI.
        :param user_id: Optional user ID to associate with the memory.
        :return: The AI-generated response.
        """
        # Retrieve relevant memories
        memories = self.get_memories(user_id=user_id)

        # If there are memories, prepend them to the question
        if memories:
            memories_content = "\n".join([memory['memory'] for memory in memories])
            question = f"Here are previous interactions with the user:\n{memories_content}\n{question}"

        # Generate a response using the LLM chain
        response = self.chain.run({"input_text": question})
        
        # Clean up the response to ensure it is HTML content
        content = response
        # Store both the question and response in memory
        self.memory.add(question, user_id=user_id, metadata={"app_id": self.app_id})
        self.memory.add(content, user_id=user_id, metadata={"app_id": self.app_id})

        return content

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with the given user ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)
