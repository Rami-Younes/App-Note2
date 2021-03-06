from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
# Create your views here.
from notes_app.models import Note
from django.contrib.auth.models import  User

def all_notes(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes': all_notes


    }
    return render(request, 'notes.html', context)


def detail(request, slug):
    note = Note.objects.get(slug=slug)
    #note = get_object_or_404(Note, slug=slug)
    context = {
        'note': note,
    }
    return render(request, 'one_note.html', context)


def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm()

    context = {
        'form': form
    }
    return render(request, 'add.html', context)




def edit(request, slug):
    note = get_object_or_404(Note, slug=slug)
    print(slug)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm(instance=note)

    context = {
        'form': form
    }
    return render(request, 'create.html', context)