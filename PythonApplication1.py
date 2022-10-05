#! /usr/bin/python

print('Content-type: text/html')
print('')
import random
import cgi
from random import randint
# Libreria che permette di comunicare con l'utente e il browser
form = cgi.FieldStorage()

reds= 0
white= 0


    #Se la sequenza non è già presente la crea 
if ('answer') in form:
    answer = form.getvalue('answer')
else:
    #Viene creato la senquenza di numeri da indovinare tramite la funzione randint
    answer = ('')
    for i in range(4):
        
        answer += str(randint(0, 9))




# Verifica che la variabile sia presente
if ('guess') in form:
    # Associa la variabile guess
    guess = form.getvalue('guess')
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    white += 1
                break 
                
else:
    guess = ('')

#Numero tentativi utente
if('number') in form:
    number= int (form.getvalue('number')) +1
else:
    number = 0    

if number == 0:
    message = "I've chosen a 4 digit number. Can you guess it?"
else: 
   
    message= 'You have '+ str(reds) + 'correct digits in the right place, and ' + str(white) + ' correct digits in the wrong place. You have had ' + str(number) + 'guess(es)'
    if(reds == 4):
         message=('Well done')
 

print('<h1>Mastermind</h1>')
print("<p>"+message+"</p>")
print('<form method="POST">')
print('<input type="text" name="guess" value="'+guess+'">')
print('<input type="hidden" name="answer" value="'+answer+'">')
print('<input type="hidden" name="numberOfGuess" value="'+str(number)+'">')
print('<input type="submit" value="Guess!"')
print('</form>')
