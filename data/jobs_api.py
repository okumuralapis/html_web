from flask import jsonify, Blueprint, make_response
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
