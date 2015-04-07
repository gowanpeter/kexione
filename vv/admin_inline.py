from django.contrib import admin
from vv.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

#@admin.register(Author, Reader, Editor, site=custom_admin_site)
#TabularInline
#StackedInline

class glaze_link_pieceInline(admin.StackedInline):
    model = GlazeLookup.glaze_pieces.through
    extra = 1

    raw_id_fields = ("piece", "glazeLookup", )

class PieceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [ 'piece_name', 'piece_description' ]
            }),
        ('Facts', {
            'fields': ['catalogue_id', 'heath_id', 'manufactured_date', 'cataloguer', 'catalogue_date'],
            }),
        ('Dimensions', {
            'fields': ['length_inches', 'width_inches', 'height_inches', 'weight_ounces', 'length_mm', 'width_mm', 'height_mm', 'weight_grams'],'classes': ['collapse']
            }),
    ]
    date_hierarchy = 'manufactured_date'
    inlines =  (glaze_link_pieceInline,)

class GlazeLookupAdmin(admin.ModelAdmin):
    inlines =  (glaze_link_pieceInline,)
    exclude = ('glaze_pieces',)

admin.site.register(Piece, PieceAdmin)
admin.site.register(GlazeLookup, GlazeLookupAdmin)
