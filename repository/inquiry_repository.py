from models.models import db, Inquiry


class InquiryRepository:

    @staticmethod
    def create_inquiry(new_inquiry):
        db.session.add(new_inquiry)
        db.session.commit()

    @staticmethod
    def get_all_inquiries():
        return Inquiry.query.all()

    @staticmethod
    def get_inquiry_by_id(inquiry_id):
        return Inquiry.query.filter_by(inquiry_id=inquiry_id).first()

    @staticmethod
    def update_inquiry(inquiry_id, data):
        inquiry = Inquiry.query.filter_by(inquiry_id=inquiry_id).first()
        if inquiry:
            db.session.commit()
        return inquiry

    @staticmethod
    def delete_inquiry(inquiry_id):
        inquiry = Inquiry.query.get(inquiry_id)
        if inquiry:
            db.session.delete(inquiry)
            db.session.commit()
            return True
        return False
