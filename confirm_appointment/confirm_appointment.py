#!/usr/bin/env python

"""
Functions of 
"""

#import packages
import random #to sample randomly
import datetime #to get dates and times
import numpy as np #to get list of numbers

#define function
def confirm(answer):
    """
    Function that asks patient to confirm, reject, or reschedule an appointment.
    After patient gives answer, function returns string response from doctor's office.

    Parameters
    ----------
    answer(str):
        "YES" to confirm
        "NO" to reject
        "STOP" to stop messaging
    
    Date = randomly sample appointment day
    Hour = randomly sample time
    """

    #Setting parameters to choose random appointment date and time
    #week = list("Mon","Tue","Wed","Thu","Fri") #set up weekdays
    #day = random.choice(week) #sample a day
    start_dt = datetime.date.today().replace(day=1, month=1).toordinal() #get current date
    end_dt = datetime.date.today().toordinal() #get end of year
    date = datetime.date.fromordinal(random.randint(start_dt, end_dt)) #random sample in range
     
    #get random timestamp for appointment
    random_hour = np.arange(9,18,0.5).tolist() #set list of hours
    hour = random.choice(random_hour) #sample one hour
    
    #Print prompt and ask for input
    print("You have an appointment scheuled for ",date,hour)
    print("Reply: YES to confirm, NO to cancel, STOP to stop receiving messages")
    
    #If patient says yes, confirm appointment
    if answer == "YES":
            print("Thank you for confirming. See you on, ", date,hour)
    #If patient says no thank them and bye bye    
    if answer == "NO":
        print("Thank you for cancelling. Goodbye!")
    #If patient asks to stop receiving messages say peace
    if answer == "STOP":
        print("You will stop receiving messages. Peace!")
    # #If input is incorrect, repeat prompt
    # else:
    #     print("I'm sorry, please write YES, NO, or STOP")
        

#Run function only when executed
if __name__ == "__main__":
    confirm("YES")