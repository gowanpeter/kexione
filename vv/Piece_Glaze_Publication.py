from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from vv.forms.py import PieceModelForm, PublicationFormSet, GlazeFormSet

from vv.models import Piece

class PieceCreateView(CreateView):
    template_name = 'Piece_add.html'
    model = Piece
    form_class = PieceForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        Publication_form = PublicationFormSet()
        Glaze_form = GlazeFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  Publication_form=Publication_form,
                                  Glaze_form=Glaze_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        Publication_form = PublicationFormSet(self.request.POST)
        Glaze_form = GlazeFormSet(self.request.POST)
        if (form.is_valid() and Publication_form.is_valid() and
            Glaze_form.is_valid()):
            return self.form_valid(form, Publication_form, Glaze_form)
        else:
            return self.form_invalid(form, Publication_form, Glaze_form)

    def form_valid(self, form, Publication_form, Glaze_form):
        """
        Called if all forms are valid. Creates a Piece instance along with
        associated Publications and Glazes and then redirects to a
        success page.
        """
        self.object = form.save()
        Publication_form.instance = self.object
        Publication_form.save()
        Glaze_form.instance = self.object
        Glaze_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, Publication_form, Glaze_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  Publication_form=Publication_form,
                                  Glaze_form=Glaze_form))    