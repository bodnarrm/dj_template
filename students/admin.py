from  django.contrib  import  admin
from  .models  import  Student,Group

class  GroupAdmin(admin.ModelAdmin):
    list_display  =  ['title',  'leader',  'notes']
    list_display_links  =  ['title']
    list_editable  =  ['leader']
    ordering  =  ['title']
    list_filter  =  ['leader']
    list_per_page  =  5
    search_fields  =  ['title',  'leader']

    def  view_on_site(self,  obj):
        return  reverse('groups_lisr')

class  StudentAdmin(admin.ModelAdmin):
    list_display  =  ['last_name',  'first_name',  'ticket',  'student_group']
    list_display_links  =  ['last_name',  'first_name']
    list_editable  =  ['student_group']
    ordering  =  ['last_name']
    list_filter  =  ['student_group']
    list_per_page  =  5
    search_fields  =  ['last_name',  'first_name',  'middle_name',  'ticket', 'notes']

    def  view_on_site(self,  obj):
        return  reverse('students_edit',  kwargs={'pk':  obj.id})

#  Register  your  models  here.
admin.site.register(Student,  StudentAdmin)
admin.site.register(Group,GroupAdmin)