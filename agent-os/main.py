from agno.os import AgentOS
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from os import getenv
from agno.tools.websearch import WebSearchTools
from prompts.math import MATH_PROMPT

load_dotenv()

HOST = getenv("HOST", "0.0.0.0")
PORT = getenv("PORT", "8000")

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
    # agent_os.serve("main:app", host=HOST, port=int(PORT), reload=True)
    math_agent.print_response("Olá, crie para mim 10 exercícios de matemática sobre propriedades da soma")