from vv.models import GlazeLookup
import autofixture
from autofixture import generators
from autofixture.generators import ChoicesGenerator
from autofixture import generators, register, AutoFixture

class GlazeLookupAutoFixture(AutoFixture):
        field_values={
                'glaze_name': generators.ChoicesGenerator(
        values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(',') ),
        }
register(GlazeLookup, GlazeLookupAutoFixture)

