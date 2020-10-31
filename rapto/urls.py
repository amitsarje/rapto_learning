from django.contrib import admin
from django.urls import path 
from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$' , views.Homepage  , name="homepage" ),
    url(r'^freecourses/$' , views.Course_List  , name="course_list" ),
    url(r'^courseinfo/(?P<id>\d+)/$' , views.Course_Info  , name="courseinfo" ),
    url(r'^courseslinks/$' , views.Courses_Links  , name="course_detail_with_links" ),
    url(r'^scrapper/$' , views.Scrapper , name="scrapper"),
    url(r'^course_detail/(?P<id>\d+)/$' , views.View_Course_Details , name="view_course_details"),
    url(r'^page_not_found/$' , views.Error_Page , name="error_page"),
]


