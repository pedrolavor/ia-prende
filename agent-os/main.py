from agno.os import AgentOS
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from os import getenv
from agno.tools.websearch import WebSearchTools

load_dotenv()

HOST = getenv("HOST", "0.0.0.0")
PORT = getenv("PORT", "8000")


MATH_PROMPT = """"
    Você é um agente especialista em matemática.
    Seu objetivo é criar exercícios de matemática para alunos do ensino fundamental.
    Você deve solicitar informações sobre o tópico de matemática específico que se o usuário deseja praticar ou reforçar (ex: adição, subtração, multiplicação, divisão, frações, etc.) e o nível de dificuldade desejado.
    Utilize suas ferramentas para pesquisar o assunto de matemática solicitado.
    Sempre pesquise primeiro para garantir que os exercícios sejam corretos e relevantes para o tópico solicitado.
    Utilizando as informações pesquisadas, crie exercícios de matemática que envolva o tópico solicitado.
"""

math_agent = Agent(
    id="math-agent",
    name="Matemático",
    description="Agente especialista em matemática.",
    model=Groq(id=getenv("GROQ_MODEL_ID")),
    tools=[WebSearchTools()],
    instructions=MATH_PROMPT,
    debug_mode=True,
)

agent_os = AgentOS(
    id="ia-prende-api",
    name="IA Prende API",
    description="API para IA Prende.",
    agents=[math_agent],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve("main:app", host=HOST, port=int(PORT), reload=True)