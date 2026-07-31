import requests

from django.conf import settings
from django.template.loader import render_to_string


class EmailService:
    BASE_URL = "https://api.resend.com/emails"

    @classmethod
    def send_email(
        cls,
        to_email: str,
        subject: str,
        html: str,
    ) -> bool:

        response = requests.post(
            cls.BASE_URL,
            headers={
                "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "from": settings.DEFAULT_FROM_EMAIL,
                "to": [to_email],
                "subject": subject,
                "html": html,
            },
            timeout=10,
        )
        print("Status:", response.status_code)
        print("Response:", response.text)

        return response.status_code in (200, 201)

    @classmethod
    def send_otp_email(
        cls,
        to_email: str,
        otp: str,
    ) -> bool:

        html = render_to_string(
            "emails/otp.html",
            {
                "otp": otp,
            },
        )

        return cls.send_email(
            to_email=to_email,
            subject="Verify your DevForge account",
            html=html,
        )