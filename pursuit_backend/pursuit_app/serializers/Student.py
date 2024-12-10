from dataclasses import field
from rest_framework import serializers
from pursuit_app.models import Student
from . Interview import InterviewDashboardSerializer
class StudentSerializer(serializers.ModelSerializer) :
 
    class Meta :
        model = Student
        fields = '__all__'

class StudentInterviewDashboardSerializer(serializers.ModelSerializer) :
    interviews = InterviewDashboardSerializer(many=True)
    class Meta : 
        model = Student
        fields=['enrollment_no','student_name','mobile_number','email','interviews','selection_status']

