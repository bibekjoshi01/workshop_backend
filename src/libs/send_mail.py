# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.conf import settings
# import logging

# # logger setup for email logs
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.ERROR)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# file_handler = logging.FileHandler("logs/email_logs.log")
# file_handler.setLevel(logging.ERROR)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


# def _send_email(template_name, context, recipient_email):
#     email_template = render_to_string(
#         f"{template_name}.html",
#         context={
#             "context": context,
#         },
#     )
#     email = EmailMultiAlternatives(
#         subject="Account Information",
#         body="Account Information",
#         from_email=settings.EMAIL_HOST_USER,
#         to=[recipient_email],
#     )

#     email.attach_alternative(email_template, "text/html")

#     try:
#         email.send()
#         return True
#     except Exception as e:
#         logger.error(f"Failed to send email to {recipient_email}: {str(e)}")
#         return False


# def _send_order_email(template_name, context, recipient_email, subject):
#     email_template = render_to_string(
#         f"{template_name}.html",
#         context={
#             "context": context,
#         },
#     )
#     email = EmailMultiAlternatives(
#         subject=subject,
#         body="Order Updates",
#         from_email=settings.EMAIL_HOST_USER,
#         to=[recipient_email],
#     )
#     email.attach_alternative(email_template, "text/html")
#     try:
#         email.send()
#         return True
#     except Exception as e:
#         logger.error(
#             f"Failed to send order updates email to {recipient_email}: {str(e)}"
#         )
#         return False
