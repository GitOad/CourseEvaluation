from flask import Flask, jsonify, abort, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)

courses = [
	{
		'id': 1,
       	'title': u'Software Architecture',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
	},
	{
		'id': 2,
        'title': u'Software Management',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
	}
]

# # GET all courses
# @app.route('/ce/api/v1.0/courses', methods=['GET'])
# def get_courses():
# 	return jsonify({'courses': courses})

# GET one specific course
@app.route('/ce/api/v1.0/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
	course = list(filter(lambda t: t['id'] == course_id, courses))
	if len(course) == 0:
		abort(404)
	return jsonify({'course': course[0]})

# transfer error page into JSON format
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

# POST a new course
@app.route('/ce/api/v1.0/courses', methods=['POST'])
def create_course():
	if not request.json or not 'title' in request.json:
		abort(400)
	course = {
		'id': courses[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
	}	
	courses.append(course)
	return jsonify({'course': course}), 201

# PUT an update
@app.route('/ce/api/v1.0/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
	course = list(filter(lambda t: t['id'] == course_id, courses))
	if len(course) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	course[0]['title'] = request.json.get('title', course[0]['title'])
	course[0]['description'] = request.json.get('description', course[0]['description'])
	course[0]['done'] = request.json.get('done', course[0]['done'])
	return jsonify({'course': course[0]})

# DELETE a course
@app.route('/ce/api/v1.0/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = list(filter(lambda t: t['id'] == course_id, courses))
    if len(course) == 0:
        abort(404)
    courses.remove(course[0])
    return jsonify({'result': True})

# optimize web service interface: change id into url
def make_client_course(course):
	new_course = {}
	for field in course:
		if field == 'id':
			new_course['url'] = url_for('get_course', course_id=course['id'],_external=True)
		else:
			new_course[field] = course[field]
	return new_course

# @app.route('/ce/api/v1.0/courses',methods=['GET'])
# def get_courses():
# 	return jsonify({'courses': list(map(make_client_course, courses))})
 
# strengthen security: login session
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'miguel':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.route('/ce/api/v1.0/courses', methods=['GET'])
@auth.login_required
def get_courses():
	return jsonify({'courses': list(map(make_client_course, courses))})

if __name__ == '__main__':
	app.run(debug=True)