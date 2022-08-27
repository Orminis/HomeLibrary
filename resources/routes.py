from resources import Main
from resources.auth import RegisterResource, LoginResource, UpdateUserResource
from resources.books import ReadingBooksResource, AudioBooksResource, DigitalBooksResource
# UpdateStatusReadingBooksResource

routes = (
    (Main, "/"),
    (RegisterResource, "/register_user/"),
    (LoginResource, "/login_user/"),
    (UpdateUserResource, "/update_user/<int:user_id>/"),
    (ReadingBooksResource, "/create_reading_book/"),
    (DigitalBooksResource, "/create_digital_book/"),
    (AudioBooksResource, "/create_audio_book/"),
    # (UpdateStatusReadingBooksResource, "/update_status_reading_book/"),
)
