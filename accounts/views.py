from django.views.generic import TemplateView

# Create your views here.
class UserList(TemplateView):
    template_name = 'accounts/userlist.html'

class UserDetail(TemplateView):
    template_name = 'accounts/userdetail.html'

class UserRegister(TemplateView):
    template_name = 'accounts/userregister.html'

class UserDelete(TemplateView):
    template_name = 'accounts/userdelete.html'

class UserUpdate(TemplateView):
    template_name = 'accounts/userupdate.html'

class UserLogin(TemplateView):
    template_name = 'accounts/userlogin.html'

