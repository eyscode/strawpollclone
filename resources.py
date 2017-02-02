from flask_restful import Resource, reqparse, fields, marshal_with
from models import Poll, Vote
from db import session

poll_parser = reqparse.RequestParser(bundle_errors=True)
poll_parser.add_argument('name', str, required=True, location=['json', 'form'])
poll_parser.add_argument('options', lambda t: t.split(','), required=True, location=['json', 'form'])

vote_parser = reqparse.RequestParser(bundle_errors=True)
vote_parser.add_argument('option', str, required=True, location=['json', 'form'])
vote_parser.add_argument('ip', lambda t: t.split(','), required=True, location=['json', 'form'])

poll_fields = {
    'id': fields.Integer
}

vote_fields = {
    'ip': fields.String,
    'option': fields.Integer
}


class PollResource(Resource):
    @marshal_with(poll_fields)
    def post(self):
        parsed_args = poll_parser.parse_args()
        poll = Poll(name=parsed_args['name'], options=parsed_args['options'])
        session.add(poll)
        session.commit()
        return poll, 201


class VoteResource(Resource):
    @marshal_with(poll_fields)
    def post(self, poll_id):
        parsed_args = vote_parser.parse_args()
        vote = Vote(option=parsed_args['option'], ip=parsed_args['ip'], poll_id=poll_id)
        session.add(vote)
        session.commit()
        return vote, 201


class PollResultsResource(Resource):
    def get(self, poll_id):
        poll = session.execute('SELECT options FROM polls WHERE id = :id', {'id': poll_id}).fetchone()
        if not poll:
            return 404, 404
        response = []
        for index, option in enumerate(poll[0].split(",")):
            votes = session.execute(
                'SELECT count(*), count(DISTINCT ip) FROM votes WHERE poll_id = :poll_id AND option=:option',
                {'poll_id': poll_id, 'option': index}).fetchone()
            response.append({
                'name': option,
                'votes': votes[0] if votes else 0,
                'unique_votes': votes[1] if votes else 0
            })
        return response, 201
