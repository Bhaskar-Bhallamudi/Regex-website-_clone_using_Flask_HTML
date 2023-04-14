# Importing flask framework
from flask import Flask, request, render_template
import re

# Creating object with parameter __name__
app = Flask(__name__)

# Creating end points
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regex', methods=['GET','POST'])
def regex():
    statement = request.form.get('Statement')
    exsprsn = request.form.get('regex_ex')
    pattern = re.findall(exsprsn, statement)
    opt = ' '.join([str(elem) for elem in pattern])
    return render_template('output.html', output = opt, count=len(pattern))
    
    
if __name__ == "__main__":
    app.run(debug=True) 