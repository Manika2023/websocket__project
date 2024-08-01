from django.shortcuts import render
from .models import Group,Chat
# Create your views here.
def index(request,group_name):
     group=Group.objects.filter(name=group_name).first()
     # if it exist already
     chats=[]
     if group:
          # then chat display
          chats = Chat.objects.filter(group=group)

          pass
     else:
     #   if group name is not then pass
       print("grp name ",group_name)
       group = Group(name=group_name)
       group.save()
     return render(request,'app/index.html',{'groupname':group_name,'chats':chats})