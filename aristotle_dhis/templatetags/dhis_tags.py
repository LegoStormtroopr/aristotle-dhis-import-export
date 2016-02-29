from django import template
register = template.Library()

@register.simple_tag
def public_flags(item):

    return "r-------"

@register.simple_tag
def value_type(item):

    type_map = {
        #"":"Code",
        "Date/Time":"DATE",
        #"":"ExternalCategory",
        #"":"GeographicLocationCode",
        #"":"GeographicStructureCode",
        "Number":"NUMBER",
        "Currency":"NUMBER",
        #"":"Scale",
        "String":"TEXT"
    }
    value_type = "TEXT"
    num_values = item.permissiblevalue_set.all().count()
    if item.data_type and num_values == 0:
        value_type = type_map.get(item.data_type.name)
    elif num_values > 0:
        value_type = "TEXT"
    
    return value_type