from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form.caesar {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 50%;
                text-align: center;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            input, textarea, label, button {
                display: block;
                text-align: left;
            }
            input[type=text] {
                width: 80%;
                margin-bottom: 15px;
            }
            textarea {
                margin: 0 0 15px 0;
                width: 80%;
                max-width: 90%;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form class='caesar' action='/' method='POST'>
            <label>Rotate by: </label>
            <input type='text' name='rot' value='0'>
            
            <label> enter some text: </label>
            <textarea name='text'>
            </textarea>
           
            <button type='submit'>Submit</button>
        </form>
    </body>
</html>
'''

@app.route('/')
def index():
    return form

@app.route('/', methods=['POST'])
def encrypt():
    rot_char = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_string(text, rot_char)

    return '<h3>' + encrypted + '</h3>'

app.run()