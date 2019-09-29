import time
import threading
import random
 #    Decide on the task to be done. - input 4 tasks that the user wants to complete. these tasks should be stored in a list? ask the user for the input, and append the input to a list until the list has 4. 
#     Set the pomodoro timer (traditionally to 25 minutes).[1] - after the list has 4 items, start a time for 25 minutes. probably has to use the datetime module
#     Work on the task. 
#     End work when the timer rings and put a checkmark on a piece of paper. - after the timer ends verify if the user has completed all 4 of there inputted tasks. iterate through the list and ask have you completed this item? y or no. if all 4 are not y then move to step 5.
#     If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2. - if 4 checkmarks havent been done take a random interval 3-5 minute break. if not then loop the program back to #2 and do another 25 minutes. 
#     After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1. - after 4 pomodoros take a longer 15-30 minute random timed interval break, clear out the list and restart the program. 

#add some type of option to see how much time is left


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
            user_input = input("What four tasks are you wanting to complete during this 25 minute Pomodoro period? ")
            self.empty_tasks.append(user_input)
            print(self.empty_tasks)
            print(len(self.empty_tasks))
            
            if len(self.empty_tasks) == i:
                time.sleep(2)
                print("The 25 minutes will now begin")

        self.printit()

    def testtimer(self):
        while self.minutes_passed < 25:
            self.minutes_passed = self.minutes_passed + 1
            self.minutes_remaining = self.minutes_remaining - 1
            print(str(self.minutes_passed) + " minutes has passed. There are " + str(self.minutes_remaining) + " minutes remaining.")
            return self.printit()

    def printit(self):
        
        timer = threading.Timer(1, self.testtimer)
        timer.start()            
        self.twentyfiveminute()

    def twentyfiveminute(self):
        if self.minutes_passed == (25) and self.minutes_remaining == (0):
            print("times up")           
            self.checkthelist()

    def checkthelist(self):
        time.sleep(2)
        random_break = random.randrange(1, 15)  
        print("Let's check each item to see if you've completed the task." )
        
        for i in self.empty_tasks[:]:
            if self.pomodoro_session > 5:
                continue
            takeinput = input("Were you able to complete the " + i + " task? " )
            
            # if takeinput != "n" and takeinput != "no" and takeinput != "yes" and takeinput != "y":
            #     print("That isn't a yes or a no. Please try again.")
            #     print(self.tasks_completed)
            #     self.checkthelist()

            if takeinput == "y" or takeinput == "yes":
                self.tasks_completed = 0
                self.tasks_completed = self.tasks_completed + 1
                self.empty_tasks.remove(i)
                print(self.empty_tasks)
                print(self.tasks_completed)

            elif takeinput != "n" and takeinput != "no" and takeinput != "yes" and takeinput != "y":
                print("That isn't a yes or a no. Please try again.")
                print(self.tasks_completed)
                self.checkthelist()
            
            else:
                if takeinput == "n" or takeinput == "no":
                    print("keeping " + i + " in the list since you did not complete it. ")
                    # continue

            if self.empty_tasks == []:
                    print("youve completed all tasks for this session! Good job! Let's take a 3-5 minute break and then start the next session.")
            else:
                if self.empty_tasks == self.empty_tasks[:1]:
                    print("Since you weren't able to complete your whole list, here's what remains: " + str(self.empty_tasks) + ". Let's take a 3-5 minute break and then start the next session. The next task will be added to the end of the list.")
                    self.checkthelist()
                


            
        
        # print("Since you weren't able to complete your whole list, here's what remains: " + str(self.empty_tasks) + ". Let's take a 3-5 minute break and then start the next session. The next task will be added to the end of the list.")
        time.sleep(random_break)
        print("the current pomodoro session " + str(self.pomodoro_session))
          
        self.minutes_passed = 0
        self.minutes_remaining = 25
        print("this is the " + str(self.pomodoro_session) + " iteration")
        if self.pomodoro_session == 4:
            restart_input = input("You have completed 4 Pomodoro sessions, great job! Would you like to start over?")
            if restart_input == "y" or takeinput == "yes":
                print("Starting over at 0")
                self.pomodoro_session = 0
                return self.tasks()
            else:
                if restart_input != "y" or restart_input != "yes":
                    print("Good job on completing 4 Pomodoro sessions. Ending the program.")
            return
        return self.tasks()


clock = Pomodoro_Clock()
clock.tasks()
