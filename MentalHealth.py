#all imports should be at the top
import datetime 

usernames = []
passwords = []
names = []


def register():
    names.append(input("Enter your name:"))
    usernames.append(input("choose your username:"))
    passwords.append(input("choose your password:"))


def login():
    username = input("Enter your username:")
    password = input("Enter your Password:")
    if username in usernames and password in passwords:
        print("welcome")
    else:
        print("incorrect!")


while True:
    account_ans = input("choose:  a)Sign Up     b)login and shop     c)quit ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        break


name = input("Enter name: ")
if name.isalpha():
  print(f"{name}\n")
else:
 print("invalid input only alphabetic characters "+name) 
 exit()

#name = input("Enter your name: ")
#print(f"{name}\n")

feeling = input("Select how you are feeling: \n1: Happy \n2: Sad \n3: Angry \n4: Depressed \n5: Ambitious \n6: Calm \n7: Defensive \n8: Fearful \n9: Frustrated \n10: Nervous \n11: Anxious\n")


def numberFeeling(feeling):
  if(feeling == "1"):
    return "happy"
  elif(feeling == "2"):
    return "sad"
  elif(feeling == "3"):
    return "angry"
  elif(feeling == "4"):
    return "depressed"  
  elif(feeling == "5"):
    return "ambitious"
  elif(feeling == "6"):
    return "calm"
  elif(feeling == "7"):
    return "defensive"
  elif(feeling == "8"):
    return "fearful"
  elif(feeling == "9"):
    return "frustrated"
  elif(feeling == "10"):
    return "nervous"
  elif(feeling == "11"):
    return "anxious"
  else:
    print("invalid option")

mood = numberFeeling(feeling)  
print(f"Hello {name}, tell me why you're feeling {mood} ")

  
notes = input(">: ")

with open(f"{name}-note.txt", mode="a+") as file:
    file.write('%s client %s reported feeling %s because %s.\n' % (datetime.datetime.now(), name, mood, notes))
#items = ["angie", "dave", "test"]

#for item in items:
 #   with open("{}note.txt".format(item), "w") as f:
 #       f.write("This is my first line of code")
  #      f.write("\nThis is my second line of code with {} the first item in my list".format(item))
 #       f.write("\nAnd this is my last line of code")

#with open("note.txt", mode='a') as file:
    
    

def pickFeeling(mood):
    if(feeling == "1"):
      print(f"congrats you're {mood} try getting out and enjoying yourself or staying in and doing things you like") 
    elif(feeling == "2"):
      print(f"bummed you're {mood}, try listening to songs that remind you of happy memories") 
    elif(feeling == "3"):
      print(f"yikes {mood}, try to exert your energy and release tention like breaking something in a safe way, screaming, hitting a punching bag") 
    elif(feeling == "4"):
      print(f"awe you're {mood}, try talking to someone unexpressed emotions tend to build until they spill over")   
    elif(feeling == "5"):
      print(f"super you're {mood}, trying using this time doing something that you would normally put off") 
    elif(feeling == "6"):
      print(f"cool you're {mood}, try taking this time to do something you enjor or learn a new skill")
    elif(feeling == "7"):
      print(f"sorry you're {mood}, try a writing exercise that allows you to express your feelings and also recognize your triggers")
    elif(feeling == "8"):
      print(f"oh no you're {mood}, try turning on a funny show or laughing research suggest that you cant be fearful and humorous at the same time")
    elif(feeling == "9"):
      print(f"ugh you're {mood}, try exercising which relieves stress and releases endorphins that can improve yoyr mood") 
    elif(feeling == "10"):
      print(f"whew you're {mood}, try doing something that excites you, the same physical symptoms are accociated with both nervousness") 
    elif(feeling == "11"):
      print(f"whoa you're {mood}, try stepping away from what you're doingand try to relax")  
pickFeeling(mood)


