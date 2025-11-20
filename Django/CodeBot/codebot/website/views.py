from django.shortcuts import render
from django.contrib import messages
import openai

# Create your views here.

def home(request):
    lang_list=["clike", "c", "cpp", "csharp", "css", "css-extras", "django", "docker", "excel-formula", "git", "go", "html", "java", "javadoc", "javadoclike", "javascript", "jsdoc", "js-extras", "jsstacktrace", "js-templates", "markup", "markup-templating", "powershell", "python", "sql", "typescript"]

    if request.method=='POST':
        code=request.POST['code']
        lang=request.POST['lang']
        if lang=='Select Programming Languauge':
            messages.success(request,"Hey, You forgot to select a programming languauge...")
            return render(request,'home.html',{"lang_list":lang_list,"code":code,"lang":lang})
        else:
            # client = OpenAI()    
            # openai.api_key = ""
            # openai.Model.list()
            
            try:
                response = openai.Completion.create(
                    engine="gpt-4o-mini",
                    prompt="Write a tagline for an ice cream shop.",
                    max_tokens=50
                    )
                
                # response= openai.completions.create(
                #     model="gpt-3.5-turbo-instruct",
                #     prompt=f"Respond only with code. Fix this {lang} code: {code}",
                #     # engine = 'text-davinci-003',
                #     # promt = f"Respond only with code. Fix this {lang} code: {code}",
                #     temperature = 0,
                #     max_tokens = 1000,
                #     top_p=1,
                #     frequency_penalty=0.0,
                #     presence_penalty=0.0,   
                # )
                return render(request,'home.html',{"lang_list":lang_list,"code":response,"lang":lang})
            except Exception as error:
                return render(request,'home.html',{"lang_list":lang_list,"code":error,"lang":lang})
        
        
    return render(request,'home.html',{"lang_list":lang_list})