Instruction to Execute code:

1. Extract the files from the zip file.

2. Now Open the code folder using Visual Studio Code Editor.

3. For running the code make sure Python 3 and django framework is installed in your system.

4. If you want to install django framework in a virtual enviroment.
   - pip install virtualenvwrapper-win
   - mkvirtualenv "environment-name" (example-test,env)
   - pip install django 

5. Install all dependencies from requirements.txt
   - pip install pyrebase
   - pip install razorpay


6. To store the data in the database 
     - Create an account on Firebase.
     - Create a database in realtime database of Firebase.
    
7. For integration of Chatbot
    - Create an account on Dilogflow
    - Create a bot with all the intent you want in the chatbot.
    - Create a Kcommunicate account to inegrate the dialogflow chatbot by add the Private key there.
    - Add the installation code in the project (script_bot.js in the project) 

8. For Payment gateway.
   - Create an account on Rozerpay
   - Create the button with functionalities and itegrate in view.py 

9. Now by using the following command the server will start on port 8000
   - python manage.py runserver

10. open the following url:
   - 127.0.0.1:8000/user/home