
from django.contrib import admin
from vv.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

#ACTION FUNCTION
#The current ModelAdmin
#An HttpRequest representing the current request,
#A QuerySet containing the set of objects selected by the user.
#Use queryset.method(...) or iterate over each object individually.
#for obj in queryset:
    #do_something_with(obj)
    
class PieceAdmin(admin.ModelAdmin):
    #Add_filters
    list_filter = ('Piece.piece_name', 'GlazeLookup.glaze_name')

    #Make Searchable (even as related fields)
    search_fields = ('Piece.piece_name', 'GlazeLookup.glaze_name')

    def wikipedia_link(self, object):
        return u" < a href = 'http://en.wikipedia.org/wiki/%s' > link < / a > "% obj.name.replace(" ", "_")
        
    #allow tags to a string
    wikipedia_link.allow_tags = True

    #list a boolean (even from a method) uses on/off icons
    def is_groovey(self, obj):Piece.
        return obj.feature < 3
        is_groovey.boolean = True

    #allow editing of field
    list_editable = ('Piece.nickname', )


admin.site.register(Piece, PieceAdmin)

class ConditionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Condition, ConditionAdmin)

class glaze_link_pieceInline(admin.TabularInline):
    model = glaze_link_piece
    extra = 1
    #form = MyGlazeLookupForm
   
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  (glaze_link_pieceInline,)
        
class GlazeLookupAdmin(admin.ModelAdmin):
    inlines =  (glaze_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(GlazeLookup, GlazeLookupAdmin)    


class documentation_link_pieceInline(admin.TabularInline):
    model = documentation_link_piece
    extra = 1
    #form = MyDocumentationForm
   
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  (documentation_link_pieceInline,)
        
class DocumentationAdmin(admin.ModelAdmin):
    inlines =  (documentation_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(Documentation, DocumentationAdmin)


class exhibition_link_pieceInline(admin.TabularInline):
    model = exhibition_link_piece
    extra = 1
    #form = MyExhibitionLookupForm
   
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  (exhibition_link_pieceInline,)
        
class ExhibitionLookupAdmin(admin.ModelAdmin):
    inlines =  (exhibition_link_pieceInline,)
    PieceAdmin
#admin.site.register(Piece, PieceAdmin)
admin.site.register(ExhibitionLookup, ExhibitionLookupAdmin)


class  heath_line_link_pieceInline(admin.TabularInline):
    model =  heath_line_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  ( heath_line_link_pieceInline,)
        
class HeathLineLookupAdmin(admin.ModelAdmin):
    inlines =  ( heath_line_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(HeathLineLookup, HeathLineLookupAdmin)


class  logo_link_pieceInline(admin.TabularInline):
    model =  logo_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  ( logo_link_pieceInline,)
        
class LogoAdmin(admin.ModelAdmin):
    inlines =  ( logo_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(Logo, LogoAdmin)


class  maker_link_pieceInline(admin.TabularInline):
    model =  maker_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  ( maker_link_pieceInline,)
        
class MakerLookupAdmin(admin.ModelAdmin):
    inlines =  ( maker_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(MakerLookup, MakerLookupAdmin)


class   material_link_pieceInline(admin.TabularInline):
    model =   material_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  (  material_link_pieceInline,)
        
class MaterialLookupAdmin(admin.ModelAdmin):
    inlines =  (  material_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(MaterialLookup, MaterialLookupAdmin)


class  method_link_pieceInline(admin.TabularInline):
    model =  method_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  ( method_link_pieceInline,)
        
class MethodLookupAdmin(admin.ModelAdmin):
    inlines =  ( method_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(MethodLookup, MethodLookupAdmin)


class   publication_link_pieceInline(admin.TabularInline):
    model =   publication_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  (  publication_link_pieceInline,)
        
class PublicationLookupAdmin(admin.ModelAdmin):
    inlines =  (  publication_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(PublicationLookup, PublicationLookupAdmin)


class  setCollection_link_pieceInline(admin.TabularInline):
    model =  setCollection_link_piece
    extra = 1
    
class PieceAdmin(admin.ModelAdmin):
    inlines =  ( setCollection_link_pieceInline,)
        
class SetCollectionAdmin(admin.ModelAdmin):
    inlines =  ( setCollection_link_pieceInline,)
    
#admin.site.register(Piece, PieceAdmin)
admin.site.register(SetCollection, SetCollectionAdmin)

##Add_filters
#list_filter = ('piece', 'glaze_name')

##Make Searchable (even as related fields)
#search_fields = ('piece_name', 'glaze_name')

#def wikipedia_link(self, object):
    #return u" < a href = 'http://en.wikipedia.org/wiki/%s' > link < / a > "% obj.name.replace(" ", "_")
    
##allow tags to a string
#wikipedia_link.allow_tags = True

###list a boolean (even from a method) uses on/off icons
##def is_groovey(self, obj):
    ##return obj.feature < 3
##is_groovey.boolean - True

##allow editing of field
#list_editable = ('nickname', )


