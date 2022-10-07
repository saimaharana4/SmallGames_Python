import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
li=[rock,paper,scissors]
randomize =random.randint(0,len(li)-1)

rps=int(input(What do you want Rock 0, Paper 1, Scissors 2n))
if rps = 3 or rps  0
  print(you chose invalid no. Try Again )
else
  print(li[rps])
  print(Computer Choose-)
  print(li[randomize])
  
  if rps == 0 and randomize == 2
    print(You Wins)
  elif randomize == 0 and rps ==2
    print(You Lose)
  elif (rps randomize)
    print(You Win!)
  elif randomize  rps
    print(You Lose)
  elif rps == randomize
    print(Its Draw)

