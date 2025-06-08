print ("Hello welcome to my quiz")

score = 0

answer = input("What is the capital of Japan?")
if answer == "Tokyo":
  print("Correct!")
  score += 1
elif answer == "":
  print("Um..")
else:
  print("Wrong")
print("The answer is Tokyo")

answer = input("What is the capital of China?")
if answer == "Beijing":
  print("Correct!")
  score += 1
elif answer == "":
  print("Um..")
else:
  print("Wrong")
print("The answer is Beijing")

answer = input("What is the capital of Korea?")
if answer == "Seoul":
  print("Correct!")
  score += 1
elif answer == "":
  print("Um..")
else:
  print("Wrong")
print("The answer is Seoul")

print("Your score is {}/3".format (score))
if score == 3:
  print("You are smart!")
elif score == 2:
  print("Nice!")
else:
  print("Try harder")
