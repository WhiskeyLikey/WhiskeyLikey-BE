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
        
        # 조니워커 레드라벨
        if result == 'NNNBSNN':
            whiskey = Whiskey.objects.get(id=1)
        # 조니워커 더블블랙라벨
        elif result == 'NNYBSYY' or 'NNYBTYY' or 'NNYSTYY' or 'NNYBSNY' or 'NNYBTNY' or 'NNYSTNY' or 'NNYBSYN' or 'NNYBTYN' or 'NNYSTYN' or 'NNYBSNN' or 'NNYBTNN' or 'NNYSTNN':
            whiskey = Whiskey.objects.get(id=2)
        # 조니워커 그린라벨
        elif result == 'YYYFTYY' or 'YYYSTYY' or 'YYYFTYN' or 'YYYSTYN' or 'YNYFTYY' or 'YNYSTYY' or 'YNYFTYN' or 'YNYSTYN':
            whiskey = Whiskey.objects.get(id=3)
        # 조니워커 골드라벨 리저브
        elif result == 'YNYBFYY' or 'YNYBSYY' or 'YNYFSYY':
            whiskey = Whiskey.objects.get(id=4)
        # 조니워커 플래티넘 라벨
        elif result == 'YYYFSYY' or 'YYYFSYN' or 'YNYFSYN':
            whiskey = Whiskey.objects.get(id=5)
        # 발렌타인 파이니스트
        elif result == 'NNNBSYN' or 'NNNBTYN' or 'NNNSTYN':
            whiskey = Whiskey.objects.get(id=6)
        # 발렌타인 12년
        elif result == 'NYNBYY':
            whiskey = Whiskey.objects.get(id=7)
        # 발렌타인 17년
        elif result == 'YYYBSYY' or 'YYYBSYN':
            whiskey = Whiskey.objects.get(id=8)
        # 제임스 스탠다드
        elif result == 'YYNBFNY' or 'NYNBFNY':
            whiskey = Whiskey.objects.get(id=9)
        # 시바스 리갈 12년산
        elif result == 'YYYBFYY' or 'YYYBFYN' or 'YYNBFYY' or 'YYNBFYN':
            whiskey = Whiskey.objects.get(id=10)
        # 시바스 리갈 18년산
        elif result == 'YYYFSNY':
            whiskey = Whiskey.objects.get(id=11)
        # 조니워커 블랙라벨
        else:
            whiskey = Whiskey.objects.get(id=12)

        whiskey_serializer = WhiskeySerializer(whiskey, context={'request': request})

        user_numbers = UserNumbers.objects.get(id=1)
        user_numbers.number += 1
        user_numbers.save()

        return Response(whiskey_serializer.data)
    
