from vv.models import GlazeLookup
import autofixture
from autofixture import AutoFixture, generators

class GlazeLookupFixture(AutoFixture):
    class Values:
 
        glaze_name = generators.ChoicesGenerator(
            values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(','))
             
    autofixture.register(GlazeLookup, GlazeLookupFixture)