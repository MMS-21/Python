import pandas as pd
import random
import re

# this dict contains categories of the Extracurricular Activity
data = {
    "Leadership": [
        "President/Captain",
        "Vice President/Co-Captain",
        "Officer/Team Leader"
        
    ],
    "Achievement": [
        "Awards Or Honors",
        "Major Accomplishments", 
        "Publications, Patents, Or Research" 
    ],
    "Community Service": [
        "Regular Involvement (2+ Years)", 
        "Consistent Involvement (1-2 years)",
        "Occasional Involvement"
    ]
}
exc = pd.DataFrame.from_dict(data)
# This  2D list contains the values of each category assigned to the columns names
data_cat = [['Leadership','Achievement','Community Service'],[10,7,5]]


## -> A function to make the user able to add the data of the applicants
def add_applicants(applicants):
    # fetching data from the applicants to start making my Admission management system
    while True:
        name = input("Enter Application Name: ")
        # using regular expression to ensure that the name does not contain any numbers 
        if name and not re.search(r'\d', name):
            try:
                # Accepting the float values beacuse most of the GPA is in this format
                gpa = float(input("Enter Applicant's GPA: "))
                # Ensuring that the gpa is high enough
                if 2.0 < gpa < 4.1:
                    sat = int(input("Enter Applicant's SAT Score: "))
     
                    # Ensure the SAT Value is reasnable
                    if 500 < sat <= 1600:
                        # EX Acticities is very crucial for applicant admission process
                        print("Do You Participate in any Extracurricular Activity: ")
                        # lowering the input and stripping it from any white spaces
                        answer = input("""1-> yes\n2-> no\n-> """).lower().strip()
                        if answer == "no" or answer == "2":
                            # Extracurricular Points is Zero because the applicant did not participate at any
                            extras = ''
                            extras_points = 0
                            break
                        else:
                            # Providing the applicant with a list of categories with their most popular points
                            print("Enter applicant's extracurricular activities (comma separated) From Table Below:")
                            # Table to choose the Activities of the extracurricular from
                            print(exc.to_markdown(index=False))
                            # Ensuring the process of having the write input
                            try:
                                extras = input("\n Enter Your Activities-> ").title().split(',')
                            except:
                                # Printing Warning message
                                print("\x1b[3;31;43mPlease Add The activities Without spaces in between in this way: First_Activity,Second_Activity,Third_Activity\x1b[0m")
                                #The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
                                continue                                                          
                        # To break out of the loop
                        break
                    else:
                        # Warning message
                        print("SAT score is not valid. Please enter a score between 500 and 1600.")
                else:
                    # Warning message
                    print("GPA is not valid. Please enter a GPA between 2.0 and 4.0.")               
            except ValueError:
                    # Warning message
                    print("invalid Input, Please ensure that GPA is a number and SAT is an integer")
        else:
            # Warning message
            print("INVALID NAME, PLEASE ENTER A NAME WITHOUT NUMBERS OR SIGNS")
            break

    # Using Random with this range to give a random id with six digits
    unique_id = random.randint(10000,999999)
    # the backbone list that contains everyone of the applicants data
    application = [unique_id ,name, gpa, sat, extras]

    # Ensuring that the list is not Empty
    if not applicants:
        # If the list is empty it will take this action
        applicants.append(application)
        # utalizing 2D list to store applicant data 
    else:
        # If the list is not empty python will take this action too
        applicants.append(application)
    # confirming the user that every thing is done as required
    print((f"Applicant '{name.capitalize()}' added successfully."))
    # Returning to  the main manu
    print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
    
def analysis(applicants):
    # Ensuring that this action can not be done without the applicants data is added
    if not applicants:
        # Warning message
        print("\x1B[1;30;44mInvalid Action. Please Add Some Values First.\x1B[0m")
        print("\x1b[3;31;46m RETURNING TO THE MAIN MENU\x1b[0m")
    else:    
        # Function to extract values from the 2D Lists Using index
        def findvaluesindex(myList, v):
            # Using Enumerate i can make an index for each value in a list, this helps with getting the index 
            # Because of the nature of the 2D values i have to  know which list my values are in and the locate the vlues within these lists
            # the (i) is index for the the lists within list and the (x) is the index for the values inside each of these lists
            for i, x in enumerate(myList):
                if v in x:
                # Adding 1 to index to get the second list
                    return (i+1, x.index(v))

        df = pd.DataFrame(applicants,columns=['ID', 'Name','GPA Score','SAT Score','Extracurricular Activity'])
        # Initializing an empty column to store the values of the activities points
        df["Activity Total Points"] = 0
        # Initializing an empty column of the total points
        df["Total Points"] = 0
        #INTIATING A LOOP FOR THE LIST VLAUES
        # trying to give each value of the list a value to make me able to iterate correctly in it
        # Using Enumerate i can make an index for each value in a list, this helps with getting the index 
        for idx, activity in enumerate(df['Extracurricular Activity']):
            # Creating an empty list to store the correspondent category of each choice
            categories = []
            # the .at[] is used to access the df rows at specific index                              
            df.at[idx,"Activity Total Points"] = 0
            # To store the final result
            extras_points = 0
            df.at[idx,'First Analysis'] = ''
            df.at[idx,"Total Points"] = 0
            # Making sure that the user did not input values that does not fall in the categories
            for i in activity:
                # Getting  the correspondent Column name of every extracurricula activity
                category_name = (exc.columns[exc.isin([f'{i}']).any()])[0]
                # Appending columns names into other list to start calulating the values of this activities 
                categories.append(category_name)
            # Iterating through the categories to calculate the values
            for r in categories:
                # using the function created to get the correspondent values of each indexes
                # because we have a 2d lists we need to get the values in this way
                index1, index2 = findvaluesindex(data_cat,r)
                # getting the values needed
                corrvalues = data_cat[index1][index2]
                # incrementing the values by adding them on each other
                extras_points += corrvalues
            # the .at[] is used to access the df rows at specific index                               
            df.at[idx,"Activity Total Points"] = extras_points
            # Formula that is used to sepcify in which category the applicant falls 
            # wether the applicant qualified or not
            # wether the applicant accepted, waitlisted, or rejected
            total_points = ((df.at[idx,"GPA Score"]*100 )+ df.at[idx,"Activity Total Points"] +(df.at[idx,"SAT Score"]*0.25))
            # assigning the results to its place in the dataframe column accoriding of its index
            df.at[idx,"Total Points"] = total_points
            
            # Conditional statement to catogrize the applicants
            if total_points >= 700:
                df.at[idx, 'First Analysis'] = 'Qualified'
            else:
                df.at[idx, 'First Analysis'] = 'Not Qualified'


        # printing the first analyses of the  applicants data wether they are qaulified enough to be accepted
        print(df[['ID', 'Name','GPA Score','SAT Score',"Activity Total Points","Total Points","First Analysis"]].to_markdown(index=False))
        # confirming that the analysis is done
        print("\033[38;2;1mApplicant data analyzed successfully.\x1b[0m")
        # # Returning to  the main manu
        print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
    


def generatereport(applicants):
    # Ensuring that this action can not be done without the applicants data is added
    if not applicants:
        # warning messag
        print("\x1B[1;30;44mInvalid Action. Please Add Some Values First.\x1B[0m")
        print("\x1b[3;31;46m RETURNING TO THE MAIN MENU\x1b[0m")
    else:
        # Function to extract values from the 2D Lists Usin index
        def findvaluesindex(myList, v):
            # Using Enumerate i can make an index for each value in a list, this helps with getting the index 
            # Because of the nature of the 2D values i have to  know which list my values are in and the locate the vlues within these lists
            # the (i) is index for the the lists within list and the (x) is the index for the values inside each of these lists
            for i, x in enumerate(myList):
                if v in x:
                    # Adding 1 to index to get the second list
                    return (i+1, x.index(v))
        # creating a df to start the analysing phase
        df = pd.DataFrame(applicants,columns=['ID', 'Name','GPA Score','SAT Score','Extracurricular Activity'])
        # Creating an empty list to store the correspondent category of each choice
        df["Activity Total Points"] = 0
        #INTIATING A LOOP FOR THE LIST VLAUES
        # trying to give each value of the list a value to make me able to iterate correctly in it
        # Using Enumerate i can make an index for each value in a list, this helps with getting the index 
        for idx, activity in enumerate(df['Extracurricular Activity']):
            # Creating an empty list to store the correspondent category of each choice
            categories = []
            # the .at[] is used to access the df rows at specific index                              
            df.at[idx,"Activity Total Points"] = 0
            # To store the final result
            extras_points = 0
            df.at[idx,'First Analysis'] = ''
            df.at[idx,"Total Points"] = 0
            # Making sure that the user did not input values that does not fall in the categories
            for i in activity:
                # Getting  the correspondent Column name of every extracurricula activity
                category_name = (exc.columns[exc.isin([f'{i}']).any()])[0]
                # Appending columns names into other list to start calulating the values of this activities 
                categories.append(category_name)
            # Iterating through the categories to calculate the values
            for r in categories:
                # using the function created to get the correspondent values of each indexes
                # because we have a 2d lists we need to get the values in this way
                index1, index2 = findvaluesindex(data_cat,r)
                # getting the values needed
                corrvalues = data_cat[index1][index2]
                # incrementing the values by adding them on each other
                extras_points += corrvalues
            # the .at[] is used to access the df rows at specific index                               
            df.at[idx,"Activity Total Points"] = extras_points
            # Formula that is used to sepcify in which category the applicant falls 
            # wether the applicant accepted, waitlisted, or rejected
            total_points = ((df.at[idx,"GPA Score"]*100 )+ df.at[idx,"Activity Total Points"] +(df.at[idx,"SAT Score"]*0.25))
        
            # Conditional statement to catogrize the applicants            
            if total_points < 625:
                df.at[idx, 'Final Result'] = 'Rejected'
            elif total_points >= 700:
                df.at[idx, 'Final Result'] = 'Accepted'
            elif 625 < total_points < 699 :
                df.at[idx, 'Final Result'] = 'Waitlisted'

        # Creating a side menu that can offers Summary or Report        
        while True:
            # asking the user to specify his choice
            print("""\x1B[1;30;43mWelcome To The Reports Generating Department:\x1B[0m
                Select Your Next Actions From List Below:
                1-> Genrating A Summary
                2-> Generating A Final Report About All applicants""")
            # Intializing a variable to store the users input
            schoice = input("Enter Your Selection (1 or 2): ")
            if schoice == "1":
                print()
                # generating the users reports
                print("\x1b[3;31;42mSummary\x1b[0m")
                print(df['Final Result'].value_counts(ascending=False))
                print()
                break

            else:
                # Generating the final report about the accepted applicants or the rejeceted
                print("\x1B[1;30;44mApplicants Final Reports.\x1B[0m")
                print(df[['ID', 'Name','Final Result']].to_markdown(index=False))
                print("\x1B[1;30;44mApplicants Final Reports Ended.\x1B[0m")
                print()
                break
        print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")

def main():
    # an empty list to store the applicants data
    applicants = []
    
    while True:
        print("""\033[1;35m Welcome To University Admissions Management System:\x1b[0m 
            Choose an action form the list below:   
                1-> Add Applicant
                2-> Analyze Applicant Data
                3-> Generate Admissions Report
                4-> Exit""")
        
        choice = input("Enter Your Choice: ")
            
        if choice == "1":
            add_applicants(applicants)
        elif choice == "2":
            analysis(applicants)
        elif choice == "3":
            generatereport(applicants)
        elif choice == '4':    
            print(("\x1B[1;30;47mExiting the program, GOODBYE!\x1B[0m"))
            break
        else:   
            print(("\x1B[1;30;45mInvalid Option. Please enter a number between 1 and 4.\x1B[0m"))


if __name__ == "__main__":
     main()