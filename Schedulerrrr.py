print("-Hello, I am your schedular");
totalHours = 16

freeHours = totalHours;
meetingHours = 0.0
workingHours = 0.0
homeworkHours = 0.0
universityHours = 0.0


# --------------------------------------- functions ------------------------------------------------
        #---------------------- checkMeeting ----------------------
def checkMeeting(ifMeeting):
    if (ifMeeting == "yes"):
        global meetingHours
        meetingDuration = input("Meeting duration ? (min/avg/max) ").lower();
        if (meetingDuration == "min"):
            meetingHours = 0.5
        elif (meetingDuration == "avg"):
            meetingHours = 1.0
        else:
            meetingHours = 1.5
        print("You have meeting with " + meetingDuration + " duration.")
        print("Meeting hours: ", meetingHours)
        global freeHours
        freeHours -= meetingHours
    else:
        print("No meeting scheduled.\nMeeting hours: 0")

        #--------------------- checkWorking ----------------------

def checkWorking(ifWorking) :
    if (ifWorking == "yes"):
        global workingHours
        workingHours = 8
        print("Working hours: 8");
        global  freeHours
        freeHours -= workingHours
    else:
        print("Not working today");
        print("Working hours: 0");
        print("HomeWork/University:");

        #---------------------- checkHomework ----------------------

def checkHomefork(ifHomework) :
    if (ifHomework == "yes"):
        global homeworkHours
        homeworkDuration = input("homework duration ? (min/avg/max) ").lower();
        if (homeworkDuration == "min"):
            homeworkHours = 1.0
        elif (homeworkDuration == "avg"):
            homeworkHours = 2.0
        else:
            homeworkHours = 3.0
        print("You have homework with " + homeworkDuration + " duration.")
        print("Homework hours: ", homeworkHours)
        global freeHours
        freeHours -= homeworkHours
    else:
        print("No homework scheduled.\nHomework hours: 0")

        #---------------------- checkUniversity

def checkUniversity(ifUniversity) :
    if (ifUniversity == "yes"):
        global universityHours
        universityDuration = input("which schedule ? (1/2) ").lower();
        if (universityDuration == "1"):
            universityHours = 2.5
        else:
            universityHours = 3.5
        print("You have university lessons with " + universityDuration + " duration.")
        print("University hours: ", universityHours);
        global freeHours
        freeHours -= universityHours
    else:
        print("No university lessons today");
        print("University hours: 0");

def printAll() :
    print("\n----Summary----")
    print("Meeting hours: ", meetingHours)
    print("Working hours: ", workingHours)
    print("Homework hours: ", homeworkHours)
    print("University hours: ", universityHours)
    print("--------")
    print("Total: ", totalHours - freeHours, "\n")

    if (freeHours < 0.0):
        print("Too much work to do!!", "+", -freeHours, "hrs.")
    else:
        print("You have ", freeHours, "hrs. to Chill.");


#----------------------------------------------------------------------------------------------

print("Meeting/Working:");
# Meeting related code
ifMeeting = input("Will you have meeting today ? (yes/no) ").lower();
checkMeeting(ifMeeting)

# Working related code ----------------------------------------------------------

ifWorking = input("Will you work today ? (yes/no) ").lower();
checkWorking(ifWorking)

# Homework related code-----------------------------------------------------------

ifHomework = input("Will you do homework today ? (yes/no) ").lower();
checkHomefork(ifHomework)

# University related code---------------------------------------------------------

ifUniversity = input("Will you have university lessons today ? (yes/no) ").lower();
checkUniversity(ifUniversity)

printAll()




