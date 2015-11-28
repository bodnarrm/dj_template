from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os, sys
from  django.shortcuts  import  render
from  django.http  import  HttpResponse

def students_list(request):
    return  render(request,  'students/students_list.html',  {})
def students_add(request):
    return  HttpResponse('<h1>Student  Add  Form</h1>')
def students_edit(request,  sid):
    return  HttpResponse('<h1>Edit  Student  %s</h1>'  %  sid)
def students_delete(request,  sid):
    return  HttpResponse('<h1>Delete  Student  %s</h1>'  %  sid)

def groups_list(request):
    return  HttpResponse('<h1>Groups  Listing</h1>')    
def groups_add(request):
    return  HttpResponse('<h1>Group  Add  Form</h1>')
def groups_edit(request,  gid):
    return  HttpResponse('<h1>Edit  Group  %s</h1>'  %  gid)
def groups_delete(request,  gid):
    return  HttpResponse('<h1>Delete  Group  %s</h1>'  %  gid)

def students_list(request):
        students  =  (
            {'id':  1,
            'first_name':  unicode('��⠫��'),
            'last_name':  u'������',
            'ticket':  235,
            'image':  'img/me.jpeg'},
            {'id':  2,
            'first_name':  u'�����',
            'last_name':  u'������',
            'ticket':  2123,
            'image':  'img/piv.png'},
            {'id':  3,
            'first_name':  u'������',
            'last_name':  u'����᫠�',
            'ticket':  5577,
            'image':  'img/bodnar.png'},)
        return  render(request,  'students/students_list.html', {'students':  students})

