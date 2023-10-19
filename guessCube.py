cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guess = 0

for guess in range(abs(cube + 1)):
  if guess**3 >= abs(cube):
    break

if guess**3 != abs(cube):
  print('Not a exact cube')
else:
  if cube < 0:
    guess = -guess
  print(f'Right guess {guess}')

print('###')
print('binary')
print('###')

cube = 64
num_guesses = 0
epsilon = 0.001
low = 0
high = cube
guess = high + low / 2

while (guess**3 - cube) >= epsilon:
  if guess**3 < cube:
    low = guess
  else:
    high = guess

  guess = (high + low) / 2
  num_guesses += 1
  print(guess)

print(f'num of guess: {num_guesses}')
print(f'{guess} is close to the cube root of {cube}')  

  