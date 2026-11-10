import random,  re , string
from flask import Flask ,request, render_template

PASSWORDS =["Random","Classic","Mixed"]

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def gen():
    #if the user typed the name  
    if request.method ==("POST"):
        #check the name form the html page

        name=request.form.get("name")

        if not name :
            return render_template("pass1.html", error="error: please try again")
        mode=request.form.get("mode") 
        print(mode)
        
    
        if mode not in PASSWORDS:
               return render_template("pass1.html" ,  error="error: please try again")
        if mode=="Classic":
            password=name.capitalize() + str(random.randint(1000,9999))
            return render_template("pass1.html",mode=mode,name=name,password=password)
        elif mode =="Mixed":
                     replacements = {
                         "a": "@", 
                         "e": "3", 
                         "i": "1", 
                         "o": "0",
                         "b":"#",
                         "c":"8",
                         "r":"8"
             
                      }       
                     table = str.maketrans(replacements)
                     length=4
                     choices = string.ascii_letters + string.digits
                     random_string = "".join(random.choices(choices, k=4))

                     password = name.translate(table) + random_string
                     return render_template("pass1.html",mode=mode,name=name,password=password)
             
    
        elif mode=="Random":

                                 length = 8
        password=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        return render_template("pass1.html",mode=mode,name=name,password=password)

    else:
    # if not stay in the same page
        return render_template("pass.html", passes=PASSWORDS)
              
              
        
    
    
    
        
          
    
    
    
