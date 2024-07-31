from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/submit-report', methods=['POST'])
def submit_report():
    name = request.form['name']
    email = request.form['email']
    issue = request.form['issue']

    # Process the report (e.g., send to a channel, store in a database, etc.)
    # For example, print the details (in a real app, you'd handle this differently)
    print(f"Report from {name} ({email}): {issue}")

    # Redirect to a thank-you page or another page
    return redirect('/thank-you')

@app.route('/thank-you')
def thank_you():
    return "Thank you for your report! We'll look into it."

if __name__ == '__main__':
    app.run(debug=True)
