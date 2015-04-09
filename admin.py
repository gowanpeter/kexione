from django.contrib import admin
from vv.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

#@admin.register(Author, Reader, Editor, site=custom_admin_site)


#StackedInline
#StackedInline

class glaze_link_pieceInline(admin.StackedInline):
   model = GlazeLookup.glaze_pieces.through
   extra = 1
   #form = MyGlazeLookupForm


class PieceAdmin(admin.ModelAdmin):
   fieldsets = [
      (None, {
         'fields': [ 'piece_name', 'piece_description' ]
         }),
      ('Facts', {
         'fields': ['catalogue_id', 'heath_id', 'manufactured_date', 'cataloguer', 'catalogue_date'],
         }),
      ('Dimensions', {
         'fields': ['length_inches', 'width_inches', 'height_inches', 'weight_ounces', 'length_mm', 'width_mm', 'height_mm', 'weight_grams'],
         'classes': ['grp-collapse grp- closed',],
         }),
         ]

   date_hierarchy = 'manufactured_date'
   inlines =  (glaze_link_pieceInline,)

class GlazeLookupAdmin(admin.ModelAdmin):
   inlines =  (glaze_link_pieceInline,)
   exclude = ('glaze_pieces',)

admin.site.register(Piece, PieceAdmin)
admin.site.register(GlazeLookup, GlazeLookupAdmin)


class documentation_link_pieceInline(admin.StackedInline):
   model = Documentation.documentation_pieces.through
   model = documentation_link_piece
   extra = 1
   #form = MyDocumentationForm


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
   inlines =  (documentation_link_pieceInline,)

class DocumentationAdmin(admin.ModelAdmin):
   inlines =  (documentation_link_pieceInline,)
   exclude = ('documentation_pieces',)
#admin.site.register(Piece, PieceAdmin)
admin.site.register(Documentation, DocumentationAdmin)


class exhibition_link_pieceInline(admin.StackedInline):
   model = exhibition_link_piece
   extra = 1
   #form = MyExhibitionLookupForm


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
   inlines =  (exhibition_link_pieceInline,)

class ExhibitionLookupAdmin(admin.ModelAdmin):
   inlines =  (exhibition_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(ExhibitionLookup, ExhibitionLookupAdmin)


class  heath_line_link_pieceInline(admin.StackedInline):
   model =  heath_line_link_piece
   extra = 1

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
   inlines =  ( heath_line_link_pieceInline,)

class HeathLineLookupAdmin(admin.ModelAdmin):
   inlines =  ( heath_line_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(HeathLineLookup, HeathLineLookupAdmin)


class  logo_link_pieceInline(admin.StackedInline):
   model =  logo_link_piece
   extra = 1

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
   inlines =  ( logo_link_pieceInline,)

class LogoAdmin(admin.ModelAdmin):
   inlines =  ( logo_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(Logo, LogoAdmin)


class  maker_link_pieceInline(admin.StackedInline):
   model =  maker_link_piece
   extra = 1

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
   inlines =  ( maker_link_pieceInline,)

class MakerLookupAdmin(admin.ModelAdmin):
   inlines =  ( maker_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(MakerLookup, MakerLookupAdmin)


class   material_link_pieceInline(admin.StackedInline):
   model =   material_link_piece
   extra = 1

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
   inlines =  (  material_link_pieceInline,)

class MaterialLookupAdmin(admin.ModelAdmin):
   inlines =  (  material_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(MaterialLookup, MaterialLookupAdmin)


class  method_link_pieceInline(admin.StackedInline):
   model =  method_link_piece
   extra = 1

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
   inlines =  ( method_link_pieceInline,)

class MethodLookupAdmin(admin.ModelAdmin):
   inlines =  ( method_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(MethodLookup, MethodLookupAdmin)


class   publication_link_pieceInline(admin.StackedInline):
   model =   publication_link_piece
   extra = 1

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
   inlines =  (  publication_link_pieceInline,)

class PublicationLookupAdmin(admin.ModelAdmin):
   inlines =  (  publication_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(PublicationLookup, PublicationLookupAdmin)


class  setCollection_link_pieceInline(admin.StackedInline):
   model =  setCollection_link_piece
   extra = 1

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
   inlines =  ( setCollection_link_pieceInline,)

class SetCollectionAdmin(admin.ModelAdmin):
   inlines =  ( setCollection_link_pieceInline,)

#admin.site.register(Piece, PieceAdmin)
admin.site.register(SetCollection, SetCollectionAdmin)
