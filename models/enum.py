from enum import Enum


class UserRoles(Enum):
    user = "Standard User"
    checker = "Checker"
    admin = "Admin"


class Covers(Enum):
    soft = "Soft Cover"
    hard = "Hard Cover"


class Status(Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


"""
As New:  The book is in the same immaculate condition as when it was published. 
 This could be the description for a book that has been lost in a warehouse for years,
 never shelved, thumbed or even opened yet may still be some years old.

Fine (F or FN): A Fine book approaches the condition of As New, but without being crisp.  
 The book may have been opened and read, but there are no defects to the book, jacket or pages. 

Very Good (VG): Describes a book that shows some small signs of wear - but no tears - on either binding or paper.
 Any defects should be noted by the seller.

Good (G): Describes the average used worn book that has all pages or leaves present. 
 Any defects should be noted by the seller.

Fair: Worn book that has complete text pages (including those with maps or plates) 
but may lack endpapers, half-title, etc. (which must be noted).
 Binding, jacket (if any), etc., may also be worn. All defects should be noted.

Poor: Describes a book that is sufficiently worn.  Any missing maps or plates should still be noted.
 This copy may be soiled, scuffed, stained or spotted and may have loose joints, hinges, pages, etc.
"""


class Condition(Enum):
    mint = "Mint"
    fine = "Fine"
    very_good = "Very Good"
    good = "Good"
    fair = "Fair"
    poor = "Poor"
