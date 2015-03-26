

from __future__ import unicode_literals
from django.db import models

class Widget(models.Model):
    name = models.CharField(max_length=12)
    #next: forms.py

class Piece(models.Model):
    id = models.AutoField (primary_key=True)
    catalogue_id = models.CharField(max_length= 8)
    heath_id = models.CharField(max_length= 8, blank=True)
    piece_name = models.CharField(max_length=6, blank=True)
    piece_description = models.CharField(max_length= 12, blank=True)
    manufactured_date = models.DateField(blank=True, null=True)
    length_inches = models.IntegerField(blank=True, null=True)
    width_inches = models.IntegerField(blank=True, null=True)
    height_inches = models.IntegerField(blank=True, null=True)
    weight_ounces = models.IntegerField(blank=True, null=True)
    length_mm = models.IntegerField(blank=True, null=True)
    width_mm = models.IntegerField(blank=True, null=True)
    height_mm = models.IntegerField(blank=True, null=True)
    weight_grams = models.IntegerField(blank=True, null=True)
    cataloguer = models.CharField(max_length=8, blank=True)
    catalogue_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.piece_name


conditions = (
    ('a', 'Pristine' ),
    ('b', 'Used, good'),
    ('c', 'Used, worn'),
    ('d', 'Cracked / chipped'),
    ('e', 'Broken'),
)
#choice
class Condition(models.Model):

    name = models.CharField(max_length=8, blank=True)
    condition = models.CharField(max_length=1, choices=conditions, default = 'b')

    def __str__(self):
        return self.name

#many to many
class Documentation(models.Model):
    documentation_name = models.CharField(max_length=8, blank=True)
    documentation_pieces = models.ManyToManyField(Piece, through="documentation_link_piece")

    def __str__(self):
        return self.documentation_name

class documentation_link_piece(models.Model):
    documentation = models.ForeignKey(Documentation)
    piece = models.ForeignKey(Piece)
    documentation_date = models.DateField(blank=True, null=True)
    documentation_author = models.CharField(max_length=8, blank=True)
    documentation_media = models.CharField(max_length=8, blank=True)
    documentation_location = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return "documentation_link_piece"

#one to many
#one exhibition has many pieces, foreign key is exibition_id and is in pieces
#exhibition = models.ForeignKey('exhibition')
class ExhibitionLookup(models.Model):
    exhibition_name = models.CharField(max_length=8, blank=True)
    exhibition_date = models.DateField(blank=True, null=True)
    exhibition_description = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.exhibition_name
    
class exhibition_link_piece(models.Model):
    piece = models.ForeignKey(Piece)
    exhibition = models.ForeignKey(ExhibitionLookup)

#many to many

class GlazeLookup(models.Model):
    glaze_name = models.CharField(max_length=8, blank= False, default = 'boola', unique = True)
    glaze_pieces = models.ManyToManyField(Piece, through="glaze_link_piece")
    glaze_description = models.CharField(max_length=12, blank=True)
    glaze_begin_date = models.DateField(blank=True, null=True)
    glaze_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.glaze_name

class glaze_link_piece(models.Model):
    piece = models.ForeignKey(Piece)
    glaze = models.ForeignKey(GlazeLookup)
    batch =  models.CharField(max_length=12, blank= False, default = '200')

    def __str__(self):
        return "glaze_link_piece"

#many to many
class HeathLineLookup(models.Model):
    heath_line_name = models.CharField(max_length=8, blank=True)
    heath_line_pieces = models.ManyToManyField(Piece, through="heath_line_link_piece")
    heath_line_begin_date = models.DateField(blank=True, null=True)
    heath_line_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.heath_line_name

class heath_line_link_piece(models.Model):
    piece = models.ForeignKey(Piece)
    heath_line = models.ForeignKey(HeathLineLookup)
    feature =  models.CharField(max_length=12, blank= False, default = 'too true')

    def __str__(self):
        return "heath_line_link_piece"

##many to many
class Logo(models.Model):
    Logo_name = models.CharField(max_length=8, blank=True)
    logo_pieces = models.ManyToManyField(Piece, through="logo_link_piece")
    logo_description = models.CharField(max_length=12, blank=True)
    stamp_name = models.CharField(max_length=8, blank=True)
    picture = models.TextField(blank=True)

    def __str__(self):
        return self.Logo_name
    
class logo_link_piece(models.Model):
    Piece = models.ForeignKey(Piece)
    Logo = models.ForeignKey(Logo)    
    feature =  models.CharField(max_length=12, blank= False, default = 'too true')


#many to many
class MakerLookup(models.Model):
    maker_name = models.CharField(max_length=8, blank=True)
    maker_pieces = models.ManyToManyField(Piece, through="maker_link_piece")
    maker_location = models.CharField(max_length=8, blank=True)
    maker_start_date = models.DateField(blank=True, null=True)
    maker_stop_date = models.DateField(blank=True, null=True)
    maker_description = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.maker_name

class maker_link_piece(models.Model):
    Piece = models.ForeignKey(Piece)
    MakerLookup = models.ForeignKey(MakerLookup)
    feature =  models.CharField(max_length=12, blank= False, default = 'too true')


    def __str__(self):
        return "maker_link_piece"

#many to many
class MaterialLookup(models.Model):
    material_name = models.CharField(max_length=8, blank=True)
    material_pieces = models.ManyToManyField(Piece, through="material_link_piece")
    material_description = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.material_name

class material_link_piece(models.Model):
    Piece = models.ForeignKey(Piece)
    MaterialLookup = models.ForeignKey(MaterialLookup)
    feature =  models.CharField(max_length=12, blank= False, default = 'too true')


    def __str__(self):
        return "material_link_piece"

#many to many
class MethodLookup(models.Model):
    method_name = models.CharField(max_length=8, blank=True)
    method_pieces = models.ManyToManyField(Piece, through="method_link_piece")
    method_description = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.method_name

class method_link_piece(models.Model):
    Piece = models.ForeignKey(Piece)
    MethodLookup = models.ForeignKey( MethodLookup)
    feature =  models.CharField(max_length=12, blank= False, default = 'too true')


    def __str__(self):
        return "method_link_piece"




#one to many
#one publication has many pieces, foreign key is publication_id and is in table 'Pieces'
#publication = models.ForeignKey('publication')

class PublicationLookup(models.Model):
    publication_name = models.CharField(max_length=8, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    publication_author = models.CharField(max_length=8, blank=True)
    publication_media = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.publication_name

class publication_link_piece(models.Model):
    piece = models.ForeignKey(Piece)
    publication = models.ForeignKey(PublicationLookup)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=8, blank=True)
    publication_author = models.CharField(max_length=8, blank=True)

#many to many
class SetCollection(models.Model):
    set_collection_name = models.CharField(max_length=8, blank=True)
    set_collection_piece = models.ManyToManyField(Piece, through="setCollection_link_piece")
    setcollection_location = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.set_collection_name

class setCollection_link_piece(models.Model):
    Piece = models.ForeignKey(Piece)
    SetCollection = models.ForeignKey(SetCollection)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return "setCollection_link_piece"