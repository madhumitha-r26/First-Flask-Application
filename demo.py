from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

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


if __name__ == '__main__':
      app.run(debug=True)