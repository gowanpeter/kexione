from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from vv.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece



class GlazeLookupAdmin(admin.ModelAdmin):
    filter_horizonal = ('glaze_pieces',)

class PieceAdminForm(forms.ModelForm):

    glazeLookups = forms.ModelMultipleChoiceField(
        queryset=GlazeLookup.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Glazes'),
            is_stacked=False
        )
    )

    class Meta:
        model = Piece
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(PieceAdminForm).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['glazeLookups'].initial = self.instance.glazeLookups.all()

    def save(self, commit=True):
        piece = super(PieceAdminForm, self).save(commit=False)

        if commit:
            piece.save()

        if piece.pk:
            piece.glazeLookup = self.cleaned_data['glazeLookups']
            self.save_m2m()

        return piece

class PieceAdmin(admin.ModelAdmin):
    form = PieceAdminForm

admin.site.register(GlazeLookup, GlazeLookupAdmin)
admin.site.register(Piece, PieceAdmin)