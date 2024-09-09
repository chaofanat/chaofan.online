from typing import List, Optional
from ninja import Schema
from datetime import datetime

# FlashcardSet Schemas
class FlashcardSetIn(Schema):
    title: str
    description: Optional[str] = None

class FlashcardSetOut(FlashcardSetIn):
    id: int
    user_id: int



# Flashcard Schemas
class FlashcardIn(Schema):
    front_content: str
    back_content: str
    cardset_id: int

class FlashcardOut(FlashcardIn):
    id: int
    knowledge_level: int


# Progress Schemas
class ProgressIn(Schema):
    user_id: int
    flashcard_set_id: int
    last_reviewed: Optional[datetime] = None
    next_review: Optional[datetime] = None
    correct_answers: int = 0
    incorrect_answers: int = 0
    

class ProgressOut(ProgressIn):
    id: int
    