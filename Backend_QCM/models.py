from db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    quizzes = relationship("Quiz", back_populates="creator")
    questions = relationship("Question", back_populates="creator")
    results = relationship("Result", back_populates="user")
    ranking = relationship("Ranking", back_populates="user", uselist=False)

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    description = Column(Text)
    parent_id = Column(Integer, ForeignKey("domains.id"), nullable=True)
    is_active = Column(Boolean, default=True)

    parent = relationship("Domain", remote_side=[id])
    quizzes = relationship("Quiz", back_populates="domain")
    questions = relationship("Question", back_populates="domain")

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    description = Column(Text)
    domain_id = Column(Integer, ForeignKey("domains.id"))
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    domain = relationship("Domain", back_populates="quizzes")
    creator = relationship("User", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete")
    results = relationship("Result", back_populates="quiz")

class QuestionType(enum.Enum):
    qcm = "QCM"
    texte = "TEXTE"
    vrai_faux = "VRAI_FAUX"
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    contenu = Column(Text, nullable=False)
    niveau = Column(String)
    type = Column(Enum(QuestionType))
    domain_id = Column(Integer, ForeignKey("domains.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    created_by = Column(Integer, ForeignKey("users.id"))

    domain = relationship("Domain", back_populates="questions")
    quiz = relationship("Quiz", back_populates="questions")
    creator = relationship("User", back_populates="questions")
    choices = relationship("Choice", back_populates="question", cascade="all, delete")

class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True)
    contenu = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

    question = relationship("Question", back_populates="choices")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)
    mistakes = Column(Integer)
    started_at = Column(DateTime(timezone=True))
    finished_at = Column(DateTime(timezone=True))

    user = relationship("User", back_populates="results")
    quiz = relationship("Quiz", back_populates="results")

class Ranking(Base):
    __tablename__ = "rankings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    score_total = Column(Integer, default=0)
    position = Column(Integer)

    user = relationship("User", back_populates="ranking")

