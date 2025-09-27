from flask import Flask, request, render_template_string

app = Flask(__name__)

# vulnerable login (SQL injection simulation)
@app.route("/", methods=["GET", "POST"])
def login():
    html = """
    <h2>Vulnerable Login</h2>
    <form method="post">
      Username: <input type="text" name="username"><br>
      Password: <input type="password" name="password"><br>
      <input type="submit" value="Login">
    </form>
    {% if result %}
      <p><b>{{ result }}</b></p>
    {% endif %}
    """
    result = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # insecure check (for demo)
        if username == "admin" and password == "admin":
            result = "Login Successful (admin)"
        elif "' OR '1'='1" in username or "' OR '1'='1" in password:
            result = "Bypassed Login with SQL Injection!"
        else:
            result = "Invalid Credentials"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
