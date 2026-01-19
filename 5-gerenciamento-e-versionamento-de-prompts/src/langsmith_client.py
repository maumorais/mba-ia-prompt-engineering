from dotenv import load_dotenv
from langsmith import Client
from langchain.chat_models import init_chat_model

# Load environment variables from .env file
load_dotenv()

client = Client()

#Chamada preparada para buscar uma commit tag específica
prompt = client.pull_prompt("agent-pull-request-creator:dev")

# Chamada preparada para buscar a latest
#prompt = client.pull_prompt("agent-pull-request-creator")

model = init_chat_model("gpt-4o-mini")
chain = prompt | model
print(chain.invoke({
    "changes_summary": "Implementation of cache system to improve performance",
    "files_changed": "src/cache.py, tests/test_cache.py, README.md",
    "issue_number": "42",
    "branch_name": "feature/add-cache-system",
    "breaking_changes": "No",
    "testing_done": "Unit tests added with 95% coverage",
}).content)