DEPENDENCIES AND INSTALLATION INSTRUCTIONS:
The script requires the following dependencies:
    - python
    - pygame
    - pygetwindow

INSTALLATION GUIDE:

1) navigate to the DEPENDENCIES folder, inside you will find 
    - The python installer
    - A file Named "dependencies.bat"

2) Install python if you have not already

3) run "dependencies.bat" 

4) Wait for all dependencies to Install

5) Run "run.bat" to start the application
    -alternatively - cd into the root directory through your terminal and run "python main.py"

USAGE GUIDE:

When launched the application will prompt you for 3 things
(PLEASE NOTE ALL NUMBERS SHOULD BE ENTERED AS A PERCENTAGE -- For example, when 100 is entered, it is treated as 100%)

1: The probability of the narrator speaking
    - 100 will prompt the narrator to speak every time a window is opened or closed 
    - 0 will render the narrator unable to speak

2: The volume of the narrator
    - 100 will make the narrator speak at full volume (while not deafening, can definetly be a jumpscare if forgotten about)
    - 0 will make the narrator completely silent

3: Window monitoring
    - If yes - the CLI will show which windows have been opened or closed
    - if no - the application will still work perfectly, it just will not display the windows being monitored

4: terminating the program:
    - closing the CLI will terminate the program
    - alternatively a keyboard interrupt (CTRL + C) will also terminate the program