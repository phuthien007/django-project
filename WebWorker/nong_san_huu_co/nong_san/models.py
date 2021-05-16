from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here


class tb_danhmucgiong(models.Model):

    ten = models.CharField(max_length=255)

    class Meta:
        db_table = 'danhmucgiong'

    def __str__(self):
        return "danh muc giong: " + self.ten


class tb_nhacungcap(models.Model):
    ten = models.CharField(max_length=255)
    diachi = models.CharField(max_length=255, null=True)
    sdt = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'nhacungcap'
    def __str__(self):
        return "ten nha cung cap: " + self.ten


class tb_thuoc(models.Model):
    ten = models.CharField(max_length=255)
    soluong = models.CharField(max_length=255)
    gia = models.CharField(max_length=255)
    nhacungcap = models.ForeignKey(tb_nhacungcap, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'thuoc'
    def __str__(self):
        return "ten: " + self.ten + ' soluong: ' +self.soluong


class tb_phanbon(models.Model):
    ten = models.CharField(max_length=255)
    soluong = models.CharField(max_length=255)
    hinh = models.ImageField(upload_to='images/phanbon')
    nhacungcap = models.ForeignKey(tb_nhacungcap, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'phanbon'
    def __str__(self):
        return "ten: " + self.ten


class tb_noilamviec(models.Model):
    ten = models.CharField(max_length=255)
    trangthai = models.CharField(max_length=255)
    hinh = models.ImageField(upload_to='images/noilamviec')
    class Meta:
        db_table = 'noilamviec'
    def __str__(self):
        return "ten: " + self.ten


class tb_giong(models.Model):
    ten = models.CharField(max_length=255)
    gia = models.CharField(max_length=255)
    thoigiansinhtruong = models.CharField(max_length=255)
    hinh = models.ImageField(upload_to='images/giong')
    hinhthai = models.CharField(max_length=255)
    soluong = models.CharField(max_length=255)
    danhmucgiong = models.ForeignKey(tb_danhmucgiong, on_delete=models.CASCADE)
    nhacungcap = models.ForeignKey(tb_nhacungcap, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'giong'
    def __str__(self):
        return "ten: " + self.ten


class tb_taikhoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hoten = models.CharField(max_length=255)
    diachi = models.CharField(max_length=255)
    sdt = models.CharField(max_length=255)
    class Meta:
        db_table = 'taikhoan'
    def __str__(self):
        return "ten dang nhap: " + self.user.username


class tb_congviec(models.Model):
    ten = models.CharField(max_length=255)
    trangthai = models.CharField(max_length=255)
    thoigian = models.DateField(null=True)
    giong = models.ForeignKey(tb_giong, on_delete=models.DO_NOTHING)
    phanbon = models.ForeignKey(tb_phanbon, on_delete=models.DO_NOTHING)
    thuoc = models.ForeignKey(tb_thuoc, on_delete=models.DO_NOTHING)
    noilamviec = models.ForeignKey(tb_noilamviec, on_delete=models.CASCADE)
    class Meta:
        db_table = 'congviec'
    def __str__(self):
        return "ten: "+ self.ten + " id: " + str(self.id)


class tb_congnhan_congviec(models.Model):
    congnhan = models.ForeignKey(tb_taikhoan, on_delete=models.CASCADE)
    congviec = models.ForeignKey(tb_congviec, on_delete=models.CASCADE)
    class Meta:
        db_table = 'congnhan_congviec'
    def __str__(self):
        return "ten cong nhan: " + self.congnhan.user.username + +" ten cong viec: "+self.congviec.ten


class tb_baocao(models.Model):
    trangthai = models.CharField(max_length=255)
    mota = models.CharField(max_length=255)
    hinh = models.ImageField(upload_to='images/baocao')
    congnhan_congviec = models.ForeignKey(tb_congnhan_congviec, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'baocao'
    def __str__(self):
        return "id bao cao: " + str(self.id)


@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created= False, **kwargs):
    if created:
        Token.objects.create(user = instance)