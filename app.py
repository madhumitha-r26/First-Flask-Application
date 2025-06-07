from flask import *
from flask_mail import *

app = Flask(__name__)
app.secret_key="abcde12345"



app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  

mail = Mail(app)  

#------------------------url building-----------------------------

def hello_world():
    return 'Hello World'
app.add_url_rule('/', 'hello', hello_world)

@app.route('/') #best one
def hello_world():
    return 'Hello World'

@app.route('/madhu')
def madhu_call():
    return 'madhumitha'

#------------------------dynamic routing-----------------------------

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello'+' '+ name

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello '+guest+' as Guest'

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


#------------------------url building with http methods-----------------------------

@app.route('/success/<name>')
def success1(name):
   return 'welcome %s' % name

@app.route('/suc/<name>')
def success2(name):
   return 'hello %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success1',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success2',name = user))

#------------------------templates usage-----------------------------

@app.route('/index')
def index():
   fruits=['apple','banana','cherry']
   courses=['python','java','c++']
   is_logged=True

   result={
      'maths':80,
      'english':90,
      'science':85
   }
   return render_template('index.html', fruits=fruits, courses=courses, is_logged=is_logged,result=result)

#------------------------ form usage -----------------------------

@app.route('/student')
def student():
   return render_template('students.html')

@app.route('/marks',methods = ['POST', 'GET'])
def marks():
   if request.method == 'POST':
      res = request.form
      return render_template('marks.html',res=res)

# ---------------------cookies------------------------------

@app.route('/cookie')
def enter_cookie():
   return render_template('cookieform.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
   if request.method == 'POST':
        user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html',username=user))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+ name + '</h1>'

# -----------------------------session-----------------------------------
@app.route('/session')
def session_page():
   res=make_response("<h4>Session variable is set, <a href='/getsession'>GET VARIABLE</a></h4>")
   session['response']='admin'
   return res

@app.route('/getsession')
def get_session():
   if 'response' in session:
      s= session['response'] 
      return render_template('getsession.html',name=s)


# --------------------- redirect, errors & flash --------------------------
@app.route('/login2')
def admin():
   return render_template('login.html')

@app.route('/login3',methods = ['POST', 'GET'])
def login2():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         flash('This is a flash message')
         return redirect(url_for('index'))
      else:
         abort(401)
   else:
      return redirect(url_for('admin'))
 
@app.route('/success')
def success():
   return 'logged in successfully'


#-------------------------- file upload -----------------------------
@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        return render_template("fileres.html", filename = f.filename)  


#-------------------------------mail extention------------------------------------
@app.route('/mailbox')  
def mailme():  
    msg = Message('subject', sender = 'admin@gmail.com', recipients=['username@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    return "Mail Sent, Please check the mail id"  

if __name__ == '__main__':
      app.run(debug=True)