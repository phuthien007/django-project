import json

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from .serializers import *
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
#

@api_view(['PUT'])
def change_password(request):
    if request.method == 'PUT':
        try:
            o_p = request.POST['old_password']
            n_p = request.POST['new_password']
            user = User.objects.filter(username=request.user.username).first()
            user.set_password(n_p)
            user.save()
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print("asd", e)
            return Response(data={"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"message": "method not allow"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            tendangnhap = request.POST['username']
            matkhau = request.POST['password']
            email = request.POST['email']
            hoten = request.POST['hoten']
            diachi = request.POST['diachi']
            sdt = request.POST['sdt']
            user = User.objects.create_user(username=tendangnhap, password=matkhau, email=email)

            token = Token.objects.get(user=user).key
            # print(token)
            tk = tb_taikhoan(user=user, hoten=hoten, diachi=diachi, sdt=sdt)
            tk.save()

            data = {
                "token": token,
                "user_id": user.id,
                "username": tendangnhap,
                "hoten": hoten,
                "diachi": diachi,
                "sdt": sdt
            }
            # print(JSONParser().parse(request))
            # return HttpResponse(tk.id)
            return JsonResponse(data)
        except:
            return JsonResponse({"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "method not allow"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ds_cong_viec(request):
    try:
        congnhan = tb_taikhoan.objects.filter(user=request.user).first()

        cv = tb_congnhan_congviec.objects.filter(congnhan=congnhan)
        # print("cv ", len(cv))
        # print(cv)
        # print(request.user)
        # print(congnhan)
    except Exception as e:
        print(e)
        return Response(data={"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        congviec = []
        try:

            for c in cv:
                # print(1)
                v = tb_congviec.objects.filter(id=c.congviec.id).first()
                bc = tb_baocao.objects.filter(congnhan_congviec=c).all()
                baocao = []
                # if bc:
                #     for b in bc:
                #         baocao.append({
                #             "trangthai": b.trangthai,
                #             "mota": b.mota,
                #             "hinhanh": b.hinh.url
                #         })
                # print("v ", v)
                congviec.append({
                    "id_congviec": v.id,
                    "tencongviec": v.ten,
                    "noilamviec": v.noilamviec.ten,
                    "tengiong": v.giong.ten,
                    "tenphanbon": v.phanbon.ten,
                    "tenthuoc": v.thuoc.ten,
                    "soluongthuoc": v.thuoc.soluong,
                    "thoigian": v.thoigian,
                    # "baocao": baocao
                })
                # print(len(congviec))
            return Response(data=congviec, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data={"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"message": "method not allow"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def gui_bao_cao(request):
    if request.method != "POST":
        return Response(data={"message": "method not allow"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        trangthai = request.POST['trangthai']
        mota = request.POST['mota']
        filename = request.POST['file_name']
        hinhanh = request.POST['hinhanh']
        cv = tb_congviec.objects.get(id=request.POST['id_congviec'])
        congnhan = tb_taikhoan.objects.filter(user=request.user).first()
        # print("asd",cv)
        import base64, os
        # print(filename)
        # hinhanh = base64.b64encode(bytes('hinhanh', 'utf-8'))
        # print(hinhanh)
        # print()
        # print(type(hinhanh))
        ima = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/images/baocao/' + filename, 'wb')

        ima.write(base64.b64decode(hinhanh))
        cn_cv = tb_congnhan_congviec.objects.filter(congnhan=congnhan, congviec=cv).first()
        # print(cn_cv)
        bc = tb_baocao(trangthai=trangthai, mota=mota, congnhan_congviec=cn_cv)
        bc.save()
        return Response(data={"message": "success"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        # print(e)
        return Response(data={"message": "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
