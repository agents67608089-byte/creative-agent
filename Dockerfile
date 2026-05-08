FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install crewai langchain-groq
CMD ["python", "main.py"]
