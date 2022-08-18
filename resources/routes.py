from resources.auth import RegisterResource, LoginResource
from resources.book import ReadingBooksResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (ReadingBooksResource, "/create_reading_book/"),
)
