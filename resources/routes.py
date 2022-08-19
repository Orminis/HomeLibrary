from resources.auth import RegisterResource, LoginResource
from resources.book import ReadingBooksResource, AudioBooksResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (ReadingBooksResource, "/create_reading_book/"),
    (AudioBooksResource, "/create_audio_book/"),
)
