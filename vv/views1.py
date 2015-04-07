
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

#from vv.forms import MyPieceForm, PieceModelForm, MyGlazeLookupForm, DocumentationForm, ConditionForm, ExhibitionLookupForm, HeathLineLookupForm, LogoForm, MakerLookupForm, MaterialLookupForm, MethodLookupForm, PublicationForm, SetCollectionForm, NameForm

from vv.forms import PieceModelForm, GlazeLookupModelForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from django.forms.models import modelformset_factory

from vv.models import Piece



def PieceView(request):

    form = PieceModelForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


#def PieceView(request, piece_id) :
    #class PieceModelForm(forms.ModelForm):
        #class Meta:
            #model = Piece
            #fields = "__all__"

    #model = get _object_or_404(Piece, pk = piece_id)
    #form = PieceModelForm(instance = piece)

    #return render(request, 'iterateModel.html', { 'form': form})

def GlazeView(request):

    form = GlazeLookupModelForm(request.POST or None)

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



