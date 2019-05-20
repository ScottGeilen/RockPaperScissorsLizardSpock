#import RPi.GPIO as GPIO
import random
import time
import sys

#GreenLed = 17
#RedLed = 23

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(GreenLed, GPIO.OUT)
#GPIO.output(GreenLed, GPIO.HIGH)

#GPIO.setup(RedLed, GPIO.OUT)
#GPIO.output(RedLed, GPIO.HIGH)




while True:
    
    human = input("Rock, Paper, Scissors, Lizard, or Spock?\n\n") # Human input. Human types from options, "Rock, Paper, Scissors, Lizard, or Spock".
    computerInt = random.randint(0, 4) # Assigning integers to the options so computer can understand


    if computerInt == 0:
        computerInt = "Rock.\n\n"
    elif computerInt == 1:
        computerInt = "Paper.\n\n"
    elif computerInt == 2:
        computerInt = "Scissors.\n\n"
    elif computerInt == 3:
        computerInt = "Lizard.\n\n"
    elif computerInt == 4:
        computerInt = "Spock.\n\n"


# If human chooses Rock
    if  human.upper() == "ROCK":
        print("You entered Rock.\n\n")
        time.sleep(1)
        
        print("Get ready. . .\n\n")
        time.sleep(2)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Lizard!\n\n")
        time.sleep(1)
        print("Spock!\n\n")
        time.sleep(1)
        
        print("The computer chooses " + str(computerInt))
        time.sleep(2)
        if computerInt == "Rock.\n\n":
            print("Nothing happens.\n\n")
            time.sleep(2)
            print("It's a tie.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Paper.\n\n":
            print("Rock is covered by Paper.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Scissors.\n\n":
            print("Rock crushes Scissors.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Lizard.\n\n":
            print("Rock crushes Lizard.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Spock.\n\n":
            print("Rock is vaporized by Spock.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)

# If human chooses Paper
    if  human.upper() == "PAPER":
        print("You entered Paper.\n\n")
        time.sleep(1)
        
        print("Get ready. . .\n\n")
        time.sleep(2)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Lizard!\n\n")
        time.sleep(1)
        print("Spock!\n\n")
        time.sleep(1)
        
        print("The computer chooses " + str(computerInt))
        time.sleep(2)
        if computerInt == "Rock.\n\n":
            print("Paper covers Rock.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Paper.\n\n":
            print("Nothing happens.\n\n")
            time.sleep(2)
            print("It's a tie.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Scissors.\n\n":
            print("Paper is cut Scissors.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Lizard.\n\n":
            print("Paper is eaten by Lizard.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Spock.\n\n":
            print("Paper disproves Spock.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
# If human chooses Scissors
    if  human.upper() == "SCISSORS":
        print("You entered Scissors.\n\n")
        time.sleep(1)
        
        print("Get ready. . .\n\n")
        time.sleep(2)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Lizard!\n\n")
        time.sleep(1)
        print("Spock!\n\n")
        time.sleep(1)
        
        print("The computer chooses " + str(computerInt))
        time.sleep(2)
        if computerInt == "Rock.\n\n":
            print("Scissors is crushed by Rock.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Paper.\n\n":
            print("Scissors cuts Paper.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Scissors.\n\n":
            print("Nothing happens.\n\n")
            time.sleep(2)
            print("It's a tie.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Lizard.\n\n":
            print("Scissors decapitates Lizard.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Spock.\n\n":
            print("Scissors are smashed by Spock.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)

# If human chooses Lizard
    if  human.upper() == "LIZARD":
        print("You entered Lizard.\n\n")
        time.sleep(1)
        
        print("Get ready. . .\n\n")
        time.sleep(2)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Lizard!\n\n")
        time.sleep(1)
        print("Spock!\n\n")
        time.sleep(1)
        
        print("The computer chooses " + str(computerInt))
        time.sleep(2)
        if computerInt == "Rock.\n\n":
            print("Lizard is crushed by Rock.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Paper.\n\n":
            print("Lizard eats Paper.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Scissors.\n\n":
            print("Lizard is decapitated by Scissors.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Lizard.\n\n":
            print("Nothing happens.\n\n")
            time.sleep(2)
            print("It's a tie.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Spock.\n\n":
            print("Lizard poisons Spock.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)

# If human chooses Spock
    if  human.upper() == "SPOCK":
        print("You entered Spock.\n\n")
        time.sleep(1)
        
        print("Get ready. . .\n\n")
        time.sleep(2)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Lizard!\n\n")
        time.sleep(1)
        print("Spock!\n\n")
        time.sleep(1)
        
        print("The computer chooses " + str(computerInt))
        time.sleep(2)
        if computerInt == "Rock.\n\n":
            print("Spock vaporizes Rock.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Paper.\n\n":
            print("Spock is disproved by Paper.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Scissors.\n\n":
            print("Spock smashes Scissors.\n\n")
            time.sleep(2)
            print("You win.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)
            
        if computerInt == "Lizard.\n\n":
            print("Spock is poisoned by Lizard.\n\n")
            time.sleep(2)
            print("You lose.\n\n")
            #GPIO.output(GreenLed, GPIO.HIGH)
            #GPIO.output(RedLed, GPIO.LOW)
            time.sleep(3)
            
        if computerInt == "Spock.\n\n":
            print("nothing happens.\n\n")
            time.sleep(2)
            print("It's a tie.\n\n")
            #GPIO.output(GreenLed, GPIO.LOW)
            #GPIO.output(RedLed, GPIO.HIGH)
            time.sleep(3)




    # Restart game scenario
    human = input("Would you like to play again? (y/n)\n\n")
    
    #GPIO.output(GreenLed, GPIO.LOW)
    #time.sleep(.5)
    #GPIO.output(RedLed, GPIO.HIGH)
    #time.sleep(.5)
    #GPIO.output(GreenLed, GPIO.HIGH)
    #time.sleep(.5)
    #GPIO.output(RedLed, GPIO.HIGH)
    
    if not human == "y":
        print("Exiting game.\n\n")
        break
