from flask import Flask, render_template,request, redirect
from fsa_datastructure import FSA

app = Flask(__name__)

s1 = ['q0','q1']
i1 = ['0','1']
# 0 for english aplhabet
# 1 for space
d1 = {('q0','0'):'q1',('q1','0'):'q1',('q1','1'):'q1'
}
st1 = 'q0'
f1  = ['q1']
fsa_name = FSA(s1,i1,d1,st1,f1)

s1 = ['q0','q1','q2','q3']
i1 = ['0','1','2','3','4','5','6','7','8','9']
d1 = {('q0','5'):'q1',('q1','0'):'q2',('q1','1'):'q2',
   ('q1','2'):'q2',('q1','3'):'q2',('q1','4'):'q2',('q1','5'):'q2'
   ,('q1','6'):'q2',('q1','7'):'q2',('q1','8'):'q2',('q1','9'):'q2'
   ,('q2','1'):'q3', ('q2','2'):'q3', ('q2','3'):'q3',
   ('q2','4'):'q3', ('q2','5'):'q3', ('q2','6'):'q3',
   ('q2','7'):'q3', ('q2','8'):'q3', ('q2','9'):'q3'          
}
st1 = 'q0'
f1  = ['q3']
fsa_rollno = FSA(s1,i1,d1,st1,f1)

Registered = {}
def transform_form_input(name):
    zerosonestwo = ''
    for x in name:
        if x.isalpha():
            zerosonestwo=zerosonestwo+'0'
        elif x.isspace():
            zerosonestwo=zerosonestwo+'1'
        else: #o for other
            zerosonestwo=zerosonestwo+'o'
    return zerosonestwo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("rollno"):
        return render_template("failure.html",msg="Cannot be empty")
    name = request.form.get("name")
    zot  = transform_form_input(name)
    rollno = request.form.get("rollno")
    if not fsa_name.accepted_or_not(zot):
        return render_template("failure.html",msg="Name is not valid")
    if not fsa_rollno.accepted_or_not(rollno):
        return render_template("failure.html",msg="Roll no is not valid")
    Registered[name]=(name,rollno)
    return render_template("success.html",reg = Registered)
