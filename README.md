# Regex Matching Web App

A web application that allows users to test regular expressions and validate email addresses.

## Features

- Test regular expressions against input strings
- Display all matches found
- Email validation functionality
- Modern and responsive UI using Bootstrap

## Setup Instructions

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Regex Matching**:
   - Enter a test string in the first text area
   - Enter a regular expression pattern in the second input field
   - Click "Find Matches" to see all matches in the test string

2. **Email Validation**:
   - Enter an email address in the email validation section
   - Click "Validate Email" to check if the email is valid

## Example Regex Patterns

- Email: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- Phone Number: `\d{3}-\d{3}-\d{4}`
- URL: `https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$` 