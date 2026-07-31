from secrets import randbelow

from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from .email_service import EmailService

from .models import EmailOTP


class OTPService:
    OTP_LENGTH = 6
    OTP_EXPIRY_MINUTES = 10

    @classmethod
    def generate_otp(cls) -> str:
        return f"{randbelow(1000000):06d}"

    @classmethod
    def create_otp(cls, email: str, purpose: str) -> str:
        otp = cls.generate_otp()

        EmailOTP.objects.filter(
            email=email,
            purpose=purpose,
            is_used=False,
        ).delete()

        EmailOTP.objects.create(
            email=email,
            otp_hash=make_password(otp),
            purpose=purpose,
            expires_at=(
            timezone.now()
            + timezone.timedelta(
            minutes=cls.OTP_EXPIRY_MINUTES,
            )
            ),
        )

        EmailService.send_otp_email(
            to_email=email,
            otp=otp,
        )

        return otp

    @staticmethod
    def verify_otp(otp_object: EmailOTP, otp: str) -> bool:
        return check_password(
            otp,
            otp_object.otp_hash,
        )