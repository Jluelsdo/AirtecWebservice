
from django.http import Http404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer, MaskeSerializer
from patients.models import Patient, Maske


class PatientsViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling patient data.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(APIView):
    """
    A view for retrieving, updating, and deleting a specific patient.

    Methods:
    - get_queryset: Returns the queryset of all patients.
    - get_object: Returns the patient object with the specified patient_id.
    - get: Retrieves the details of a specific patient.
    - put: Updates the details of a specific patient.
    - delete: Deletes a specific patient.
    """

    def get_queryset(self):
        """
        Returns the queryset of all patients.
        """
        return Patient.objects.all()

    def get_object(self, patient_id):
        """
        Returns the patient object with the specified patient_id.

        Args:
        - patient_id: The ID of the patient.

        Raises:
        - Http404: If the patient with the specified ID does not exist.
        """
        try:
            return Patient.objects.get(patient_id=patient_id)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, patient_id, format=None):
        """
        Retrieves the details of a specific patient.

        Args:
        - request: The HTTP request object.
        - patient_id: The ID of the patient to retrieve.
        - format: The format of the response data (default: None).

        Returns:
        - Response: The serialized data of the patient.
        """
        patient = self.get_object(patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, patient_id, format=None):
        """
        Updates the details of a specific patient.

        Args:
        - request: The HTTP request object.
        - patient_id: The ID of the patient to update.
        - format: The format of the request data (default: None).

        Returns:
        - Response: The serialized data of the updated patient if the request data is valid,
                    otherwise the errors in the serializer.
        """
        patient = self.get_object(patient_id)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, patient_id, format=None):
        """
        Deletes a specific patient.

        Args:
        - request: The HTTP request object.
        - patient_id: The ID of the patient to delete.
        - format: The format of the response data (default: None).

        Returns:
        - Response: The HTTP response with status code 204 (No Content).
        """
        patient = self.get_object(patient_id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaskeViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling mask data.
    """
    queryset = Maske.objects.all()
    serializer_class = MaskeSerializer

class MaskeDetailView(APIView):
    """
    A view for retrieving, updating, and deleting a specific mask.

    Methods:
    - get_queryset: Returns the queryset of all masks.
    - get_object: Returns the mask object with the specified id.
    - get: Retrieves the details of a specific mask.
    - put: Updates the details of a specific mask.
    - delete: Deletes a specific mask.
    """

    def get_queryset(self):
        """
        Returns the queryset of all masks.
        """
        return Maske.objects.all()

    def get_object(self, id):
        """
        Returns the mask object with the specified id.

        Args:
        - id: The ID of the mask.

        Raises:
        - Http404: If the mask with the specified ID does not exist.
        """
        try:
            return Maske.objects.get(id=id)
        except Maske.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """
        Retrieves the details of a specific mask.

        Args:
        - request: The HTTP request object.
        - id: The ID of the mask to retrieve.
        - format: The format of the response data (default: None).

        Returns:
        - Response: The serialized data of the mask.
        """
        mask = self.get_object(id)
        serializer = MaskeSerializer(mask)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        Updates the details of a specific mask.

        Args:
        - request: The HTTP request object.
        - id: The ID of the mask to update.
        - format: The format of the request data (default: None).

        Returns:
        - Response: The serialized data of the updated mask if the request data is valid,
                    otherwise the errors in the serializer.
        """
        mask = self.get_object(id)
        serializer = MaskeSerializer(mask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        """
        Deletes a specific mask.

        Args:
        - request: The HTTP request object.
        - id: The ID of the mask to delete.
        - format: The format of the response data (default: None).

        Returns:
        - Response: The HTTP response with status code 204 (No Content).
        """
        mask = self.get_object(id)
        mask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
