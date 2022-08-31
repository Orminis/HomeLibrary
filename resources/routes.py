from resources.auth import UpdateUserResource, PersonalUserResource, \
    DeleteUserResource, RegisterUserResource, LoginUserResource, AddReadingBookToCollectionResource, \
    RemoveReadingBookFromCollectionResource
from resources.books import ReadingBooksResource, AudioBooksResource, DigitalBooksResource, BooksResource, \
    RejectReadingBookResource, ApproveReadingBookResource

# UpdateStatusReadingBooksResource

routes = (
    (PersonalUserResource, "/<int:user_id>/"),
    (RegisterUserResource, "/register_user/"),
    (LoginUserResource, "/login_user/"),
    (UpdateUserResource, "/<int:user_id>/update_user/"),
    (DeleteUserResource, "/<int:user_id>/delete_user/"),

    (BooksResource, "/books/"),
    (ReadingBooksResource, "/reading_book/"),
    (DigitalBooksResource, "/digital_book/"),
    (AudioBooksResource, "/audio_book/"),

    (ApproveReadingBookResource, "/reading_book/<int:id>/approve/"),
    (RejectReadingBookResource, "/reading_book/<int:id>/reject/"),
    (AddReadingBookToCollectionResource, "/reading_book/<int:id>/add/"),
    (RemoveReadingBookFromCollectionResource, "/reading_book/<int:id>/remove/")
    # (UpdateStatusReadingBooksResource, "/update_status_reading_book/"),
)
