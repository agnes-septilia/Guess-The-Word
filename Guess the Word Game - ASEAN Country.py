print("Guess the ASEAN country")

#define the computer option
import random
country = ['Indonesia', 'Malaysia', 'Singapore', 'Thailand', 'Philippine',
           'Laos', 'Brunei', 'EastTimor', 'Vietnam', 'Myanmar', 'Kamboja']
comp = random.choice(country)
lw_comp = comp.lower()

#close the chosen word
dashed = ""
for c in comp:
    dashed = dashed + "-"
print(dashed)

#start the game 
i = 0
wrong = 0
while i >= 0:
    guest = input("Guess the letter: ")
    #transform the input into lowercase
    guest = guest.lower()
    #if the letter is not in the chosen word, add `wrong` score
    if lw_comp.count(guest) == 0:
        wrong = wrong + 1
    #if the letter is in the chosen word, reveal the letter
    for j in range(len(lw_comp)):
        if lw_comp[j] == guest:
            dashed = dashed[:j] + comp[j] + dashed[j+1:]
    print(dashed)

    #if more then 5 times failed, gameover. Otherwise, win.
    if wrong == 5:
        print("Game over!")
        break      
    if dashed == comp:
        print("Congratulations! You guess it right!")
        break
    i = i + 1        

print()
input("Press enter to exit")

