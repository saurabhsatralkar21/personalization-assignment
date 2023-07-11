# personalization-assignment
A personalization assignment based on Turtl doc. 

Small lightweight Flask application written in python that runs on the browser locally but makes API calls to the Turtl system with prior access. When run, follow the instructions on the browser. Select the .csv file with data and click "Create Personalization" button to create the personalization on your Turtl account from the Master doc.


# Dependancies:
- ```python pip3 install 'flask[async]' ``` - To perform asynchronious task
- A test CSV file.

# How to fullfill prerequisites and run?
- Clone the repository on your machine
- Install and add the dependancy above
- Create a directory in the project root folder as "credentials". Create a token.json file within the directory. Within token.json file, add your Bearer token. For example, copy paste the JSON code below in token.json file and add your API Bearer token:
```json { "Bearer_token": "Add your token here" } ```
- Run the command ```python flask run``` in the terminal
- Once the program is running on some port, follow the instructions on the browser