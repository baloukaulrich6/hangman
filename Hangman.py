from replit import  clear

import  random
hangman = ('''


 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   



''')
stages = ['''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|______
''','''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|______
''','''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |   
     |         
     |
 ____|______


''','''
     _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
 ____|______
''','''
     _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
 ____|______
''','''
     _______
     |/      |
     |      (_)
     |       |
     |       
     |        
     |
 ____|______
''','''
     _______
     |/      |
     |      (_)
     |      
     |       
     |        
     |
 ____|______
''','''
     _______
     |/      |
     |      
     |      
     |       
     |       
     |
 ____|______
''']
print(hangman)
end_of_game = False
word_liste = ["zoro", "sanji", "camel"]
chosen_word =random.choice(word_liste)
word_length= len(chosen_word)

lives = 6

print(f"la solution est {chosen_word}")
display =[]
for _ in range(word_length):
     display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"current position: {position}\n current letter : {letter}\n letter{guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])







