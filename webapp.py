from bottle import route, run, template, view, static_file
from mongoengine import *
import os

root = os.path.dirname(__file__)
static_root = os.path.join(root, "static")

connect ('greeter')

class Name(Document):
	name=StringField(default="World")

@route('/')
@view('index')
def slogan():
	slogan = random.choice(Slogan.objects()).slogan
	noun = random.choice(Noun.objects()).noun
	return {'slogan': slogan + ' ' + noun + '.'}


@route('/noun/<noun>')
def saveNoun(noun):
	# todo: not everyone should be able to set.
	dbnoun = Noun.objects(noun=noun).first() or Noun()
	dbnoun.noun = noun
	dbnoun.save()
	return template("Saved {{noun}}", {'noun':noun})

@route('/slogan/<slogan>')
def saveSlogan(slogan):
	# todo: not everyone should be able to set.
	dbslogan = Slogan.objects(slogan=slogan).first() or Slogan()
	dbslogan.slogan = slogan
	dbslogan.save()
	return template("Saved {{slogan}}", {'slogan':slogan})

@route('/static/<path:path>')
def static(path):
	return static_file(path, root=static_root)

if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')