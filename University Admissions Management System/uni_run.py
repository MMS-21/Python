import pandas as pd
data = {
    "Leadership": {
        "President/Captain": 10,
        "Vice President/Co-Captain": 8,
        "Officer/Team Leader": 6,
        "Committee Chair": 5
    },
    "Achievement": {
        "Awards or Honors": 8,
        "Major Accomplishments": 6, 
        "Publications, Patents, or Research": 7 
    },
    "Participation": {
        "Regular Involvement (2+ years)": 4, 
        "Consistent Involvement (1-2 years)": 3,
        "Occasional Involvement": 1
    }
}

exc = pd.DataFrame(data).stack().reset_index()
extra = exc.columns =['Extracurricular Category', 'Activity Level', 'Points']
print(exc)

while True:
    print("""\033[1;36mUniversity Admissions Management System: 
            Choose an action form the list below:   
                1-> Add Applicant
                2-> Analyze Applicant Data
                3-> Generate Admissions Report
                4-> Exit""")
    break

""" Accepted: If the total score were more than 799, the applicant would be placed on the Accepted list.
    Waiting List: If the total score were between 700 and 799, the applicant would be placed on the waiting list.
    Rejected: If the total score were below 700, the applicant would be rejected."""


"""Scoring the Criteria:
GPA:
Convert GPA to a numerical value (e.g., 4.0 scale).
Multiply the GPA by 100 to get a score between 0 and 400.

SAT Score:
Convert SAT score to a numerical value (e.g., out of 1600).
Multiply the SAT score by 0.25 to get a score between 0 and 400.

Extracurricular Activities:
Assign points based on the quality and quantity of activities. 

For example:
Leadership roles: 5 points
Significant involvement: 3 points
Minor involvement: 1 point
"""