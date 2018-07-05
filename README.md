# Automated testing and utilities for Humboldt State University's Identity Management System
This project highlights the setup and usage of a continuous integration environment for Humboldt State University's Fischer International Identity Management System.

Date Started: 2017-11-07

Our testing environment includes the use of a Jenkins continuous integration server and the browser automation tool called Selenium. Using Python’s unittest and pytest libraries to write testing scripts that interact with the selenium server to test against the data presented in the DOM and/or frontend of the application.

Be sure that you setup your server environments to match your local environment. It’s very important that the software installed in both environments is the same, otherwise testing your scripts locally may produce different results when deployed to the remote servers.

#### Servers and associated ports:
You should have access to each of these server environments. If not talk to your friendly local sys-admin.

* [http://dw-autotest-dev.humboldt.edu:8080/job/Fischer/](http://dw-autotest-dev.humboldt.edu:8080/job/Fischer/) - Jenkins Development Dashboard
* [http://dw-autotest-prod.humboldt.edu:8080/job/Fischer/](http://dw-autotest-dev.humboldt.edu:8080/job/Fischer/) - Jenkins Production Dashboard
* [https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf](https://idm-prov-dev.humboldt.edu/identity/self-service/hsu/login.jsf) - Fischer User login 
* [https://idm-prov-dev.humboldt.edu/identity/admin/logon.html](https://idm-prov-dev.humboldt.edu/identity/admin/logon.html) - Fischer Admin login 
* [https://hr85513.cms.calstate.edu/psp/HBHUMSTG/?&cmd=login&languageCd=ENG&](https://hr85513.cms.calstate.edu/psp/HBHUMSTG/?&cmd=login&languageCd=ENG&) - PeopleSoft login 
* [http://dw-autotest-dev.humboldt.edu](http://dw-autotest-dev.humboldt.edu) – selenium dev server located here
* [http://dw-autotest-prod.humboldt.edu](http://dw-autotest-prod.humboldt.edu) – selenium prod server located here

Make sure you have python 2.7 on all your environments. Be sure to add it to your path variable.

#### Install python libraries:
* `pip install -U pytest`
* `pip install -U selenium`

#### Dw-autotest-dev:
* With: xvfb, selenium, and firefox installed on DISPLAY:99.
* Java version "1.7.0_101"
* This should be called on startup of the server: `java -jar .\selenium-server-standalone-3.4.0.jar`
* A softlink created at `/usr/bin/geckodriver` to point to `/usr/local/bin/geckodriver` it should work even if `/usr/local/bin` is not in the PATH of the Jenkins user. Please also make sure the port 4444 is open.

#### Selenium on dw-autotest-dev.humboldt.edu and dw-autotest-prod.humboldt.edu:
* Selenium is a browser automation tool, we’ll be using the Selenium Python library to write scripts that navigate “headlessly” on the server. While, locally we’ll be running selenium and launching an actual browser window on our machine to write and test our scripts.

## Testing With Selenium Locally

* You’ll want to download the selenium server, we happen to be using version 3.4.0
* Using the node packet manager you can download this jar file here:

`npm install selenium-server-standalone-jar@3.4.0`

* Install locally, for example: C:\selenium\selenium-server-standalone-3.4.0.jar
* Be sure to add this to your Path variable.
Pro tip: Make sure that any other zombie selenium servers from past runs are killed via the task manager before you start a fresh run of the server.

Run:

`java -jar .\selenium-server-standalone-3.4.0.jar`

* Navigate to the location where you have stored your tests. In my case I have a local version of the project’s repository. Ex: C:\Users\mkl177\projects\fischer-2017\fischer\test_cases
* In our tests we have a line at the top of each setup method that describes the driver being used and where that driver will live in the browser and on which port, in our case you can view active sessions on the Selenium server at: http://localhost:4444/wd/hub


You may specify a single test case by using this syntax: `pytest .\<script_name>.py`
Or
You can test the entire directory you are in for all python files with test in the name: `Pytest .`

This will kick off the pytest file collection process, it should look similar to this:

    `PS C:\Users\mkl177\projects\fischer-2017\fischer\test_cases> pytest .`
    ============================= test session starts =============================
    platform win32 -- Python 2.7.14, pytest-3.2.2, py-1.4.34, pluggy-0.4.0
    rootdir: C:\Users\mkl177\projects\fischer-2017\fischer\test_cases, inifile:
    collected x items`

* This should eventually open a new firefox browser and the tests will begin.
* You will see the browser change and modify values, it will open and close itself at the start and end of each test directly on your workstation in front of you.
* Once the tests have run it will report the status of each of these tests in the console.

###Git workflow

In order to have a better team workflow, we have devised a series of branches that will allow for team level collaboration, before merging into the Master. 

        Master
          |
        Sprint
        /    \
      Max     Josh

## Jenkins:
* Jenkins is our orchestrator. Like many tools it can have multiple projects running all at once.
* When you first login you’ll notice that there are quite a few projects listed. Select Fischer.
* Below are the different sections of the Jenkins Pipline specifically for our Fischer project. 
* You’ll find this under the URL: [http://dw-autotest-dev.humboldt.edu:8080/job/Fischer/configure](http://dw-autotest-dev.humboldt.edu:8080/job/Fischer/configure)
* We utilize Jenkins to perform testing in our server environment. For local testing view the section called: “Testing With Selenium Locally”

**Jenkins plugins:**

* Jenkins has a huge library of plugins to add functionality to your project. 
* Located: [dw-autotest-dev.humboldt.edu:8080/pluginManager/installed](dw-autotest-dev.humboldt.edu:8080/pluginManager/installed)

Besides the defaults plugins that come with new Jenkins installations we used:

* Various: Bitbucket plugins
* Email Extension Plugin v2.58
* Junit Plugin v1.20
* Mailer Plugin v1.20
* Slack Notification Plugin v2.2
* Test Results Analyzer Plugin v0.3.4

###Example Jenkins Job Setup

####General:
* The name should already be specified when you created the Job.
* General is a good place to keep notes and any job specific reminders/explanations.

####Source Code Management:
* Once Jenkins has made a connection to source control, it needs a branch to be specified. In our case, we want the newest version, so we pull from Master.
* However, while developing you may want to specify a static branch, but we’ll talk more about that in the section in the documentation called “Testing With Selenium Locally”.

####Build triggers:

* Because we are relying on master to have the most up to date version we can set the build trigger in Jenkins to “Build when a change is pushed to BitBucket”
* Pro tip: when testing the reliability of scripts we can set to build periodically, which uses chron job notation to set your tests to run on a reoccurring time table. Which can help you understand how strong/weak a test case really is.

####Build Environment:

* I like to check off the option that allows us to “Add timestamps to the Console Output”
* This is a matter of preference and will not affect the functionality of the project.
* Depending on the Fisher Build you may need to select: "Inject environment variables to the build process" more on this in a specific section detailing specific scripts.

####Build:

**Execute Shell:**

`py.test --junitxml /var/lib/jenkins/workspace/Fischer/<Project_Name>/results.xml  /var/lib/jenkins/workspace/Fischer/<Project_Name>/test-cases/<Script_Name>`

The above code utilizes the built in feature of the Py.test framework to generate an XML output of the results of testcases. The results.xml is what populates the email that gets sent with every pass or fail of the Jenkins build.

####Post-build Actions:

**Publish JUnit test result report:**

* By selecting this you are enabling the blue and red graph that appears on the project dashboard page showing your “Test Result Trend” along with that, the XML supplies the data for the plugin: Test Results Analyzer. This can be found in the main navigation on the left side of the project dashboard.

**Editable Email Notification:**

* This area of the post-build Action section will show how we modify recipients and formatting for the email notifications generated by each build: "/var/lib/jenkins/email-templates"
* The file we are using here is called: groovy-html.template
* This template will utilize the xml generated and display it in html so that the email can be rendered by the mailer.

**Slack:**

* I have all the checkboxes set to display in a new slack channel.
* You will need an integration token with slack and you will need to know the team subdomain in our case we used: hsu-its

##File specific notes:

**test_LoopPasswordChanges.py**

This script is more of a utility than a test. We ensure that the password enforcement groups are being covered by the list of users we have selected. As of the writing of this readme, the enforcement groups we are testing are the “Finance” and “Default” groups.  

* LoopPasswordChanges()
    * This utility will log into [Fischer Admin](https://idm-prov-dev.humboldt.edu/identity/admin/logon.html) via the setup_login.py module. Given a list of user ids the script will generate a random password. This then creates a dictionary of user_ids and passwords. 
    * In order for the script to access the proper html, the webdriver must switch frames. You see this command on line 39.
    * The loop begins going through the dictionary created. 
        * For each user is selected via checkbox from a unique list on the users tab of the admin site. 
        * The "View Profile(s)" button is selected. Once the page titled: "Modify Profile User Details" loads we click the "Password View" button. 
        * We wait for the "User Password Management" page loads fully, this is done when the list of checkboxes loads with the various HSU properties that all need to be selected to ensure the password is reset for all of them.  
        * The "Reset Password" button is selected. We wait for the success response. 
        * Finally clicking the "modify profile" button to start from the beginning. 
        * The loop then continues until all passwords have been reset. 
* The script then enters into a teardown phase where it logs out of the environment. 

**test_add_remove_user.py**

![workflow](https://bytebucket.org/humboldt/fischer/raw/913bd41a79bb73c386ee3971f5e3d2d541a513c9/add_remove_user_peoplesoft_fischer_pic.png?token=47f41c00fdac5ea73ca96ed5fbb562e62c88a9fd)

This script qualifies more as a utility than a test. From start to finish this script will create, verify, and terminate a set of users. There are FOUR test functions in this file:

* test_add_peoplesoft_user() - This function creates and outputs a list of users.
    * This utility will log into [PeopleSoft](https://cmsdev1.calstate.edu/psp/HAHUMSTG/EMPLOYEE/HRMS/c/ADMINISTER_WORKFORCE_(GBL).PERSONAL_DATA_ADD.GBL?PORTALPARAM_PTCNAV=HC_ADD_PERSON_2&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=HC_WORKFORCE_ADMINISTRATION&EOPP.SCLabel=Workforce%20Administration&EOPP.SCPTfname=HC_WORKFORCE_ADMINISTRATION&FolderPath=PORTAL_ROOT_OBJECT.HC_WORKFORCE_ADMINISTRATION.CO_PERSONAL_INFORMATION.HC_ADD_PERSON_2&IsFolder=false) 
    * It proceeds to create a file name with the time of execution and with the provided environmental variables that are injected via the Jenkins job. (when running this script locally the environmental variables are injected in the setup_login.py script using driver_setup() in the final else clause of the function) 
    * A list is created ready to hold the contents of the user profiles created
    * Based on the injected "num_users" a loop is initiated to start the user creation process:
        * The proper HTML frame is specified so the script can select the html elements on the page. 
        * Navigate to the "Add a Person" page.
        * First, last name are entered. In this case the names are given random ints to ensure uniqueness.
        * The "Ok" button is pressed.
        * DOB and SSN are entered. SSN is a generated set of random ints.
        * Click the "Contact Information" tab.
        * In "Email Type" enter "Personal" from the dropdown. 
        * Email is entered as an injected environmental variable.
        * Click "Add Address Detail"
        * Address is added.
        * Click "OK" button for address.
        * The script waits for the loading icon to complete its loading status.
        * "Ok" is clicked on newly loaded page.
        * Click the "Organizational Relationships" tab.
        * Check the "Person of Interest" check box.
        * The script waits for the loading icon to complete its loading status.
        * Click the "Person of Interest" dropdown arrow.
        * The script waits for the loading icon to complete its loading status.
        * Depending on type of user the script enters a if/else block, depending on the type of "POI" they are:
            * if "Future Hire" select.
            * elif "Future Hire Faculty" select.
            * elif "Future Hire Staff" select.
        * Click "Add the Relationship".
        * The script waits for the loading icon to complete its loading status.
        * Under the "Security Access Type" field select "BUSINESS UNIT"
        * Click the plus button.
        * Under new drop-down select "POI DEPARTMENT" it's the fourth option.
        * For the "Value 1" enter or click the "HMCMP" value.
        * For the "Value 2" enter or click any of the values, for our case we will select or enter "D20076", this however is customizable via injected variables.
        * In the *Effective Date" section enter or leave the already populated Today's date.
        * In the "Planned exit" enter a date that is 2 days from now. This is handled via calculating the date two days from the moment the script starts. This too is customizable via injected variables.
        * In the "More information" tab add the fact that this is a test user. This too is customizable via injected variables.
        * Save "Person ID" for future reference in generated id list.
        * Save all these custom variables into a dictionary, that is normalized into ascii.
        * Click the "apply" button.
        * Click the "OK" button.
        * The loop continues util all users are created.
    * After the loop finishes a JSON file is created with the users added. 
    * The script then enters into a teardown phase where it logs out of the environment. 
        

* test_check_fischer_user_added() - This function verifies the users exist.
    * This utility will log into [Fischer Admin](https://idm-prov-dev.humboldt.edu/identity/admin/logon.html) via the setup_login.py module. 
    * In order for the script to access the proper html, the webdriver must switch frames.
    * Loads the file name of the list of user profiles created in the previous function outlined.
    * The tool parses the json file to create a list of dictionaries.
    * Cast EMPL_IDs to strings from json unicode and pull the each dictionary by their keys to create a list of only the ID's so we can verify they were created.
    * A loop is initiated to start the user verification process, based on the number of employees in the newly parsed list:
        * Clear the HSU ID field and enter the empl_id to check for.
        * Select the HSU ID field and enter the empl_id to check for.
        * Click the "Search" button.
        * Click the check the box for the unique user.
        * Click the "View Profile(s)" button.
        * Make sure that the association exists by checking to make sure that the "Employee Types:" field contains one of the following, an if statement begins:
            * If |Staff|, |Faculty|, |Faculty|Staff|, |Staff|Faculty|
            * else exit the script
        * Click the "Back to Results" button
        * The loop continues until all the users have been processed.
    * The script then enters into a teardown phase where it logs out of the environment. 


* test_edit_planned_exit() - This function change the value of their planned exit date.
    * This utility will log into [PeopleSoft](https://cmsdev1.calstate.edu/psp/HAHUMSTG/EMPLOYEE/HRMS/c/ADMINISTER_WORKFORCE_(GBL).PERSONAL_DATA_ADD.GBL?PORTALPARAM_PTCNAV=HC_ADD_PERSON_2&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=HC_WORKFORCE_ADMINISTRATION&EOPP.SCLabel=Workforce%20Administration&EOPP.SCPTfname=HC_WORKFORCE_ADMINISTRATION&FolderPath=PORTAL_ROOT_OBJECT.HC_WORKFORCE_ADMINISTRATION.CO_PERSONAL_INFORMATION.HC_ADD_PERSON_2&IsFolder=false) 
    * In order for the script to access the proper html, the webdriver must switch frames.
    * Checks off the correct history box.
    * Parse the file, from the os variable that is storing the json to create a list of dictionaries.
    * Cast EMPL_IDs to strings from json unicode and pull the each dictionary by their keys to create a list of only the IDs so we can change their planned exit date in peoplesoft.
    * Based on the injected "num_users" a loop is initiated to start the user creation process:
        * Clear user field.
        * Clear Person of Interest Type.
        * Input the first user EMPL_IDS.
        * Click search.
        * Clear the date that is in expected end date.
        * Get today's date.
        * Send the date in recently cleared field.
        * Clear the text from more info area.
        * In the "More information" tab add the fact that this is a test user, with a shortened planned exit date.
        * Click Save.
        * The loop continues until all the users have been processed.
    * The script then enters into a teardown phase where it logs out of the environment. 


* test_check_fischer_user_recently_seperated() - The next day we check to make sure that that user is in fischer with the Employee type as "|Recently Seperated|"
    * This utility will log into [Fischer Admin](https://idm-prov-dev.humboldt.edu/identity/admin/logon.html) via the setup_login.py module. 
    * In order for the script to access the proper html, the webdriver must switch frames.
    * Loads the file name of the list of user profiles created via the json file name, which is stored as an os variable.
    * Parse the file, from the os variable that is storing the json to create a list of dictionaries.
    * Cast EMPL_IDs to strings from json unicode and pull the each dictionary by their keys to create a list of only the IDs so we can change their planned exit date in peoplesoft.
    * Based on the injected "num_users" a loop is initiated to start the user creation process:
        * Clear the HSU ID field.
        * Select the HSU ID field and enter the empl_id to check for.
        * Click the "Search" button.
        * Click the check box for the unique user.
        * Click the "View Profile(s)" button.
        * Check for the emp type field to exist.
        * Enter if/else statement:
            * Take the text from the field and check for it to have the value "|Recently Separated|"
            * Else exit the script.
        * Click the "Back to Results" button.
    * The loop continues until all the users have been processed.
    * The script then enters into a teardown phase where it logs out of the environment. 
