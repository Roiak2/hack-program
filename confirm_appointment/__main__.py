#!/usr/bin/env python

"""
Comman line argparse for confirm_appointment
"""

#importing pacakge
import argparse
from confirm_appointment import confirm

#defining function to parse arguments
def parse_arguments():

    """
    Parses command line arguments using argparse
    """
    #init the argparse class object
    parser = argparse.ArgumentParser()

    #parse arguments from confirm_appointment function
    parser.add_argument(
        "--YES",
        action = "store_true",
        help = "confirm appointment"
    )

    parser.add_argument(
        "--NO",
        action = "store_true",
        help = "cancel appointment"
    )

    parser.add_argument(
        "--STOP",
        action = "store_true",
        help = "Stop receiving messages about appointment"
    )

    #returns argument dict-like object containing user arguments
    args = parser.parse_args()
    
    #checks user only entered one action argument
    if sum([args.YES, args.NO, args.STOP]) > 1:
        raise SystemExit(
            "Only one argument (YES, NO, or STOP) at a time please"
        )
    
    #return to user
    return args

#define funciton to run our confirm appointment program
def main():
    "Runs the command line program"

    #get command line arguments
    args = parse_arguments()
    
    #if user inputs YES, feed YES into function
    if args.YES:
        confirm("YES")
    #same with NO or STOP
    if args.NO:
        confirm("NO")
    if args.STOP:
        confirm("STOP")

#Execute to confirm
if __name__ == "__main__":
    confirm("YES")
