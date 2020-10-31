from django.shortcuts import render , HttpResponse , redirect
from  .models import *
from .forms import Contact_Us_Form

from django.contrib import messages
import bs4
from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail



# Contact form to be used in every page
ContactForm = Contact_Us_Form(None)


#This function handles homepage loading 
def Homepage(request):
    if request.method=="POST":
        form = Contact_Us_Form(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Message= form.cleaned_data['Message']
            Email = form.cleaned_data['Email']
            send_mail(
                'from {}'.format(Name),
                '{} - {}'.format(Message , Email),
                Email,
                ['rohansolanke4@gmail.com'],
                fail_silently=False,)
            contactform = form.save()
            contactform.save()
            messages.add_message(request , messages.SUCCESS , 'new' , extra_tags='message_recieved')
            return redirect('/')
        else:
            return HttpResponse(status=404)
        
    C = Courses.objects.all()
  
    context ={
        'Courses':C[0:5],
        'ContactForm':ContactForm
    }

    return render( request , 'homepage.html',context)



#course list retrieval and viewing
def Course_List(request):
    C = Courses.objects.all()
    if request.session.get('coursetitle'):
        courseinfo = [request.session.get('coursetitle'), request.session.get('coursesubtitle'), request.session.get('courselink')]
        context={
      'Courses':C , 
      'courseinfo':courseinfo
    }
    else:
        courseinfo = None
        context={
      'Courses':C , 
      'ContactForm':ContactForm
      
    }
   
   
    if request.session.get('coursetitle'): 
        del request.session['coursetitle']
        del request.session['coursesubtitle']
        del request.session['courselink']
    print(courseinfo)
    return render(request , 'course_list.html'  , context)


# Getting course info for admin to copy details
def Course_Info(request , id):
    C = Courses.objects.get(id=id)
    request.session['coursetitle'] = C.Title
    request.session['coursesubtitle'] = C.Subtitle
    link = 'http://' + request.get_host() + '/course_detail/' + str(C.id) 
    messages.add_message(request , messages.SUCCESS , 'new' , extra_tags='cinfo')
    request.session['courselink'] = link
    return redirect('/freecourses/')


# getting links and titles of every page
def Courses_Links(request):
    courses = Courses.objects.all()
    Courselistmain = []
    count = 0
    for course in courses:
        link = '        http://' + request.get_host() + '/course_detail/' + str(course.id) 
        count+=1
        Courselist = []
        title = (str(count) +'. ' + course.Title).replace('\n' , '') + '\n'
        Courselist.append(title)
        Courselist.append(link)
        Courselistmain.append(Courselist)
    print(Courselistmain)
    context = {
        'courselist':Courselistmain
    }

    return render(request , 'courselinks.html' , context)

 

# details of a particulat course
def View_Course_Details(request , id ):
    try:
        C = Courses.objects.get(id = id)
        Objectives = list(filter(None,C.Objective.split('$')))
        Description = list(filter(None,C.Description.split('$')))
        Requirements = list(filter(None,C.Requirements.split('$')))
        print(Objectives , '\n')
        context={
            'course':C,
            'Objectives':Objectives,
            'Description1':Description[0:5],
            'Description2':Description[5:],
            'Requirements':Requirements,
            'ContactForm':ContactForm
        }
    except:
        return redirect('/page_not_found/')
    return render(request , 'course_detail.html' , context)



# Function for scrapping data from udemy and saving sufficient info in data with each coure's expiry date
def Scrapper(request):
    try:
        link = request.POST.get('search')
        no = request.POST.get('no')

        if int(no)==0:
            return redirect('/scrapper/')
        
        page=requests.get(link)
        
        if not 'https://www.udemy.com/course/' in link:
            messages.add_message(request , messages.SUCCESS , 'Fuck off dude , wrong url' , extra_tags='wrongurl')
            return redirect('/freecourses/')
        
        soup=BeautifulSoup(page.content,"html.parser")
        Title = soup.find(class_="udlite-heading-xl clp-lead__title clp-lead__title--small").text
        Subtitle = soup.find(class_='udlite-text-md clp-lead__headline').text
        Obj =soup.find_all(class_="what-you-will-learn--objective-item--ECarc")
        Req = soup.find(class_="ud-component--course-landing-page-udlite--requirements").find(class_='unstyled-list udlite-block-list')

        Image_URL = soup.find("meta",  {"name":"twitter:image"})
        Desc = soup.find(attrs={'data-purpose':'safely-set-inner-html:description:description'})



        Description=''
        objective=''
        Requirements =''
        for i in Desc:
            try:
                Description = Description + '$' + i.text
            except:
                pass
    
        
        for i in Obj:
            objective = objective + '$' + i.text
        
        for i in Req:
            Requirements = Requirements  + '$' + i.text



        Courses.objects.create(Image=Image_URL['content'] , Title=Title , Subtitle=Subtitle ,Objective = objective , Requirements=Requirements , Description=Description , Udemy_Link=link , No_Of_Days=int(no))
    except:
        return HttpResponse('Bad request')


    return redirect('/freecourses/')



#Function for handling any kind of exception of bad request
def Error_Page(request):
    return render(request , 'errorpage.html' , {'ContactForm':ContactForm})

