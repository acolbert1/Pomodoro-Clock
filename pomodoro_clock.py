import time
import threading
 #    Decide on the task to be done. - input 4 tasks that the user wants to complete. these tasks should be stored in a list? ask the user for the input, and append the input to a list until the list has 4. 
#     Set the pomodoro timer (traditionally to 25 minutes).[1] - after the list has 4 items, start a time for 25 minutes. probably has to use the datetime module
#     Work on the task. 
#     End work when the timer rings and put a checkmark on a piece of paper. - after the timer ends verify if the user has completed all 4 of there inputted tasks. iterate through the list and ask have you completed this item? y or no. if all 4 are not y then move to step 5.
#     If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2. - if 4 checkmarks havent been done take a random interval 3-5 minute break. if not then loop the program back to #2 and do another 25 minutes. 
#     After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1. - after 4 pomodoros take a longer 15-30 minute random timed interval break, clear out the list and restart the program. 

#add some type of option to see how much time is left
#to check if the item in the list has been completed, iterate through the list and check yes or no. if no then start the program

#ToDo
#0. Once the minutes get to 25, the timer needs to stop and go to the next step. 
#1.Add the ability to ask the user if they've completed all of there tasks. Check the empty_tasks list and iterate through each index asking yes or no.  
#2.If the user inputs no for any of the indexes, the program should time.sleep for a random period between 3-5 minutes and then the program should start a 25m timer again. 
#3.If the user has completed all 4 tasks then print a good job message and start from scratch again. This needs to happen a total of 4 times.
#4. Once the 4th pomodoro has completed, ask the user if they would like to continue and start another pomodoro, or are they done and would like to exit. Print a msg stating the program has ended. 

class Pomodoro_Clock:
    def __init__(self):
        self.minutes_passed = 0
        self.minutes_remaining = 25

    def tasks(self):
        empty_tasks = []
        i = 4
        
        while len(empty_tasks) != i:
            user_input = input("What four tasks are you wanting to complete during this 25 minute Pomodoro period? ")
            empty_tasks.append(user_input)
            print(empty_tasks)
            print(len(empty_tasks))
            
            if len(empty_tasks) == i:
                time.sleep(2)
                print("The 25 minutes will now begin")
                # self.timer()
        self.printit()
        

    # def restart_clock(self):
    #     timer = threading.Timer
    #     print("Did you complete all of your tasks?")
    # #     #check each item in the list and if completed move to the next, if the first is n then restart 25 minutes 

      

    def testtimer(self):
        
        self.minutes_passed = self.minutes_passed + 1
        self.minutes_remaining = self.minutes_remaining - 1
        print(str(self.minutes_passed) + " minutes has passed. There are " + str(self.minutes_remaining) + " minutes remaining.")
        if self.minutes_passed == (25) and self.minutes_remaining == (0):
            print("times up")
            # timer.cancel()
        return self.printit()

    def printit(self):
        timer = threading.Timer(1, self.testtimer)
        timer.start()
        return self.printit()


        

clock = Pomodoro_Clock()
clock.tasks()



