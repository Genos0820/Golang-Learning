from rest_framework import serializers # type: ignore
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes User profile Object"""
    class Meta:
         model=models.UserProfile
         fields = ('id','email','name','password')
         extra_kwargs={
             'password':{
                 'write_only': True,
                 'style': {'input_type': 'password', 'placeholder':'Password'}
             }
         }
         
    def create(self,validated_data):
        """Create and return a new user"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)

'''
class UserProfileSerializer(serializers.Serializer):
    """Serializes a name, email and password field for  our ProfileAPI"""
    email = serializers.EmailField()
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
'''

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serailizes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={
            'user_profile':{'read_only':True}
        }
        

