from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Note, Profile, LikeNotes
from django.contrib import messages, auth

@login_required(login_url='signin')
def index(request):
    query = request.GET.get('query','')
    current_route = "home"
    if query:
        notes = Note.objects.filter(Q(title__icontains=query))
    else:
        notes = Note.objects.all()
    return render(request, 'core/index.html',{
        "notes":notes,
        "like_notes":like_notes,
        "current_route":current_route
    })

@login_required(login_url='signin')
def new(request):
    current_route = "new"
    if request.method == "POST":
        user = request.user.username
        title = request.POST['title']
        description = request.POST['description']

        new_note = Note.objects.create(user=user, title=title, description=description)
        new_note.save()
        return redirect('/')
    
    return render(request, 'core/new.html', {"current_route":current_route})

@login_required(login_url='signin')
def detail(request,pk):
    note = get_object_or_404(Note,pk=pk)
    print(note.user)

    return render(request, 'core/detail.html',{
        "note":note
    })

@login_required(login_url="signin")
def like_notes(request):
    username = request.user.username
    notes_id = request.GET.get('note_id')

    notes = Note.objects.get(id=notes_id)
    print(notes)

    likes_filter = LikeNotes.objects.filter(notes_id=notes_id, username=username).first()

    if likes_filter == None:
        new_like = LikeNotes.objects.create(username=username, notes_id=notes_id)
        new_like.save()
        
        notes.no_of_likes = notes.no_of_likes + 1
        notes.save()

        print(notes.no_of_likes)
        
        return redirect('/')
    else:
        likes_filter.delete()
        notes.no_of_likes = notes.no_of_likes-1
        notes.save()
        return redirect('/')


@login_required(login_url='signin')
def delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()

    return redirect('/')

@login_required(login_url="signin")
def edit(request,pk):
    note = get_object_or_404(Note, pk=pk)
    print(note.title)
    print(note.description)
    if request.method == "POST":
        user = request.user.username
        title = request.POST['title']
        description = request.POST['description']
        note.title = title
        note.description = description
        note.save()
        return redirect("/")
    
    return render(request,'core/edit.html', {"title":note.title,"desc":note.description})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, "email taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save()

                new_profile = Profile.objects.create(user= user,id_user = user.id)
                new_profile.save()
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                return redirect('/')
        else:
            messages.info(request, "password not match")
            return redirect('signup')
    else:
        return render(request, 'core/signup.html')
    
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "credential invalid")
            return redirect('signin')
    else:
        return render(request, 'core/signin.html')
    
@login_required(login_url='signin')
def profile(request,pk):
    user = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user)
    user_notes = Note.objects.filter(user=pk)
    current_route = "profile"

    return render(request, 'core/profile.html',{
        'user_profile':user_profile,
        "user_notes":user_notes,
        "current_route":current_route
    })