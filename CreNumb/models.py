from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    RoomID = models.CharField('Ký hiệu phòng', max_length=30)

    def __str__(self):
        return self.RoomID  # hiển thị tên từng loại tờ trình theo tên phòng

    class Meta:
        verbose_name_plural = 'Phòng ban'


class LoaiTT(models.Model):
    TTId = models.CharField('Ký hiệu TT', max_length=20)

    # TTName = models.CharField('Tên đầy đủ',max_length=50)
    def __str__(self):
        return self.TTId  # hiển thị tên từng loại tờ trình theo tên tờ trình

    class Meta:
        verbose_name_plural = 'Loại tờ trình'


class ToTrinh(models.Model):
    SoTT = models.CharField('Số tờ trình', max_length=50)
    TTId = models.ForeignKey(LoaiTT, on_delete=models.PROTECT, verbose_name='Loại tờ trình')
    TTtitle = models.CharField('Tên tờ trình', max_length=150)
    TTText = models.TextField('Nội dung tóm tắt', max_length=500, null=True, blank=True)
    Created_on = models.DateField('Ngày lấy số', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Người tạo')
    RoomId = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True, verbose_name='Phòng')

    def __str__(self):
        return self.TTtitle  # hiển thị tờ trình theo SoTT

    def __save__(self,*args,**kwargs):
        time = str(self.Created_on)[:-4]


    class Meta:
        verbose_name_plural = 'Tờ trình'
