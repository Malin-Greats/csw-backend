from cgitb import lookup
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from rest_framework import mixins
from rest_framework import generics
from main.choices import MEMBER, MANAGER, STUDENT, ADMIN

from main.models import Admission, Patient,\
    Prescription, Referral, User, Ward, Member
from main.view_helpers import generate_clinician_stats,\
    generate_receptionist_stats
from .serializers import AdmissionNestedSerializer, AdmissionSerializer,\
    PatientSerializer, PrescriptionNestedSerializer,\
    PrescriptionSerializer, ReferralNestederializer,\
    ReferralSerializer, UserSerializer, WardSerializer, MemberSerializer, RegisterSerializer
from .permissions import IsAdmin, IsMember, IsManager, IsStudent
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
class MemberViewSet(viewsets.ModelViewSet):
    """List, create, retreive and destroy operations for a member"""
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.order_by('-created_at')
    serializer_class = MemberSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class PatientViewSet(viewsets.ModelViewSet):
    """List, create, retreive and destroy operations for a patient"""
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsMember]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user,
                        updated_at=timezone.now())

class RegisterMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """List, create, retreive and destroy operations for a new member"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """List, create, retreive and destroy operations for a user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



class ReceptionistPatientView(viewsets.ReadOnlyModelViewSet):
    """ Get patients registered by a particular receptionist """
    serializer_class = PatientSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Patient.objects.filter(created_by=user)


class ReferralViewSet(viewsets.ModelViewSet):
    """
    List, create, retreive and destroy
    operations for a patient referred to a clinician
    """
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]
    queryset = Referral.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user,
                        updated_at=timezone.now())


class ClinicianAssignedPatientsViewSet(viewsets.ReadOnlyModelViewSet):
    """Get patients assigned to a particular clinician"""
    serializer_class = ReferralSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return Referral.objects.filter(doctor=self.request.user)


class PrescriptionViewSet(viewsets.ModelViewSet):
    """
    List, create, retreive and destroy
    operations for a patient's prescription
    made by a clinician
    """
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsMember]
        else:
            permission_classes = [IsMember]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now(),
                        updated_by=self.request.user)


class AdmissionViewSet(viewsets.ModelViewSet):
    """
    List, create, retreive and destroy operations for an admitted patient to
    a particular ward
    """
    serializer_class = AdmissionSerializer
    queryset = Admission.objects.all()

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsMember]
        else:
            permission_classes = [IsMember]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now(),
                        updated_by=self.request.user)


class WardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List, create, retreive and destroy operations for a ward
    """
    serializer_class = WardSerializer
    queryset = Ward.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = None


class ReceptionistStatAPIView(APIView):
    """
    Fetch statistics for a particular receptionist
    e.g Number of patients registered today
    """
    permission_classes = []

    def get(self, request, format=None):
        stats = generate_receptionist_stats(request)
        return Response(stats)


class ClinicianStatAPIView(APIView):
    """
    Fetch statistics for a particular clinician
    e.g Number of patients admitted today
    """
    permission_classes = [IsMember]

    def get(self, request, format=None):
        stats = generate_clinician_stats(request)
        return Response(stats)


class ClinicianInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Fetch users who are only clinicians
    A clinician is either a Doctor, Nurse
    or Student Clinician
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return User.objects.filter(role__in=[MANAGER, MEMBER, STUDENT])


class PatientAdmissionInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Fetch admission data for a particular patient
    A patient id is required as query param
    Else fetch all admission data for all patients
    """
    permission_classes = [IsMember]
    serializer_class = AdmissionNestedSerializer
    pagination_class = None

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id')

        if not patient_id:
            return Admission.objects.all()

        return Admission.objects.filter(patient=patient_id)


class PatientPrescriptionInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Fetch prescription data for a particular patient
    A patient id is required as query param
    Else fetch all prescription data for all patients
    """
    serializer_class = PrescriptionNestedSerializer
    permission_classes = [IsMember]
    pagination_class = None

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id')

        if not patient_id:
            return Prescription.objects.all()

        return Prescription.objects.filter(patient=patient_id)


class PatientReferralInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View referral history of a patient or all patients
    Add patient_id as query param to get history for a patient
    """
    serializer_class = ReferralNestederializer
    permission_classes = [IsMember]
    pagination_class = None

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id')

        if not patient_id:
            return Referral.objects.all()

        return Referral.objects.filter(patient=patient_id)


class PatientsByName(generics.ListAPIView):
    """
    Fetch a patient's data using their name
    patient_name query param is required
    """
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        patient_name = self.request.query_params.get('patient_name')
        queryset = Patient.objects.filter(patient_name__iexact=patient_name)
        if not queryset or len(queryset) == 0:
            queryset = Patient.objects.filter(
                patient_name__icontains=patient_name)
        return queryset
