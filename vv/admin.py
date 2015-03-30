
from django.contrib import admin

from .models import Piece, GlazeLookup, glaze_link_piece

#from vv.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piecedef PieceView(request, piece_id) :



#from vv.models imtabular.htmlport Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

#class PieceAdmin(admin.ModelAdmin):
    #pass
#admin.site.register(Piece, PieceAdmin)

class glaze_link_pieceInline(admin.TabularInline):
    list_display = ['batch']
    list_filter = ['piece', 'glazeLookup']
    search_fields = ['piece__piece_name']
    model = glaze_link_piece
    extra = 1

class PieceAdmin(admin.ModelAdmin):
    list_display = ['catalogue_id', 'heath_id', 'piece_name', 'piece_description', 'manufactured_date' , 'length_inches', 'width_inches', 'height_inches', 'weight_ounces', 'length_mm',  'width_mm', 'height_mm', 'weight_grams', 'cataloguer', 'catalogue_date']
    inlines =  (glaze_link_pieceInline,)
    search_fields = ['piece__piece_name']

class GlazeLookupAdmin(admin.ModelAdmin):
    list_display = ['glaze_name', 'glaze_description', 'glaze_begin_date',  'glaze_end_date']
    search_fields = ['piece__piece_name']
    filter_horizontal = ('glaze_pieces',)
    #filter_vertical = ('glaze_pieces',)
    inlines =  (glaze_link_pieceInline,)

admin.site.register(Piece, PieceAdmin)
admin.site.register(GlazeLookup, GlazeLookupAdmin)


#class documentation_link_pieceInline(admin.TabularInline):
    #model = documentation_link_piece
    #extra = 4
    ##form = MyDocumentationForm


#class PieceAdmin(admin.ModelAdmin):
    #inlines =  (documentation_link_pieceInline,)

#class DocumentationAdmin(admin.ModelAdmin):
    #inlines =  (documentation_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(Documentation, DocumentationAdmin)


#class exhibition_link_pieceInline(admin.TabularInline):
    #model = exhibition_link_piece
    #extra = 4
    ##form = MyExhibitionLookupForm


#class PieceAdmin(admin.ModelAdmin):
    #inlines =  (exhibition_link_pieceInline)

#class ExhibitionLookupAdmin(admin.ModelAdmin):
    #inlines =  (exhibition_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(ExhibitionLookup, ExhibitionLookupAdmin)


#class  heath_line_link_pieceInline(admin.TabularInline):
    #model =  heath_line_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  ( heath_line_link_pieceInline,)

#class HeathLineLookupAdmin(admin.ModelAdmin):
    #inlines =  ( heath_line_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(HeathLineLookup, HeathLineLookupAdmin)


#class  logo_link_pieceInline(admin.TabularInline):
    #model =  logo_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  ( logo_link_pieceInline,)

#class LogoAdmin(admin.ModelAdmin):
    #inlines =  ( logo_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(Logo, LogoAdmin)


#class  maker_link_pieceInline(admin.TabularInline):
    #model =  maker_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  ( maker_link_pieceInline,)

#class MakerLookupAdmin(admin.ModelAdmin):
    #inlines =  ( maker_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(MakerLookup, MakerLookupAdmin)


#class   material_link_pieceInline(admin.TabularInline):
    #model =   material_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  (  material_link_pieceInline,)

#class MaterialLookupAdmin(admin.ModelAdmin):
    #inlines =  (  material_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(MaterialLookup, MaterialLookupAdmin)


#class  method_link_pieceInline(admin.TabularInline):
    #model =  method_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  ( method_link_pieceInline,)

#class MethodLookupAdmin(admin.ModelAdmin):
    #inlines =  ( method_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(MethodLookup, MethodLookupAdmin)


#class   publication_link_pieceInline(admin.TabularInline):
    #model =   publication_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  (  publication_link_pieceInline,)

#class PublicationLookupAdmin(admin.ModelAdmin):
    #inlines =  (  publication_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(PublicationLookup, PublicationLookupAdmin)


#class  setCollection_link_pieceInline(admin.TabularInline):
    #model =  setCollection_link_piece
    #extra = 4

#class PieceAdmin(admin.ModelAdmin):
    #inlines =  ( setCollection_link_pieceInline,)

#class SetCollectionAdmin(admin.ModelAdmin):
    #inlines =  ( setCollection_link_pieceInline,)

##admin.site.register(Piece, PieceAdmin)
#admin.site.register(SetCollection, SetCollectionAdmin)


