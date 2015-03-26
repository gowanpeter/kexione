from django.shortcuts import render, render_to_response, RequestContext
from vv.forms import MyPieceForm, MyGlazeLookupForm, DocumentationForm, ConditionForm, ExhibitionLookupForm, HeathLineLookupForm, LogoForm, MakerLookupForm, MaterialLookupForm, MethodLookupForm, PublicationForm, SetCollectionForm

def home(request):

    form = MyPieceForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def GlazeView(request):

    form = MyGlazeLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

def DocumentationView(request):

    form = DocumentationForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

def ConditionView(request):

    form = ConditionForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def ExhibitionLookupView(request):

    form = ExhibitionLookupForm
    
    Form(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def HeathLineLookupView(request):

    form = HeathLineLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))



def LogoView(request):

    form = LogoForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

def MakerLookupView(request):

    form = MakerLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def MaterialLookupView(request):

    form = MaterialLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def MethodLookupView(request):

    form = MethodLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def PublicationView(request):

    form = PublicationForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def SetCollectionView(request):

    form = SetCollectionForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()



    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))



