from django.shortcuts import render , HttpResponse,redirect
from .models import Message,Comment
from login_register_app.models import User
from django.contrib import messages
from datetime import datetime,timedelta
import pytz

#1
def index(request):
    if not ('userId' in request.session):
        messages.error(request, "Need to login first", 'alert alert-danger')
        return render(request,'posts.html')
    user = User.objects.filter(id = request.session['userId']).first()

    present = pytz.utc.localize(datetime.utcnow())
    #extract the present time in a formate that is == created_at formate in Message model
    present = present - timedelta(minutes=30)
    #subtract 30 minutes from the present time, to compare the message.created_at date to the present date-30 minutes, if present-30min > created_at => the message is created before 30 mins, else the message doesn't exceed 30 min from posting it, then it can be deleted.

    currentUser = request.session['userId']
    print('')
    context = {
        'user' : user,
        'posts': Message.objects.all().order_by('-created_at'),
        'present_30':present,
        'currentUser':currentUser,
    }
    return render(request,'posts.html',context)

#2
def post(request):
    if request.method != 'POST':
        return redirect('/wall')
    user = User.objects.get(id = request.session['userId'])
    postStr = request.POST.get('post')
    post = Message.objects.create(message = postStr,user=user)

    return redirect('/wall')

#3
def comment(request,postId):
    if request.method != 'POST':
        return redirect('/wall')
    #return the post from db to assign the comment to a specific post:
    post = Message.objects.filter(id=postId).first()

    #check if the post exist:
    if not(post):
        messages.error(request, "Coudn't Found the post to comment", 'alert alert-danger')
        return redirect('/wall')

    #returning the CURRENT user id to assign the comment to the user:
    user = User.objects.get(id = request.session['userId'])

    #extracting the comment from the form.
    commentStr = request.POST.get('comment')

    #creating new comment object.

    Comment.objects.create(comment=commentStr,user=user,message=post)
    return redirect('/wall')

#4
def deleteMsg(request,postId):
    if request.method != 'POST':
        return redirect('/wall')
    post = Message.objects.filter(id=postId).first()
    print('--'*50,post)
    post.delete()
    return redirect('/wall')

#5
def deleteComment(request,comId):
    if request.method != 'POST':
        return redirect('/wall')
    
    comment = Comment.objects.filter(id=comId).first()
    print('--'*50,comment)
    comment.delete()
    return redirect('/wall')