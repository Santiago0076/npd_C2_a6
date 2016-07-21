from ..general.expressions import polite
from ..countries.us import locations as us_worst
from ..countries.uk import locations as locations_uk_worst
# DO NOT EDIT BELOW THIS LINE
phrase = polite("I truly hate {} in US, and really hate {} in UK".format(
    us.worst,
    locations_uk.worst,
))
