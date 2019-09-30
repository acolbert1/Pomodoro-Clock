import time
import threading
import random
#ToDo
 
#4. cleanup method names, print statements, and seconds. 
#add the correct naming for minutes. i.e. 1 minutes should be minute
#add conditional if yes or no isn't inputted.
#fix print statement if all 4 items have been completed in the list

class Pomodoro_Clock:
    def __init__(self):
        self.pomodoro_session = 0
        self.minutes_passed = 0
        self.minutes_remaining = 25
        self.empty_tasks = []
        
    def tasks(self):
        self.pomodoro_session = self.pomodoro_session + 1
        i = 4
        
        while len(self.empty_tasks) != i:
            user_input = input("What four tasks would you like to complete during this 25 minute Pomodoro session? ")
            self.empty_tasks.append(user_input)
            print(self.empty_tasks)
            # print(len(self.empty_tasks)) - can be deleted
            
            if len(self.empty_tasks) == i:
                time.sleep(2)
                print("Now that you have 4 items in the list, let's start the 25 minute timer.")

        self.printit()

    def testtimer(self):
        while self.minutes_passed < 25:
            self.minutes_passed = self.minutes_passed + 1
            self.minutes_remaining = self.minutes_remaining - 1
            if self.minutes_passed == 1:
                print(str(self.minutes_passed) + " minute has passed. There are " + str(self.minutes_remaining) + " minutes remaining.")
            
            else:
                print(str(self.minutes_passed) + " minutes have passed. There are " + str(self.minutes_remaining) + " minutes remaining.")
            return self.printit()

    def printit(self):
        timer = threading.Timer(1, self.testtimer)
        timer.start()            
        self.twentyfiveminute()

    def twentyfiveminute(self):
        if self.minutes_passed == (25) and self.minutes_remaining == (0):
            print("Times up!")           
            self.checkthelist()

    def checkthelist(self):
        time.sleep(2)
        random_break = random.randrange(1, 15)  
        print("Let's check each item to see if you've completed the task." )
        self.tasks_completed = 0
        
        for i in self.empty_tasks[:]:
            
            if self.pomodoro_session > 5:
                continue
            takeinput = input("Were you able to complete the " + i + " task? " )
            
            # if takeinput != "n" and takeinput != "no" and takeinput != "yes" and takeinput != "y":
            #     print("That isn't a yes or a no. Please try again.")
            #     print(self.tasks_completed)
            #     self.checkthelist()

            if takeinput == "y" or takeinput == "yes":
                self.tasks_completed = self.tasks_completed + 1
                self.empty_tasks.remove(i)
                print(self.empty_tasks)
                print(self.tasks_completed)
                # elif takeinput != "n" and takeinput != "no" and takeinput != "yes" and takeinput != "y":
            #     print("That isn't a yes or a no. Please try again.")
            #     print(self.tasks_completed)
                # self.checkthelist()
            
            else:
                if takeinput == "n" or takeinput == "no":
                    print("Keeping " + i + " in the list since you did not complete it. ")
        
                    

        if self.empty_tasks == []:
                print("you've completed all tasks for this session! Good job! Let's take a 3-5 minute break and then start the next session.")
        else:
            if self.empty_tasks != []:
                print("Since you weren't able to complete your whole list, here's what remains: " + str(self.empty_tasks) + ". Let's take a 3-5 minute break and then start the next session. The next task will be added to the end of the list.")
         
    
        # print("Since you weren't able to complete your whole list, here's what remains: " + str(self.empty_tasks) + ". Let's take a 3-5 minute break and then start the next session. The next task will be added to the end of the list.")
        time.sleep(random_break)
        print("the current pomodoro session " + str(self.pomodoro_session))
          
        self.minutes_passed = 0
        self.minutes_remaining = 25
        print("This begins session # " + str(self.pomodoro_session))
        self.testfunction()
    

    def testfunction(self):
        if self.pomodoro_session == 4:
            restart_input = input("You have completed 4 Pomodoro sessions, great job! Would you like to start over? ")
            if restart_input == "y" or restart_input == "yes":
                print("Starting over at 0")
                self.pomodoro_session = 0
                self.empty_tasks = []
                return self.tasks()
            elif restart_input == "n" or restart_input == "no":
                    print("Good job on completing 4 Pomodoro sessions. Ending the program.")
                    
            else:
                if restart_input != "y" or restart_input != "yes":
                    print("This is not a correct input. Please try again.")
                    self.testfunction()
            return
        
        self.tasks()

    # def testfunction(self):
    #     if self.pomodoro_session == 4:
    #             restart_input = input("You have completed 4 Pomodoro sessions, great job! Would you like to start over? ")
    #             if restart_input == "y" or restart_input == "yes":
    #                 print("Starting over at 0")
    #                 self.pomodoro_session = 0
    #                 return self.tasks()
    #             elif restart_input == "n" or restart_input == "no":
    #                     print("Good job on completing 4 Pomodoro sessions. Ending the program.")
    #                     return
    #             else:
    #                 if restart_input != "y" or restart_input != "yes":
    #                     print("This is not a correct input. Please try again.")
    #                     return self.testfunction()
    #     return self.tasks()
        

clock = Pomodoro_Clock()
clock.tasks()
