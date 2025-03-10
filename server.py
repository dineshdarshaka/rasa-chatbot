import os
from rasa.core.agent import Agent

model_path = "models"
port = int(os.getenv("PORT", 5005))

if __name__ == "__main__":
    agent = Agent.load(model_path)
    agent.handle_channels([InputChannel(port=port)])
