from main import db

class User(db.Document):
    fb_id = db.StringField(max_length=255, required=True)
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    twitter = db.URLField(verify_exists=True)
    fb_link = db.URLField(verify_exists=True)
    template_choice = db.IntField(min_value=0)
