#chat bot project
def chatbot():
 print("hello i am chat bot . type 'bye' to exit.")
#condition
 while True:
  user=input("you:").lower()
  if"hi"in user or "hello" in user:
   print("chatbot: hello there!")
  elif"how are you"in user:
   print("chatbot:I'm fine. what about you.")
  elif"what is your name" in user:
   print("chat bot: Iam chatbot . your virtual assistant")
  elif"who made you" in user:
   print(" I made by Ayush dwivedi")
  elif"who is bhanu sir" in user:
   print("bhanu sir is best  teacher in the world")
  elif"bye" in user:
   print("chatbot: good bye *_* . Have a nice day!")
   break
  else:
   print("chatbot: sorry , I don't understand that")
#to run the program
chatbot()