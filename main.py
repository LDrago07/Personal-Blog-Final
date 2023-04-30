from flask import Flask, render_template, request
import requests
import smtplib
from post import Post

EMAIL = "EXAMPLE"
PASSWORD = "EXAMPLE"

app = Flask(__name__)

@app.route("/")
def home():
    blog = "https://api.npoint.io/25087c5de55ee4339eff"
    response = requests.get(blog)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post/<blog_id>")
def get_blog(blog_id):
    post = Post(blog_id)
    return render_template("post.html", post=post.blog_post, blog_id=post.blog_id)

@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, PASSWORD, email_message)

''' Old Method of retriving data from forms need to edit contact.html to use again replace the action url for contact with recieve_data
@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
'''
    
if __name__ == "__main__":
    app.run(debug=True)