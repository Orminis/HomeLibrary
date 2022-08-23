from resources.auth import RegisterResource, LoginResource, UpdateUserResource
from resources.books import ReadingBooksResource, AudioBooksResource, DigitalBooksResource, AcceptBooksResource

routes = (
    (RegisterResource, "/register_user/"),
    (LoginResource, "/login_user/"),
    (UpdateUserResource, "/update_user/"),
    (ReadingBooksResource, "/create_reading_book/"),
    (DigitalBooksResource, "/create_digital_book/"),
    (AudioBooksResource, "/create_audio_book/"),
    (AcceptBooksResource, "/accept_book/"),
)
