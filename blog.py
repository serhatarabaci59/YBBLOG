from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

# kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators = [validators.Length(min = 4, max =25 )])
    username = StringField("Kullanıcı Adı",validators = [validators.Length(min = 5, max =35 )])
    email = StringField("E-mail Adresi",validators = [validators.Email(message= "Lütfen Geçerli Bir Mail Adresi Girin...")])
    password = PasswordField("Parola:", validators = [
        validators.DataRequired(message="Lütfen Parola Belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor")
    ])
    confirm = PasswordField("Parola Doğrula")


    



app = Flask(__name__)

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_pASSWORD"]= ""
app.config["MYSQL_DB"]= "ybblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/")
def index():
    numbers = [1,2,3,4,5]
    return render_template("index.html", numbers = numbers )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article/<string:id>")
def detail(id):
    return "Article Id:" + id

#Kayıt Olma
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST":
        pass
    else:
        return render_template("register.html",form = form)
if __name__=="__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
