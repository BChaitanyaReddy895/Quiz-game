

print("Hi welcome to quiz world!")

subject=input(("select the subject(mathematics,physics,chemistry)\nin which you want to test your knowledge:\n"))

if(subject=="mathematics" or "maths"):
    age=int(input("enter your current age:"))
    if(6<age<=10):
        print("let's start your quiz:")
        print("q1:Is 12*3 and 3*12 are same?")
        answer=input("enter your answer(true/false):")
        score=0
        if (answer=="true"):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q2:what is the result for 12/0 ?")
        answer=input("enter your answer:")
        if answer==("not defined" or "Not Defined" or "infinite"):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q3:what is the result for (12*3+12-10/5)?")
        answer=int(input("enter your answer:"))
        if (answer==46):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q4:what is the remainder for 15/2?")
        answer=int(input("enter your answer:"))
        if (answer==1):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q5:if cost of 1 pen is 5rupees what is the cost of 5 pens?")
        answer=int(input("enter your answer:"))
        if (answer==25):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("thanks for taking quiz!!!")
        print("your final score is:",score)
        percentage=(score/5)*100
        print(" your percentage is:",percentage)
        if(3<score<=5):
            print("you have good knowledge in maths")
        else:
            print("good try, but try to improve your score next time!!!")
            quit()
    else:
            print("sorry your age is too low")
subject=input(("select the subject(mathematics,physics,chemistry)\nin which you want to test your knowledge:\n"))

if(subject=="english"):
    age=int(input("enter your current age:"))
    if(6<age<=10):
        print("let's start your quiz:")
        print("q1:")
        answer=input("enter your answer(true/false):")
        score=0
        if (answer=="true"):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q2:what is the result for 12/0 ?")
        answer=input("enter your answer:")
        if answer==("not defined" or "Not Defined" or "infinite"):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q3:what is the result for (12*3+12-10/5)?")
        answer=int(input("enter your answer:"))
        if (answer==46):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q4:what is the remainder for 15/2?")
        answer=int(input("enter your answer:"))
        if (answer==1):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("your next question is")
        print("q5:if cost of 1 pen is 5rupees what is the cost of 5 pens?")
        answer=int(input("enter your answer:"))
        if (answer==25):
            print("your are right!")
            score+=1
        else:
            print("your are wrong")
        print("thanks for taking quiz!!!")
        print("your final score is:",score)
        percentage=(score/5)*100
        print(" your percentage is:",percentage)
        if(3<score<=5):
            print("you have good knowledge in maths")
        else:
            print("good try, but try to improve your score next time!!!")
            quit()
    else:
            print("sorry your age is too low")
                        
   

        
    

       
    

        
