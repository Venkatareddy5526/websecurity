# vuln_demo_fixed.py
from flask import Flask, request, render_template_string, escape

app = Flask(__name__)
VALID_USERS = {"admin": "admin"}  # demo only

@app.route("/", methods=["GET", "POST"])
def login():
    html = """
    <h2>Safe Login Demo</h2>
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
        username = request.form.get("username","")
        password = request.form.get("password","")
        if VALID_USERS.get(username) == password:
            result = "Login Successful (admin)"
        else:
            safe_user = escape(username)
            result = f"Invalid credentials (received: {safe_user})"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
