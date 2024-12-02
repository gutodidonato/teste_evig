from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

async def generate_description(property_details: dict) -> str:
    # Cria uma string formatada com os detalhes da propriedade
    details = ", ".join([f"{key}: {value}" for key, value in property_details.items()])

    template = """
    Question: {details}
    
    Answer: Let's think step by step."""


    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3.2", base_url="http://localhost:11434")  
    

    chain = prompt | model
    response = chain.invoke({"details": f"Me fale sobre uma propriedade que: {details}"})
    return response