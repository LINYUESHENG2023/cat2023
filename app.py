#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask,request,render_template


# In[8]:


import openai


# In[ ]:


app = Flask(__name__)
openai.api_key = "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"
@app.route("/",methods=["GET","POST"])
def index():
           if request.method == "POST":
               q = request.form.get("question")
               r = openai.ChatCompletion.create(
                   model = "gpt-3.5-turbo-0613",
                   message = [{
                       "role" : "user",
                       "content" : q
                   }]
               )
               return(render_template("index.html",result=r["choices"][0]["message"]["content"]))
           else:
               
                return(render_template("index.html",result="waiting"))
if __name__ == "__main__":
    app.run()


# In[ ]:




