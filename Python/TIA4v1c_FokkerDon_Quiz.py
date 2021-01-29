print("\nWelcome to my quiz make sure to answer all the questions with a captial letter!")

starting = True
while starting:
    choice = input("Would you like to start the quiz? Y/N: ")
    if choice == "Y":
        print ("\nStarting the quiz.")
        starting = False
        break
    elif choice == "N":
        print ("Bruh")
    else:
        print ("Please enter Y or N.")
        
score = 0

Q1 = input("\n1. What is a correct syntax to output \"Hello World\" in Python? \nA. echo \"Hello World\" \nB. p(\"Hello World\") \nC. print(\"Hello World\") \nD. echo(\"Hello World\") \nAnswer: ")

if Q1 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q2 = input("\n2. How do you insert COMMENTS in Python code? \nA. //This is a comment \nB. /*This is a comment*/ \nC. #This is a comment \nAnswer: ")

if Q2 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q3 = input("\n3. Which one is NOT a legal variable name? \nA. _myvar \nB. my-var \nC. Myvar \nD. my_var \nAnswer: ")

if Q3 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q4 = input("\n4. How do you create a variable with the numeric value 5? \nA. X = 5 \nB. Both the other answers are correct \nC. X = int(5) \nAnswer: ")

if Q4 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q5 = input("\n5. What is the correct file extension for Python files? \nA. .pyth \nB. .pt \nC. .py \nD. .pyt \nAnswer: ")

if Q5 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q6 = input("\n6. How do you create a variable with the floating number 2.8? \nA. X = float(2.8) \nB. Both the other answers are correct \nC. X = 2.8 \nAnswer: ")

if Q6 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q7 = input("\n7. What is the correct syntax to output the type of a variable or object in Python? \nA. print(typeOf(x)) \nB. print(type(x)) \nC. print(typeof(x)) \nD. print(typeof x) \nAnswer: ")

if Q7 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q8 = input("\n8. What is the correct way to create a function in Python? \nA. create myFunction(): \nB. def myFunction(): \nC. function myfunction(): \nAnswer: ")

if Q8 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q9 = input("\n9. What is the correct way to create a function in Python? \nFalse \nTrue \nAnswer: ")

if Q9 == "TRUE":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q10 = input("\n10. What is a correct syntax to return the first character in a string? \nA. X = \"Hello\"[0] \nB. X = sub(\"Hello\", 0, 1) \nC. X = \"Hello\".sub(0, 1) \nAnswer: ")

if Q10 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q11 = input("\n11. Which method can be used to remove any whitespace from both the beginning and the end of a string? \nA. ptrim() \nB. strip() \nC. trim() \nD. len() \nAnswer: ")

if Q11 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q12 = input("\n12. Which method can be used to return a string in upper case letters? \nA. toUpperCase() \nB. upperCase() \nC. upper() \nD. uppercase() \nAnswer: ")

if Q12 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q13 = input("\n13. Which method can be used to replace parts of a string? \nA. switch() \nB. replace() \nC. replaceString() \nD. repl() \nAnswer: ")

if Q13 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q14 = input("\n14. Which operator is used to multiply numbers? \nA. % \nB. # \nC. X \nD. * \nAnswer: ")

if Q14 == "D":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q15 = input("\n15. Which operator can be used to compare two values? \nA. <> \nB. = \nC. >< \nD. == \nAnswer: ")

if Q15 == "D":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q16 = input("\n16. Which of these collections defines a LIST? \nA. [\"apple\", \"banana\", \"cherry\"] \nB. {\"name\": \"apple\", \"color\": \"green\"} \nC. (\"apple\", \"banana\", \"cherry\") \nD. {\"apple\", \"banana\", \"cherry\"} \nAnswer: ")

if Q16 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q17 = input("\n17. Which of these collections defines a TUPLE? \nA. {\"name\": \"apple\", \"color\": \"green\"} \nB. [\"apple\", \"banana\", \"cherry\"] \nC. (\"apple\", \"banana\", \"cherry\") \nD. {\"apple\", \"banana\", \"cherry\"} \nAnswer: ")

if Q17 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q18 = input("\n16. Which of these collections defines a SET? \nA. [\"apple\", \"banana\", \"cherry\"] \nB. {\"apple\", \"banana\", \"cherry\"} \nC. (\"apple\", \"banana\", \"cherry\") \nD. {\"name\": \"apple\", \"color\": \"green\"} \nAnswer: ")

if Q17 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q19 = input("\n19. Which of these collections defines a DICTIONARY? \nA. {\"name\": \"apple\", \"color\": \"green\"} \nB. [\"apple\", \"banana\", \"cherry\"] \nC. {\"apple\", \"banana\", \"cherry\"} \nD. (\"apple\", \"banana\", \"cherry\") \nAnswer: ")

if Q19 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q20 = input("\n20. Which collection is ordered, changeable, and allows duplicate members? \nA. LIST \nB. SET \nC. TUPLE \nD. DICTIONARY \nAnswer: ")

if Q20 == "A":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q21 = input("\n21. Which collection does not allow duplicate members? \nA. LIST \nB. SET \nC. TUPLE \nAnswer: ")

if Q21 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q22 = input("\n22. How do you start writing an if statement in Python? \nA. if (x > y) \nB. if x > y then: \nC. if x > y: \nAnswer: ")

if Q22 == "C":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q23 = input("\n23. How do you start writing a while loop in Python? \nA. while(x > y) \nB. while x > y: \nC. while x > y { \nD. x > y while { \nAnswer: ")

if Q23 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q24 = input("\n24. How do you start writing a for loop in Python? \nA. for each x in y: \nB. for x > y: \nC. for x in y: \nAnswer: ")

if Q24 == "B":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

Q25 = input("\n25. Which statement is used to stop a loop? \nA. exit \nB. return \nC. stop { \nD. break { \nAnswer: ")

if Q25 == "D":
    print("CORRECT!")
    score = score + 1
else:
    print("INCORRECT!")

print ("\n\nYour score is: " + str(score))
 
if score >= 19:
    print ("You scored high.")
elif score <= 14:
    print ("You scored below avarage.")
else:
    print ("You scored avarage.")


#Answers: 1.C 2.C 3.C 4.A 5.C 6.A 7.B 8.B 9.TRUE 10.A 11.C 12.C 13.B 14.D 15.D 16.A 17.C 18.B 19.A 20.A 21.B 22.C 23.B 24.B 25.D