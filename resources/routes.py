from resources.auth import RegisterResource, LoginResource
from resources.books import ReadingBooksResource, AudioBooksResource, DigitalBooksResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (ReadingBooksResource, "/create_reading_book/"),
    (DigitalBooksResource, "/create_digital_book/"),
    (AudioBooksResource, "/create_audio_book/"),
)
