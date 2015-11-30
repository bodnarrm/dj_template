from  django.views.generic.edit  import  FormView

class  ContactView(FormView):
    template_name  =  'contact_form.html'
    form_class  =  ContactForm
    success_url  =  '/email-sent/'

    def  form_valid(self,  form):
    """This  method  is  called  for  valid  data"""
    subject  =  form.cleaned_data['subject']
    message  =  form.cleaned_data['message']
    from_email  =  form.cleaned_data['from_email']

    send_mail(subject,  message,  from_email,  ['admin@gmail.com'])

    return  super(ContactView,  self).form_valid(form)