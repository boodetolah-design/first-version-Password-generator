import random
from flask import Flask ,request, render_template

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def gen():
    #if the user typed the name  
    if request.method ==("POST"):
        #check the name form the html page

        name=request.form.get("name")
        if not name :
            #if the name is empty go to pass1 page and display error
            return render_template("pass1.html", error="error: please try again")
        #if the user input something like his then capitlaize the first letter and then choose rand number between 1000 to 9999 and stick it togather
        
        password=name.capitalize() + str(random.randint(1000,9999))
        #RETURN back to pass1 page and take the name and the password with you
        #check the name form the html page
        return render_template("pass1.html",name=name,password=password)
    else:
     #if not stay in the same page 


     return render_template("pass.html")
    
