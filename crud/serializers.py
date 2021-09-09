from rest_framework import serializers
from crud.models import Student

# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with r")

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = "__all__"

# Field level Validation in DRF
    # def validate_name(self, value):
    #     if value == "Rohit":
    #         raise serializers.ValidationError("Name should not be Rohit")
    #     return value
    

# Object level Validation      
    # def validate(self, data):
    #     nm = data.get('name')
    #     sec = data.get('section')
    #     print(nm)
    #     print(sec)
    #     if nm.lower() == 'rahul' and sec.lower() != 'B':
    #         raise serializers.ValidationError("for rohit section should be B")
    #     return data