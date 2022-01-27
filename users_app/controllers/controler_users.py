from flask import redirect, render_template, request
from users_app import app 
from users_app.models.model_users import User

@app.route("/users",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        print("renderizando")
        objects_user=User.get_all()
        return render_template("index.html", users = objects_user)
    if request.method =='POST':
        nuevo_usuario={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email']
        }
        usuario_creado=User.create_new_user(nuevo_usuario)
        print("envio a la base de datos",usuario_creado)
        return redirect("/users")


@app.route("/users/new",methods=['GET'])
def new_user():
    print("renderizando")
    return render_template("new_user.html")