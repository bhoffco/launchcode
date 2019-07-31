def analyze_text(text):
    # Your code here
    result = 0
    is_e = 0
    for char in text:
        if char.isalpha():
            result += 1
    for char in text:
        if char == "e" or char == "E":
            is_e +=1
    
    average = is_e / result
    average *= 100
    
    return "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(result, is_e, average)
    
    
        
    
    
    
    


# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)