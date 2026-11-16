from django.shortcuts import render,get_object_or_404

from leads.models import Lead
from leads.serializers import LeadSerializer

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class LeadCreateListView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):

        form_data=request.data

        serializer_instance=LeadSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(created_by=request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


    def get(self,request):
        
        qs=Lead.objects.filter(created_by=request.user)

        serializer_instance=LeadSerializer(qs,many=True)

        return Response(serializer_instance.data)


class LeadRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):

        qs=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,qs)

        serializer_instance=LeadSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data=request.data

        lead_object=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,lead_object)

        serializer_instance=LeadSerializer(data=form_data,instance=lead_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


    def delete(self,request,pk=None):

        lead_object=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,lead_object)

        lead_object.delete()

        response_data={"message":"deleted..."}

        return Response(data=response_data)


    def patch(self, request, pk=None):

        form_data = request.data

        lead_object = get_object_or_404(Lead, id=pk, created_by=request.user)

        self.check_object_permissions(request,lead_object)

        serializer_instance = LeadSerializer(data=form_data,instance=lead_object,partial=True)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

