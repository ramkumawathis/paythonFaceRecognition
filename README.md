
# install python  3.10.11
Flask: jo jo package install kiye hai unki history ke liye  "requirements.txt" create kr lo
like is time se history rkh lo 
flask
opencv-python
face-recognition
requests 
python-dotenv


# Note: all package ek sath install ke liye below command chala do console me
pip install -r requirements.txt       // for all requirements ek sath install krni ho to





# flask project restart:   Ye nhi kroge to chagnes ke bad me restart kroge tab hi changes dikhenge
# FLASK_APP=app (app) name hamesa wo hi name do jo aapko call krwana hai lime isme main.py hai
pip install python-dotenv  // ye project install kr lo
.flaskenv                  // root directory in create a file and below wala code dal do
	
FLASK_APP=app  // jis file ko run krte hai (app or main) file
FLASK_DEBUG=1




-> Add to environ ment variables
    Go to Advance => click on “Environment variable”
    Ststem variable=> click on path and “edit”
    Add new path=> Like for python10:
# ye two path add krne hote environment variable me
# ye path nikalen ke liye 
# run type on serch bar in window 10 
    %localappdata%         // ye command lik kr "OK" kro
    // Programs\Python ye mil jayga path

    C:\Users\ADMIN\AppData\Local\Programs\Python\Python310
    C:\Users\ADMIN\AppData\Local\Programs\Python\Python310\Scripts



########### for face-recognition Only ############# 

    for face-recognition library note install then:-
    1).
    https://stackoverflow.com/questions/55154397/modulenotfounderror-no-module-named-face-recognition

    https://www.youtube.com/watch?v=sS010y23neU
    dlib binary
    https://github.com/z-mahmud22/Dlib_Windows_Python3.x

    python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl  // only for window
    https://cmake.org/download/                 // for window  "Windows x64 Installer:"

    2). 
    ye donload kr ke: install kr lo direct next next kr ke.
    https://cmake.org/download/
    Windows x64 Installer:

    ------------ server pr ye install krna hota hai -------------
        --- ye sub "dlib", "cmake" server vale install kr ke diye the
        pip3.10 install pyqt5
        pip3 install wheel setuptools pip --upgrade
        pip install toml
        pip install Cmake
    ------------ server pr ye install krna hota hai -------------

########### for face-recognition Only ############# 






############# now python code ############
    Pyton project setup:  ye two package install kr ke "python main.py" run kiya tha tab code chal gya tha
    1). pip install opencv-python
    2). pip install face-recognition

    pip install -r requirements.txt       // for all requirements ek sath download krni ho to
############# now python code ############






####################### for help ##################
# Note full code work nhi krega face recognition ke liye 
threshold = 0.60           // while se phel ye add kr do

    while True:

    if matches[best_match_index]:    # // ye match hone ke bad me below wala if "threshold" add kr do for currect face ke liye
                    confidence_score = round(1 - face_distances[best_match_index], 2)
                    
                    if confidence_score > threshold:
                        name = known_face_names[best_match_index]


    https://github.com/ageitgey/face_recognition

    https://github.com/krishnaik06/Flask-Web-Framework
    8 number project
    Note: iske liye python ka 3.10 version download krna hoga.

    run: python main.py
    pip install -r requirements.txt


    for face-recognition library note install then:-
    1).
    https://stackoverflow.com/questions/55154397/modulenotfounderror-no-module-named-face-recognition

    https://www.youtube.com/watch?v=sS010y23neU
    dlib binary
    https://github.com/z-mahmud22/Dlib_Windows_Python3.x

    2). 
    ye download kr ke: install kr lo direct next next kr ke.
    https://cmake.org/download/
    Windows x64 Installer:
####################### for help ##################







############### flask ke liye #########################
    
1). pip install opencv-python
2). pip install face-recognition
3). pip install requests        // api se data lena ho third party se to 

Flask: https://www.youtube.com/watch?v=hVEZYEYctSc&t=20s

	1). main.py file, templates, static   // ye flask ka stracture hota hai.
	2). flask minimal app (user version 2.2.x)        // https://flask.palletsprojects.com/en/2.2.x/quickstart/

app.secret_key = "super secret key"      // ye dalna hotha hia.

3).pip install Flask
#### add code on main.py 
	from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run(debug=True)

4).flask --app main run      //  run flask
    flask run // now use  (flaskdotenv) file create ke bad me ye command chala denge.

5). top me template import kr lo // from flask import Flask, render_template
	@app.route("/")
	def hello_world():
	    # return "<p>Hello, World!</p>"
	    return render_template("index.html")


6). For forms  top me request import kr lo// from flask import Flask, render_template, request 

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        return "Edit post request"
    else:
        return "Edit Get Request"


####### jha bhi form dalna hai wha dal do #########
	<form action="{{url_for('edit')}}" method="post">
            <label for="enter_value">*Sample Text*:</label><br>
            <input type="text" name="enter_value">
            <input type="submit" value="Submit">
        </form>
####### jha bhi form dalna hai wha dal do #########



7). how to upload a file to flask
	
8). flask flash messages. (for message show).



1). 
Facial Recognition Attendance System Using Python & Flask: 
https://www.youtube.com/watch?v=_EDoqeS0etE
https://github.com/Chando0185/face_recognition_flask

import this module:-
pip install -U scikit-learn

Run: flask --app app run 

2). https://www.youtube.com/watch?v=Zc-t0mjkiWk
www.github.com/itsmeSamrat/Face-Recognition-System-for-Student-Attendance


############### flask ke liye #########################
