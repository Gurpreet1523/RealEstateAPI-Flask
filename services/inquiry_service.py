from _datetime import datetime, timezone

from repository.inquiry_repository import InquiryRepository
from models.models import db, Inquiry


class InquiryService:

    @staticmethod
    def create_inquiry(user_id, property_id, message, inquiry_date):
        new_inquiry = Inquiry(user_id=user_id, property_id=property_id, message=message,
                              inquiry_date=datetime.now(timezone.utc))
        InquiryRepository.create_inquiry(new_inquiry)
        return new_inquiry

    @staticmethod
    def get_all_inquiries():
        return InquiryRepository.get_all_inquiries()

    @staticmethod
    def get_inquiry_by_id(inquiry_id):
        return InquiryRepository.get_inquiry_by_id(inquiry_id)

    @staticmethod
    def update_inquiry(inquiry_id, message):
        inquiry = InquiryRepository.get_inquiry_by_id(inquiry_id)
        if inquiry:
            inquiry.message = message
            InquiryRepository.update_inquiry(inquiry_id, message)
        return inquiry

    @staticmethod
    def delete_inquiry(inquiry_id):
        inquiry = InquiryRepository.get_inquiry_by_id(inquiry_id)
        if inquiry:
            InquiryRepository.delete_inquiry(inquiry_id)
        return inquiry
