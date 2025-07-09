 -----   
# Admissions Management System For University 
---
## Project OverView:
This Python project is an Admissions Management System For University that allows users to add new applications, And view them,Doing analysis on them to specify who accepted and who is not.The system provides a simple and efficient way to manage Applicants data.
## Acceptence Criteria:
### Scoring the Criteria:
*  GPA:
   * Convert GPA to a numerical value (e.g., 4.0 scale).
Multiply the GPA by 100 to get a score between 0 and 400.

* SAT Score:
  * Convert SAT score to a numerical value (e.g., out of 1600).
Multiply the SAT score by 0.25 to get a score between 0 and 400.

 * Extracurricular Activities:
    *  Assign points based on the quality and quantity of activities. 

 *  For example:
     * Leadership roles: 10 points

     * Significant involvement: 7 points

     *  Minor involvement: 5 point

* Accepted:
    * If the total score were more than 700, the applicant would be placed on the Accepted list.
* Waiting List:
    * If the total score were between 625 and 699, the applicant would be placed on the waiting list.
* Rejected:
    * If the total score were below 625, the applicant would be rejected

## Flowchart Components
* Start
* Display Menu: 
   * Options for "Add Applicant,"
   * "Analyze Applicant Data,"  
   * "Generate Admissions Report," 
   * and "Exit."
* Choice Decision:
 Based on the user’s selection, the flowchart branches out to different actions.
* Add Applicant
    * Input applicant data
    * Store data in the list
* Analyze Applicant Data
    * Compare each applicant’s data with the criteria
    * Mark as "Qualified" or "Not Qualified"
* Generate Admissions Reports
    * Assign "Accepted" or "Rejected" based on the analysis
    * Count and display accepted, rejected, and waitlisted applicants
* Exit
  * Terminate the program
* Loop Back to Menu after each task until the user selects "Exit."
* End
## Explanation of the Functions
* add_applicants():
  -  This function collects applicant data and stores it in a list. The data is appended to the main list of applicants.
* analysis(): 
  * This function checks each applicant against defined thresholds (GPA, SAT score, extracurricular activities) and appends itial analyses to each applicant's data wether he is qualified or not.
* generatereport(): 
  - This function prints the admissions decisions for all applicants and provides statistics on the number of accepted, waitlisted, and rejected applicants.
* main():
  - This is the main loop that handles user input and calls the appropriate functions based on the user's choice.
## Execution and Output
You can run the program and interact with it through the terminal or command line. Each step will prompt you for input, and the results will be displayed accordingly.

## Challenges and Solutions
* Data Validation:
   <p> Ensuring the input data is valid (GPA and SAT is within a reasonable range) is essential.and Ensuring that the Extracurricular Activities is input in a valid format</p>

* Modularity: 
   <p>Keeping the program modular allows for easier maintenance and updates, such as changing the criteria for admissions or adding new features.</p>

----

## Flow Chart Graph    
```    
+--------------------+
|       Start        |
+--------------------+
        |
        v
+--------------------+
|  Display Menu      |
+--------------------+
        |
        v
+--------------------+     
| User Chooses Option|
+--------------------+
     /   |   |   \
    /    |   |    \
   /     |   |     \
  v      v   v      v
[Option1][Option2][Option3][Option4]
  |      |   |      |
  v      v   v      v
+---------+ +----------+ +-----------+ +----------+
| Add     | | Analyze  | | Generate  | | Exit     |
| Applicant| | Applicant| | Report    | |          |
+---------+ +----------+ +-----------+ +----------+
  |         |             |             |
  v         v             v             v
+--------------------+ +-----------------------+
| Store Applicant    | | Compare Against        |
| Data in List       | | Criteria & Assign      |
|                    | | Admission Decision     |
+--------------------+ +-----------------------+
  |                     |
  v                     v
+-------------------+ +----------------------+
| Return to Menu    | | Return to Menu       |
+-------------------+ +----------------------+
  |                     |
  v                     v
+-------------------+ +----------------------+
| Display List of   | | Calculate & Display  |
| Applicants &      | | Admission Statistics |
| Decisions         | +----------------------+
+-------------------+
  |
  v
+-------------------+
| Return to Menu    |
+-------------------+
  |
  v
+-------------------+
|      End          |
+-------------------+
```
---- 
## Screen Shots of the program running

### First Action Adding 
![alt text](<Screenshot 2024-08-19 215328-1.png>) 
![alt text](<Screenshot 2024-08-19 215032-1.png>)
### Second Action Analysis
![alt text](<Screenshot 2024-08-19 215231-1.png>)
### Third Action Reporting
![alt text](<Screenshot 2024-08-19 215317-1.png>)
### Final Action Quit
![alt text](<Screenshot 2024-08-19 215328-1-1.png>)