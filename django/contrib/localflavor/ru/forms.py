"""
Russian-specific forms helpers
"""
import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Select, RegexField
from django.utils.translation import ugettext_lazy as _

phone_digits_re = re.compile(r'^(?:[78]-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')


class RUCountySelect(Select):
    """
    A Select widget that uses a list of Russian Counties as its choices.
    """
    def __init__(self, attrs=None):
        from ru_regions import RU_COUNTY_CHOICES
        super(RUCountySelect, self).__init__(attrs, choices=RU_COUNTY_CHOICES)


class RURegionSelect(Select):
    """
    A Select widget that uses a list of Russian Regions as its choices.
    """
    def __init__(self, attrs=None):
        from ru_regions import RU_REGIONS_CHOICES
        super(RURegionSelect, self).__init__(attrs, choices=RU_REGIONS_CHOICES)


class RUPostalCodeField(RegexField):
    """
    Russian Postal code field.
    Format: XXXXXX, where X is any digit, and first digit is not zero.
    """
    default_error_messages = {
        'invalid': _(u'Enter a postal code in the format XXXXXX.'),
    }
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(RUPostalCodeField, self).__init__(r'^\d{6}$',
            max_length, min_length, *args, **kwargs)


class RUPassportNumberField(RegexField):
    """
    Russian internal passport number format:
    XXXX XXXXXX where X - any digit.
    """
    default_error_messages = {
        'invalid': _(u'Enter a passport number in the format XXXX XXXXXX.'),
    }
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(RUPassportNumberField, self).__init__(r'^\d{4} \d{6}$',
            max_length, min_length, *args, **kwargs)


class RUAlienPassportNumberField(RegexField):
    """
    Russian alien's passport number format:
    XX XXXXXXX where X - any digit.
    """
    default_error_messages = {
        'invalid': _(u'Enter a passport number in the format XX XXXXXXX.'),
    }
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(RUAlienPassportNumberField, self).__init__(r'^\d{2} \d{7}$',
            max_length, min_length, *args, **kwargs)
