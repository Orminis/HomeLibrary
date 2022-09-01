from resources.auth import DeleteUserResource, RegisterUserResource, LoginUserResource, CreateCheckerResource

from resources.books import AudioBooksResource, DigitalBooksResource, BooksResource, \
    RejectReadingBookResource, ApproveReadingBookResource, ReadingBooksResource, DeleteReadingBooksResource

from resources.users import AddReadingBookToCollectionResource, RemoveReadingBookFromCollectionResource, \
    PersonalUserResource, UserReadingBooksResource, UpdateUserResource

routes = (
    (PersonalUserResource, "/<int:user_id>/"),
    (RegisterUserResource, "/register_user/"),
    (LoginUserResource, "/login_user/"),
    (UpdateUserResource, "/<int:user_id>/update_user/"),
    (DeleteUserResource, "/<int:user_id>/delete_user/"),
    (UserReadingBooksResource, "/<int:user_id>/reading_book/"),

    (CreateCheckerResource, "/register_checker/"),
    (CreateAdminResource, "/register_checker/"),

    (BooksResource, "/books/"),

    (ReadingBooksResource, "/reading_book/"),
    (ApproveReadingBookResource, "/reading_book/<int:id>/approve/"),
    (RejectReadingBookResource, "/reading_book/<int:id>/reject/"),
    (DeleteReadingBooksResource, "/<int:book_id>/delete/"),
    (AddReadingBookToCollectionResource, "/reading_book/<int:book_id>/add/"),
    (RemoveReadingBookFromCollectionResource, "/reading_book/<int:book_id>/remove/"),

    (DigitalBooksResource, "/digital_books/"),
    (AudioBooksResource, "/audio_books/"),
)
