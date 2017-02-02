from flask import Flask
from flask_restful import Api
from resources import PollResource, VoteResource, PollResultsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PollResource, '/polls', endpoint='polls')
api.add_resource(VoteResource, '/polls/<int:poll_id>/vote', endpoint='polls_vote')
api.add_resource(PollResultsResource, '/polls/<int:poll_id>/results', endpoint='polls_results')

if __name__ == '__main__':
    app.run(debug=True)
