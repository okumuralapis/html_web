from flask import jsonify, Blueprint, make_response, request
from . import db_session
from .jobs import Job

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jb = db_sess.query(Job).all()
    return jsonify({'jobs': [item.to_dict(only=('id', 'job', 'team_leader',
                                                'work_size',
                                                'collaborators', 'is_finished')) for item in jb]})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Job).get(jobs_id)
    if not jb:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jb.to_dict(only=('id', 'job', 'team_leader',
                                     'work_size',
                                     'collaborators', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators',
                  'is_finished', 'category']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Job(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        category=request.json['category']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Job).get(jobs_id)
    if not jb:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jb)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET', 'POST'])
def change_jobs(jobs_id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Job).get(jobs_id)
    if not jb:
        return make_response(jsonify({'error': 'Not found'}), 404)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators',
                  'is_finished', 'category']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    jb.job = request.json['job']
    jb.team_leader = request.json['team_leader']
    jb.work_size = request.json['work_size']
    jb.collaborators = request.json['collaborators']
    jb.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'id': jb.id})
