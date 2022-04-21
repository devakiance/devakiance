import random

print("This is game which you check if a number you entered is the same with a random number from 1 to 100")
print("You have to enter only a number from 1 to 100, if you enter a bigger or a smaller number it will ask again")
print("Also, if you enter a string it will ask for a number from 1 to 100 again. If you enter a number different than")
print("the random number it will tell you if it is bigger or smaller from the random number and it will start again.")
print("If you enter a number which is the same with the random number you will win and the game will tell you how many times ")
print("you entered a wrong number. Anytime it asks you for a number you can exit the programm by writing exit")
print("The game will give you 10-n poitns where n is the number of lost tries")
print("If you want to play again the game will ask you and you should type yes, if you do not want to play again write no")





while(True):
        times = 0
        x = random.randrange(1,100,1)
        while (True):
                while (True):
                        y = input("Enter a number from 1 to 100: ")
                        if (y=="exit"):
                                break
                        count = 0
                        if len(y)==1:
                                if y[0] == '1' or y[0]=='2' or y[0]=='3' or y[0]=='4' or y[0]=='5' or y[0]=='6' or y[0]=='7' or y[0]=='8' or y[0]=='9':
                                        count = count + 1
                                elif y[0] == '0':
                                        count = -500
                        elif len(y)==2:
                                if y[0] == '1' or y[0]== '2' or y[0]=='3' or y[0]=='4' or y[0]=='5' or y[0]=='6' or y[0]=='7' or y[0]=='8' or y[0]=='9':
                                        count = count + 1
                                elif y[0]=='0':
                                        count = -500

                                if y[1]== '0' or y[1] == '1' or y[1]=='2' or y[1]=='3' or y[1]=='4' or y[1]=='5' or y[1]=='6' or y[1]=='7' or y[1]=='8' or y[1]=='9':
                                        count = count + 1
                        if count == 2 or count==1:
                                y = int(y)
                                break
                        else:
                                print("You did not enter a number from 1 to 100")              


                if(y=="exit"):
                        break
                if (x==y):
                        if (times<=10):
                                print("Congratulations, you found the number after ", times, " times and you won ",10-times, "points")
                        else:
                                print("Congratulations, you found the number after ", times, " times but you won no points because you tried more than 10 times")
                        break
                elif (x<y):
                        print("The number you entered is bigger than the random number")
                        times = times + 1
                elif(x>y):
                        print("The number you entered is smaller than the random number")
                        times = times + 1
        z = input("Do you want to play again? ")
        if z == "no" or z == "exit":
                print("Bye bye")
                break
        elif z == "yes":
                continue
