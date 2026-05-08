import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# 初始化大腦 (Groq)
llm = ChatGroq(model_name="llama3-70b-8192", api_key=os.environ.get("GROQ_API_KEY"))

# 設定代理人
researcher = Agent(
  role='創作資料蒐集員',
  goal='搜尋並整理 19 世紀服裝設定',
  backstory='你是一位專業的小說設定顧問，擅長找尋精確細節。',
  llm=llm
)

# 定義簡單任務
task = Task(description='寫出三種當時倫敦貧民窟常見的衣服材質。', agent=researcher)

# 執行
crew = Crew(agents=[researcher], tasks=[task])
print(crew.kickoff())
