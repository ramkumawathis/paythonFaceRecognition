import os
from flask import Flask, render_template, request, flash, redirect, url_for, Response
import requests
# for video 
import face_recognition
import cv2
import numpy as np
# for video 


#for file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#for file



# for video 
# video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
# mahesh_image = face_recognition.load_image_file("mahesh.jpg")
# krish_face_encoding = face_recognition.face_encodings(mahesh_image)[0]

# # Load a second sample picture and learn how to recognize it.
# bradley_image = face_recognition.load_image_file("bradley.jpg")
# bradley_face_encoding = face_recognition.face_encodings(bradley_image)[0]

# # Create arrays of known face encodings and their names
# known_face_encodings = [
#     krish_face_encoding,
#     bradley_face_encoding
# ]
# known_face_names = [
#     "Mahesh",
#     "Bradley"
# ]

known_face_encodings = []
known_face_names = []

# Iterate over the images in the static folder
upload_folder = app.config['UPLOAD_FOLDER']
subfolder =   'a'
subfolder_path = os.path.join(upload_folder, subfolder)

for filename in os.listdir(subfolder_path):
    # Construct the full path to the image
    image_path = os.path.join(subfolder_path, filename)
    
    # Load the image file
    image = face_recognition.load_image_file(image_path)
    
    # Extract face encoding
    face_encoding = face_recognition.face_encodings(image)[0]
    
    # Extract the name from the filename (assuming filenames are in the format "<name>.jpg")
    name = os.path.splitext(filename)[0]
    
    # Append the face encoding and name to the arrays
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)

# Now you have the arrays of known face encodings and their names
# You can use them for face recognition



def generate_frame():
    global video_capture
    video_capture = cv2.VideoCapture(0)
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    threshold = 0.60

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    confidence_score = round(1 - face_distances[best_match_index], 2)
                    
                    if confidence_score > threshold:
                        name = known_face_names[best_match_index]
                        print(f"Recognized as {name} with confidence {confidence_score}")
                        
                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Convert the frame to bytes
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield the frame bytes
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
# for video 


# images get 
# API endpoint that serves images
API_ENDPOINT = "https://jsonplaceholder.typicode.com/photos"

def get_images_from_api():
    try:
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            # Assuming the API returns a list of image objects with 'url' attribute
            images = response.json()
            # Extract image URLs and store in an array
            image_urls = [image['url'] for image in images]
            return image_urls
        else:
            print("Failed to fetch images from API:", response.status_code)
            return []
    except Exception as e:
        print("Error fetching images from API:", str(e))
        return []
# images get 

@app.route("/")
def home():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/userimage", methods=["GET", "POST"])
def userimage():
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            #return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
          #  return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("index.html")
            # return redirect(url_for('download_file', name=filename))
    else:
        return render_template('userfile.html')

@app.route("/camera")
def camera():
    return render_template("camera.html")   

@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_images')
def get_images():
    image_urls = get_images_from_api()
    # Pass image URLs array to template for rendering
    return render_template('images_list.html', image_urls=image_urls)

@app.route('/take_photo')
def take_photo():
    global video_capture
    if video_capture is not None:
        video_capture.release()
    return render_template('take_photo.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            upload_folder = app.config['UPLOAD_FOLDER']
            subfolder =   request.form['gym_id']

            # Check if the subfolder exists, create it if it doesn't
            subfolder_path = os.path.join(upload_folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

            # photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
            photo.save(os.path.join(subfolder_path, photo.filename))
            return 'Photo uploaded successfully!'
    return 'No photo received.'

app.run(debug=True)