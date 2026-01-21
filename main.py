from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 

load_dotenv()

def main():
    print("Hello from langchain-course!")

    text = """
                Elon Reeve Musk ( born June 28 , 1971 ) is a South African - Canadian - American businessman. He is the founder of SpaceX and co-inventor and founder of Zip2 . Musk is also aware of an electric car brand Tesla , which he founded a year ago, with the expectation that he may also call himself founder of Tesla. He is also the founder of X.com, which later merged with Confinity Inc. wyder gung as PayPal . He is general manager and chief designer of SpaceX, general manager and product designer for Tesla and former chairman of SolarCity, before Tesla took over. He also founded The Boring Company and helped found Neuralink and OpenAI . With a taxable net worth of a staggering 247 billion euros, Musk was the richest man in the world in December 2021 .
            """

    summary_template = """
    Given the following {text}, provide a concise summary.
    1. Keep it under 50 words.
    2. Focus on the main points.
    3. Use clear and simple language.
    4. Avoid technical jargon.
    """

    summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)

    llm = ChatOpenAI(model="gpt-5", temperature=0)

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"text": text})
    print(response.content)

if __name__ == "__main__":
    main()
