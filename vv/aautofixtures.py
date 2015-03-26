import datetime
from vv.models import GlazeLookup
from autofixture import generators, register, AutoFixture
from autofixture.generators import ChoicesGenerator, DateTimeGenerator

class CommonFixture(AutoFixture):
    class Values:

        dd = generators.DateTimeGenerator(
            min_date=datetime(2009,1,1),
            max_date=datetime(2009,12,31))

        ii = generators.StringGenerator(self, chars=None, multiline=False,
                                        min_length=10, max_length= 30)
        
        #nn = generators.LoremWordGenerator(LoremGenerator):
            #count = 7
            #method = 'w'
            
        #ss = generators.LoremSentenceGenerator(LoremGenerator):
            #method = 's'          


class GlazeLookupFixture(AutoFixture):
    class Values:
        glaze_description = ii         
        glaze_name = generators.ChoicesGenerator(
            values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(',')
        )
        glaze_begin_date = dd
        glaze_end_date = dd
autofixture.register(GlazeLookup, GlazeLookupFixture, overwrite=False, fail_silently=False)
