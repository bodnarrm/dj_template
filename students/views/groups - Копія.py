# -*- coding: utf-8 -*-

import os, sys

from  django.shortcuts  import  render
from  django.http  import  HttpResponse

def groups_list(request):
    return  HttpResponse('<h1>Groups  Listing</h1>')    

def groups_add(request):
    return  HttpResponse('<h1>Group  Add  Form</h1>')

def groups_edit(request,  gid):
    return  HttpResponse('<h1>Edit  Group  %s</h1>'  %  gid)

def groups_delete(request,  gid):
    return  HttpResponse('<h1>Delete  Group  %s</h1>'  %  gid)

def groups_list(request):
        groups  =  (
            {'id':  1,
            'group_name':  u'МтМ-21',
            'starosta_name':  u'Боднар Ростислав'},
            {'id':  2,
            'group_name':  u'МтМ-22',
            'starosta_name':  u'Покорний Сергій'},
            {'id':  3,
            'group_name':  u'МтМ-23',
            'starosta_name':  u'Мальгінов Олександр'},)
        return  render(request,  'students/groups_list.html', {'groups':  groups})
