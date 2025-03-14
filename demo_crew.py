import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-11111111111111111111111111111111"

# Configurer Ollama avec Llama3.2
llm = ChatOpenAI(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434"
)

# Define the agents
researcher = Agent(
    role="Senior Research Analyst", 
    goal="Find compelling information about the topic",
    backstory="""
        You are a researcher in digital sustainability for AI who is tasked with finding information about the topic in scientific papers articles and reports with a focus on data and verified sources.
    """,
    verbose=True,
    allow_delegation=False,
    # Utiliser Ollama avec Llama3.2
    llm=llm
)
writer = Agent(
    role="Technical Content Writer", 
    goal="Write a report about the topic",
    backstory="You are a writer who is tasked with writing a report about the topic.",
    verbose=True,
    allow_delegation=False,
    # Utiliser Ollama avec Llama3.2
    llm=llm
)

# Define the tasks
task1 = Task(
    description="Research the topic and provide a list of sources",
    expected_output="A comprehensive list of sources and information about the topic.",
    agent=researcher
)
task2 = Task(
    description="Write a report about the topic",
    expected_output="A well-written report about the topic based on the scientific papers and sources provided in a structured way with actionable insights for the reader.",
    agent=writer
)

# Create the crew
crew = Crew(
    agents=[researcher, writer], 
    tasks=[task1, task2],
    verbose=True,
)

# Run the crew
result = crew.kickoff()

# Print the result
print("########################")
print(result)
