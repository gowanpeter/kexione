from django import forms
from vv.models import Piece, GlazeLookup, Documentation, Condition, ExhibitionLookup, HeathLineLookup, Logo, MakerLookup, MaterialLookup, MethodLookup, PublicationLookup, SetCollection
from django.forms import ModelForm

from vv.models import Widget

#class WidgetForm(forms.ModelForm):
        #def __init__(self, *args, **kwargs):
        #super(WidgetForm, self).__init__(*args, **kwargs)
        #self.fields['my_extra_field'] = forms.CharField()

        #class Meta:
        #model = Widget
#now, to admin.py


#class PieceForm(forms.ModelForm):
        #class Meta:
        #model = Piece
        #fields = "__all__"

class MyPieceForm(forms.Form):
        model = Piece
        #fields = "__all__"
        field1 = forms.ModelChoiceField(queryset=GlazeLookup.objects.all())

#Create the form class
#class GlazeLookupForm(forms.ModelForm):
        #class Meta:
        #model = GlazeLookup
        #fields = "__all__"

class MyGlazeLookupForm(forms.Form):
        model = GlazeLookup
        field1 = forms.ModelChoiceField(queryset=GlazeLookup.objects.all())

#form to add a glaze
#form = GlazeLookupForm(ModelForm)

#form to change an existing glaze
#glaze = GlazeLookup.objects.get(pk=1)
#form = GlazeLookupForm(instance=glaze)

#many to many
#Create the form class
class DocumentationForm(forms.ModelForm):
        class Meta:
                model = Documentation
                fields = "__all__"

#class MyDocumentationForm(forms.Form):
                #location = forms.MultipleModelChoiceField(
                        #queryset=Documentation.objects.all())


class ExhibitionLookupForm(forms.ModelForm):
        class Meta:
                model = ExhibitionLookup
                fields = "__all__"

#class MyExhibitionLookupForm(forms.Form):
                #location = forms.MultipleModelChoiceField(
                        #queryset=Exhibition.objects.all())

class ConditionForm(forms.ModelForm):
        class Meta:
                model = Condition
                fields = ['name', 'condition']


class HeathLineLookupForm(forms.ModelForm):
        class Meta:
                model = HeathLineLookup
                fields = "__all__"


class LogoForm(forms.ModelForm):
        class Meta:
                model = Logo
                fields = "__all__"


class MakerLookupForm(forms.ModelForm):
        class Meta:
                model = MakerLookup
                fields ="__all__"


class MaterialLookupForm(forms.ModelForm):
        class Meta:
                model = MaterialLookup
                fields = "__all__"


class MethodLookupForm(forms.ModelForm):
        class Meta:
                model = MethodLookup
                fields = "__all__"


class PublicationForm(forms.ModelForm):
        class Meta:
                model = PublicationLookup
                fields = "__all__"


class SetCollectionForm(forms.ModelForm):
        class Meta:
                model = SetCollection
                fields = "__all__"





