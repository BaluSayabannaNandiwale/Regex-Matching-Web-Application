from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')
    
    try:
        # Find all matches in the test string
        matches = re.findall(regex_pattern, test_string)
        return render_template('index.html', 
                             test_string=test_string,
                             regex_pattern=regex_pattern,
                             matches=matches,
                             error=None)
    except re.error as e:
        return render_template('index.html',
                             test_string=test_string,
                             regex_pattern=regex_pattern,
                             matches=None,
                             error=f"Invalid regex pattern: {str(e)}")

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form.get('email', '')
    # Email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    is_valid = bool(re.match(email_pattern, email))
    return render_template('index.html',
                         email=email,
                         is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True) 