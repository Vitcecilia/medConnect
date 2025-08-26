from idlelib.browser import file_open

from django_filters.rest_framework import filters

from core import models

LIKE = 'unaccent__icontains'
ICONTAINS = 'icontains'
UNACCENT_TEXACT = 'unaccent_iexact'
EQUALS = 'exact'
NOT_EQUALS = 'iexact'
STARTS_WITH = 'startswith'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'
IN = 'contains'



class UserFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    cpf = filters.CharFilter(lookup_expr=ICONTAINS)

    class Meta:
        model = models.User
        fields = ['name', 'cpf']

class TelephoneFilters(filters.FilterSet):
    user = filters.CharFilter(lookup_expr=LIKE)
    id = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        models = models.Telephone
        fields = ['user', 'id']

class AddressFilter(filters.FiltersSet):
    user = filters.CharFilter(lookup_expr=LIKE)
    id = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Address
        fields = ['user', 'id']

class HealthInsuranceFilters(filters.FilterSet):
    id = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.HealthInsurance
        fields = ['id']

class PatientFilters(filters.FilterSet):
    user = filters.CharFilter(lookup_expr=LIKE)
    id = filters.CharFilter(lookup_expr=EQUALS)
    name = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Patient
        fields = ['id', 'name', 'user']

class PatientHealthInsuranceFilters(filters.FilterSet):
    type = filters.CharFilter(lookup_expr=LIKE)
    patient = filters.CharFilter(lookup_expr=LIKE)
    id = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.PatientHealthInsurance
        fields = ['type', 'patient', 'id']

class MedicFilters(filters.FilterSet):
    user = filters.CharFilter(lookup_expr=LIKE)
    crm = filters.CharFilter(lookup_expr=LIKE)
    specialization = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Medic
        fields = ['user', 'crm', 'specialization']

class SpecializationFilters(filter.Filters):
    name = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Specialization
        fields = ['name']

class ConsultationFilters(filters.FilterSet):
    id = filters.CharFilter(lookup_expr=EQUALS)
    medic = filters.CharFilter(lookup_expr=LIKE)
    patient = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Consultation
        fields = ['medic', 'patient']

class MedicationFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    type = filters.CharFilter(field_name='type_application',lookup_expr=LIKE)

    class Meta:
        model = models.Medication
        fields = ['name', 'type']

class MedicationConsultationFilters(filters.FilterSet):
   id = filters.CharFilter(lookup_expr=EQUALS)
   consultation = filters.CharFilter(lookup_expr=LIKE)

   class Meta:
       model = models.MedicationConsultation
       fields = ['consultation']






