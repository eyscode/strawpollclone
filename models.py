import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Poll(Base):
    __tablename__ = 'polls'

    created_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String())
    options = sa.Column(sa.String())

    def __repr__(self):
        return '<Poll id={} options={}>'.format(self.id, self.options)


class Vote(Base):
    __tablename__ = 'votes'

    created_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    id = sa.Column(sa.Integer, primary_key=True)
    ip = sa.Column(sa.String(), index=True)
    option = sa.Column(sa.Integer())
    poll_id = sa.Column(sa.Integer, sa.ForeignKey('polls.id'))
    poll = relationship('Poll', backref=backref('votes', lazy='dynamic'))

    def __repr__(self):
        return '<Vote id={} option={} poll={}>'.format(self.id, self.option, self.poll_id)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
