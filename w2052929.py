# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# References: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
# UOW Username: w2052929 # UOW Student ID: 20529293 # IIT Student ID: 20221921
# Name: MUHAMMED SAAJID IMTIYAZ AHAMED
# Date: 11/12/2023

from graphics import * # importing the graphics module

# initializing variables
credit_range = [0,20,40,60,80,100,120]
progress = 0
progress_list = []
progress_str = ""
trailer = 0
trailer_list = []
trailer_str = ""
retriever = 0
retriever_list = []
retriever_str = ""
excluded = 0
excluded_list = []
excluded_str = ""

x1 = 60 # starting x-cordinate of first bar (from left)
x2 = 120 # ending x-cordinate of first bar 
space = 150 # value for the space between the bars
y1 = 100 # value for the first y coordinate (top-start height)
y2 = 420 # value for the second y coordinate (bottom-end height)
h_difference = y2 - y1 # difference between the top and bottom height of the bar

# function to generate title text in graphics window
def setTitle(x_cordinate,y_cordinate,title,textSize=10,text_color="white"):
        """This user-defined function generates any number of title text in the graphics window"""
        bar_title = Text(Point(x_cordinate,y_cordinate), title)
        bar_title.setFace("arial")
        bar_title.setStyle("bold")
        bar_title.setTextColor(text_color)
        bar_title.setSize(textSize)
        bar_title.draw(win)

# function to generate bars for the histogram and to display the values on top
def createBar(x1_cordinate,x2_cordinate,percentage,color,bar_value):
        """This user-defined function creates the bars and the displays the values above the bars"""
        point1 = Point(x1_cordinate, y1 + (h_difference * (1.00 - percentage)))
        point2 = Point(x2_cordinate,y2)
        rectangle_bar = Rectangle(point1,point2)
        rectangle_bar.setFill(color)
        rectangle_bar.draw(win)
        if bar_value != 0:
            bar_title2 = Text(Point((x1_cordinate + x2_cordinate) / 2, y1 + (h_difference * (1.00 - percentage)) - 20),str(bar_value))
            bar_title2.setTextColor("white")
            bar_title2.setSize(12)
            bar_title2.draw(win)
        else: 
            pass

# function to format the list data and to display it
def formatList(list_variable,result_type):
    """User-defined function to retrieve data from a nested list, format the data in a specific way and to display that data"""
    for i in list_variable:
        new_str = str(i).replace("[","").replace("]","") # this converts each list items to string format & removes the square brackets from it.
        print(f"{result_type} - {new_str}")
        # below code segment will concatenate the result to string variables based on the result type. this will be used for the text file extension later.
        if result_type.lower() == "progress":
            global progress_str
            progress_str += f"{result_type} - {new_str}\n"
        elif result_type.lower() == "progress (module trailer)":
            global trailer_str
            trailer_str += f"{result_type} - {new_str}\n"
        elif result_type.lower() == "module retriever":
            global retriever_str
            retriever_str += f"{result_type} - {new_str}\n"
        elif result_type.lower() == "exclude":
            global excluded_str
            excluded_str += f"{result_type} - {new_str}\n"
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Part 01 - A, B, & C 
# Getting user inputs and determining the outcomes
print("WELCOME TO THE UNIVERSITY PROGRESSION PREDICTION SYSTEM!\n\nPLEASE NOTE:\n1. If you are a student you will be able to only predict your progression outcome (ONLY ONCE).\n2. If you are a staff member you will be able to predict progression outcomes of multiple students (PROGRAM WILL LOOP),\n and will have access to the histogram feature, List extension feature, & file extension feature.\n")
while True:
    title_input = input("Enter your title (STUDENT/STAFF): ").lower()
    while title_input in ["student","staff"]:

        while True:
            try:
                pass_input = int(input("Please enter your credits at PASS: "))
                if pass_input not in credit_range:
                    print("Out of range")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")
                continue

        while True:
            try:
                defer_input = int(input("Please enter your credits at DEFER: "))
                if defer_input not in credit_range:
                    print("Out of range")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")
                continue

        while True:
            try:
                fail_input = int(input("Please enter your credits at FAIL: "))
                if fail_input not in credit_range:
                    print("Out of range")
                    continue
                else:
                    break
            except ValueError:
                print("Integer required")
                continue

        if (pass_input == 120 and defer_input == 0 and fail_input == 0):
            print("Progress")
            progress += 1
            progress_list.append([pass_input,defer_input,fail_input])
        elif ((pass_input == 100 and defer_input == 20 and fail_input == 0) or (pass_input == 100 and defer_input == 0 and fail_input == 20)):
            print("Progress (module trailer)")
            trailer += 1
            trailer_list.append([pass_input,defer_input,fail_input])
        elif ((pass_input == 80 and defer_input == 40 and fail_input == 0)  or (pass_input == 80 and defer_input == 20 and fail_input == 20) or (pass_input == 80 and defer_input == 0 and fail_input == 40) or (pass_input == 60 and defer_input == 60 and fail_input == 0) or (pass_input == 60 and defer_input == 40 and fail_input == 20) or (pass_input == 60 and defer_input == 20 and fail_input == 40) or (pass_input == 60 and defer_input == 0 and fail_input == 60 ) or (pass_input == 40 and defer_input == 80 and fail_input == 0) or (pass_input == 40 and defer_input == 60 and fail_input == 20) or (pass_input == 40 and defer_input == 40 and fail_input == 40) or (pass_input == 40 and defer_input == 20 and fail_input == 60) or (pass_input == 20 and defer_input == 100 and fail_input == 0) or (pass_input == 20 and defer_input == 80 and fail_input == 20) or (pass_input == 20 and defer_input == 60 and fail_input == 40) or (pass_input == 20 and defer_input == 40 and fail_input == 60) or (pass_input == 0 and defer_input == 120 and fail_input == 0) or (pass_input == 0 and defer_input == 100 and fail_input == 20) or (pass_input == 0 and defer_input == 80 and fail_input == 40) or (pass_input == 0 and defer_input == 60 and fail_input == 60)):
            print("Do not progress (module retriever)")
            retriever += 1
            retriever_list.append([pass_input,defer_input,fail_input])
        elif ((pass_input == 20 and defer_input == 0 and fail_input == 100) or (pass_input == 20 and defer_input == 20 and fail_input == 80) or (pass_input == 40 and defer_input == 0 and fail_input == 80) or (pass_input == 0 and defer_input == 40 and fail_input == 80) or (pass_input == 0 and defer_input == 20 and fail_input == 100) or (pass_input == 0 and defer_input == 0 and fail_input == 120)):
            print("Exclude")
            excluded += 1
            excluded_list.append([pass_input,defer_input,fail_input])
        elif pass_input + defer_input + fail_input != 120: 
            print("Total incorrect")

        if title_input == "student":
            break
        else:
            playAgain_input = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
            if playAgain_input == "y":
                print()
                continue
            else:
                print("\nHistogram will be generated. please close the histogram pop-up window to run the PART 02 & PART 03 sections of this code!\n")
                break

    if title_input not in ["staff","student"]:
        print("Please enter a valid title")
        continue
    else:
        break
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Part 01 - D
if title_input == "staff":
# Initializing variables required for generating the histogram
    max_count = max(progress, trailer, retriever, excluded)
    total_outcomes = progress + trailer + retriever + excluded

    # Calculating percentages based on the maximum count
    if max_count != 0:
        prog_percentage = progress / max_count
        trail_percentage = trailer / max_count
        ret_percentage = retriever / max_count
        exc_percentage = excluded / max_count
    else:
        prog_percentage = 0
        trail_percentage = 0
        ret_percentage = 0
        exc_percentage = 0

    try:
        # Generating a window for histogram
        win = GraphWin("Histogram Result - (SAAJID AHAMED - w2052929)", 640, 480)
        # Setting the background colour of the window
        win.setBackground("black") 

        # Setting all the titles in the graphics window
        setTitle(325,30,"Histogram Results",20,"red")
        setTitle(x1+31,440,"Progress",10)
        setTitle(x1+(space)+31,440,"Trailer",10)
        setTitle(x1+(space*2)+31,440,"Retriever",10)
        setTitle(x1+(space*3)+31,440,"Exclude",10)
        setTitle(325,465,f"{total_outcomes} outcomes in total.",12,"red")

        # Creating bars in the graphics window
        createBar(x1,x2,prog_percentage,"darkblue",progress)
        createBar(x1+(space),x2+space,trail_percentage,"Tomato",trailer)
        createBar(x1+(space*2),x2+(space*2),ret_percentage,"pink",retriever)
        createBar(x1+(space*3),x2+(space*3),exc_percentage,"purple",excluded)

        # Drawin a line below the bars
        line = Line(Point(0,420),Point(800,420))
        line.setFill("white")
        line.draw(win)
        
        win.getMouse()
        win.close()

    except:
        pass
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Part 02: The users inputs that were appended in a nested list is displayed
    print("PART 02 (List Extension): ")
    formatList(progress_list,"Progress")
    formatList(trailer_list,"Progress (module trailer)")
    formatList(retriever_list,"Module retriever")
    formatList(excluded_list,"Exclude")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Part 03: Generating a text file and printing the data accessed from it
    with open("CreditsTextFile.txt","w") as file_access: # Opening the file in write mode
        file_access.write(f"Part 03 (Text file extension):\n{progress_str}{trailer_str}{retriever_str}{excluded_str}") # writing data to the file
    print("\nThe data has been written to the file successfully!")

    with open("CreditsTextFile.txt","r") as file_access: # Opening the file in read mode
        file_data = file_access.read().strip()
    print(f"\n{file_data}")
else:
    pass # program will skip the histogram, list extension, file extension if the user is not a STAFF member 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
