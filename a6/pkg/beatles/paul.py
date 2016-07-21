from ..general.expressions import polite as expressions_polite
from ..countries.us import locations as us
from ..countries.uk import locations as uk
# DO NOT EDIT BELOW THIS LINE
phrase = expressions_polite("love {} in US, love {} in UK".format(
    us.best,
    uk.best,
))
