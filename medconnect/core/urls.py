from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()

router.register('users', viewsets.UserViewSet)
router.register('telephones', viewsets.TelephoneViewSet)
router.register('addresses', viewsets.AddressViewSet)
router.register('healthinsurance', viewsets.HealthInsuranceViewSet)
router.register('blood_types', viewsets.BloodTypeViewSet)
router.register('patients', viewsets.PatientViewSet)
router.register('medics', viewsets.MedicationViewSet)
router.register('specializations', viewsets.SpecializationViewSet)
router.register('consultations', viewsets.ConsultationViewSet)
router.register('medications', viewsets.MedicationViewSet)
router.register('consultation_medication', viewsets.ConsultationMedicationViewSet)

urlpatterns = router.urls