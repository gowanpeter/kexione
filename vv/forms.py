from django import forms
from vv.models import Piece

class PieceModelForm(forms.ModelForm):

    class Meta:
        model = Piece
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['piece_name'].queryset = Piece.avail.all()