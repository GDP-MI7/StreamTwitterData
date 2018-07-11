from mongoengine import *
import datetime

#connecting to database
connect('twitter', host='mongodb://localhost:27017')
#host='localhost', port=27017)

#defining documents
class Hashtagdata(Document):
    user_screen_name = StringField(required=True)
    created_at = datetime(required=True)
    text = StringField(required=True)
    hashtag = StringField(required=True)