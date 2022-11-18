from django.db import models
from common.models import CommonModel

# Create your models here.


class Room(CommonModel):

    class CountryChoices(models.TextChoices):
        DF = ("default", "나라 선택하기")
        KO = ("ko", "한국")
        USA = ("usa", "미국")
        JP = ("japan", "일본")

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private_Room")
        SHARED_ROOM = ("shared_room", "Shared_Room")

    name = models.CharField(
        max_length=150,
        default="",
    )

    country = models.CharField(
        max_length=100,
        default="default",
        choices=CountryChoices.choices
    )
    city = models.CharField(
        max_length=100,
        default="서울",
    )
    price = models.PositiveIntegerField(

    )
    rooms = models.PositiveIntegerField(

    )
    toilets = models.PositiveIntegerField(

    )
    description = models.TextField(

    )
    address = models.CharField(
        max_length=250
    )

    pet_friendly = models.BooleanField(
        default=True,
        help_text="반려동물 출입여부"
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    # 방 주인 계정 삭제 시 삭제.
    owner = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,

    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",


    )

    # def __str__(self):
    #     return self.name


# 편의 시설
class Amenity(CommonModel):

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        default="",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"