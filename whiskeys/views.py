from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import WhiskeySerializer, UserNumbersSerializer
from .models import Whiskey, UserNumbers

class NumbersView(APIView):
    def get(self, request):
        user_numbers = UserNumbers.objects.get(id=1)
        numbers_seriazlier = UserNumbersSerializer(user_numbers)

        return Response(numbers_seriazlier.data)

class RessultView(APIView):
    def post(self, request):
        data = request.data
        result = data['result']
        print()
        # 조니워커 레드라벨
        if result == 'NNNSNN' or result == 'NNNBNN':
            whiskey = Whiskey.objects.get(id=1)
        # 조니워커 더블블랙라벨
        elif result == 'NNYBYY' or result == 'NNYTYY' or result == 'NNYSYY' or result == 'NNYBNY' or result == 'NNYTNY' or result == 'NNYSNY' or result == 'NNYBYN' or result == 'NNYTYN' or result == 'NNYSYN' or result == 'NNYBNN' or result == 'NNYTNN' or result == 'NNYSNN':
            whiskey = Whiskey.objects.get(id=2)
        # 조니워커 그린라벨
        elif result == 'YYYSYY' or result == 'YNYTYY' or result == 'YNYTYN':
            whiskey = Whiskey.objects.get(id=3)
        # 조니워커 골드라벨 리저브
        elif result == 'YNYBYY':
            whiskey = Whiskey.objects.get(id=4)
        # 조니워커 플래티넘 라벨
        elif result == 'YYYFYY' or result == 'YYYFYN' or result == 'YNYFYN':
            whiskey = Whiskey.objects.get(id=5)
        # 발렌타인 파이니스트
        elif result == 'NNNBYN' or result == 'NNNSYN':
            whiskey = Whiskey.objects.get(id=6)
        # 발렌타인 12년
        elif result == 'NYNBYY':
            whiskey = Whiskey.objects.get(id=7)
        # 발렌타인 17년
        elif result == 'YYYBYY' or result == 'YYYSYN':
            whiskey = Whiskey.objects.get(id=8)
        # 제임스 스탠다드
        elif result == 'YYNBNY' or result == 'NYNFNY':
            whiskey = Whiskey.objects.get(id=9)
        # 시바스 리갈 12년산
        elif result == 'YYYBYN' or result == 'YYNFYY' or result == 'YYNFYN':
            whiskey = Whiskey.objects.get(id=10)
        # 시바스 리갈 18년산
        elif result == 'YYYFNY' or result == 'YYYSNY':
            whiskey = Whiskey.objects.get(id=11)
        # 조니워커 블랙라벨
        else:
            whiskey = Whiskey.objects.get(id=12)

        print(whiskey)

        whiskey_serializer = WhiskeySerializer(whiskey, context={'request': request})

        user_numbers = UserNumbers.objects.get(id=1)
        user_numbers.number += 1
        user_numbers.save()

        return Response(whiskey_serializer.data)
    
