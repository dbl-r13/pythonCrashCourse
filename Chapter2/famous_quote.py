#Import statement for the choice method of the Random package
from random import choice as c

#Created an array with all the author's names of the quotes below. 
arr = ["Theodore Roosevelt", "Neil Armstrong", "Franklin D. Roosevelt"]

#Dictionary of Quotes that have the Key/Value pair of Author/Quote
quotes = { "Theodore Roosevelt": "Speak softly and carry a big stick", "	Neil Armstrong": "That's one small step for a man, a giant leap for mankind.", "Franklin D. Roosevelt": "The only thing we have to fear is fear itself."} 

#Randomly chooses an author from array above and saves to variable
pick = c(arr)

#Prints the the random data provided from all above data structures into a sentence.
print(f"{pick} once said, '{quotes[pick]}'")
