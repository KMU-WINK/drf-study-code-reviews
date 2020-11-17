from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, password, extra_fields):
        kwargs = extra_fields.copy()
        kwargs['grade'] = int(kwargs['grade'][0])
        user = self.model(
            **kwargs
        )
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name, phone, date_of_birth):
        user = self.model(
            email=email, password=password, name=name, phone=phone, date_of_birth=date_of_birth

        )

        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.grade = 100
        user.set_password(password)
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(null=False, unique=True, verbose_name="이메일")
    phone = PhoneNumberField(null=False, unique=True, verbose_name="휴대폰 번호")
    name = models.CharField(max_length=7, null=False, verbose_name="이름")
    nickname = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="닉네임")
    password = models.CharField(max_length=256, null=False, verbose_name="패스워드")
    date_of_birth = models.DateField(null=False, verbose_name="생년월일")
    profile_thumbnail = models.ImageField(null=True, blank=True, upload_to="static/images/profile_img/", verbose_name="프로필 사진")
    is_active = models.BooleanField(verbose_name="활성화 여부", default=False)
    is_admin = models.BooleanField(verbose_name="관리자 계정 여부", default=False)
    is_staff = models.BooleanField(verbose_name="스태프 여부", default=False)
    is_superuser = models.BooleanField(verbose_name="최고 관리자 여부", default=False)
    grade = models.IntegerField(null=False, default=1, verbose_name="회원 등급")

    is_email_vaild = models.DateTimeField(null=True, blank=True, verbose_name="이메일 인증 시간")
    is_phone_vaild = models.DateTimeField(null=True, blank=True, verbose_name="휴대폰 인증 시간")
    address = models.CharField(max_length=256, null=True, blank=True, verbose_name="상세 주소")
    zipcode = models.CharField(max_length=5, null=True, blank=True, verbose_name="우편 번호")

    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name="휴대폰 인증 시간")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['name', 'phone', 'date_of_birth']
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "회원 정보"