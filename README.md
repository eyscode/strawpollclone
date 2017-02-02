# Strawpoll alike project

Implementation of a polling Rest API similar to http://www.strawpoll.me .
The user can create a poll with a number of options, and vote on polls.

## Getting Started

Install Python 3.6.0 version

```
brew install pyenv
pyenv install 3.6.0
```

Create a virtual environment, activate it, and install Python dependencies

```
pyenv virtualenv 3.6.0 strawpollclone
pyenv active strawpollclone
pip install -r requirements.txt
```

Create the database schema

```
python models.py
```

Launch the application

```
python app.py
```

## API specification


#### POST /polls

Create a new poll. Returns a JSON object with one key `id`, the ID of the new poll. POST arguments are:

- name: name of poll to create
- options: comma separated list of poll options


##### POST /polls/:id/vote

Vote on a poll. POST arguments are:

- option: Zero-based index of option to vote on
- ip: IP address of voter. Use this argument instead of actual remote IP to make testing easier


#### GET /polls/:id/results

Get poll results. Returns a JSON list of objects, each with the keys:

- name: Name of the option
- votes: Raw number of votes on the option
- unique_votes: Unique number of IP addresses that voted on the option