# Write code below 💖
credits = int(input ('cuantos creditos tienes: '))
height = int(input ('indica tu altura en cm: '))
if height > 137 and credits > 10:
  print("Enjoy the ride!")
elif height < 137 and credits > 10:
  print("You are not tall enough to ride.")
elif height > 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print ("you don't have met either requirement")