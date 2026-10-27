import os

def answeringbot():
  
  print("Question Answering Bot")

  question = input("Ask me something: ")
  
  if question == "HKU":
    print("Bot: Hello! Wellcome to HKU.")

  elif question == "robot":
    print("Bot: I'm a chatting robot.")

  elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer.")

  elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")

  elif question == "human":
    print("Bot: I'm not a human. Are you?")

  else:
    print("Bot: Sorry, I don't understand.")

while(1):

  answeringbot()
