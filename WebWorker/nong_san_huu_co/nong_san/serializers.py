from rest_framework import serializers
from .models import *


class thuocSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_thuoc
        fields = '__all__'


class congviecSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_congviec
        fields = '__all__'


class taikhoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_taikhoan
        fields = '__all__'


class congnhan_congviecSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_congnhan_congviec
        fields = '__all__'


class noilamviecSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_noilamviec
        fields = '__all__'


class giongSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_giong
        fields = '__all__'


class phanbonSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_phanbon
        fields = '__all__'


class nhacungcapSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_nhacungcap
        fields = '__all__'


class danhmucgiongSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_danhmucgiong
        fields = '__all__'


class baocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_baocao
        fields = '__all__'
