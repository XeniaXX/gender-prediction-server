#!flask/bin/python
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

c_df = pd.read_csv("/Users/Xenia/todo-api/views_by_cat")
df=c_df.drop(['gender'],axis=1)
data=df.to_dict('records')

from flask import abort

@app.route('/todo/api/v1.0/data/<int:p>/<string:session_id>', methods=['GET'])
def get_task(session_id,p):
    task = list(filter(lambda t: t['session_id'] == session_id, data))
    if len(task) == 0:
        abort(404)
    if p==1:
        return jsonify({'task': task[0:5]})
    elif p==2:
        t=task[0]
        t1=t.values()
        t1=list(t1)
        s=sum(t1[1:])
        t2=[t1[0]]
        for i in range(1,5):
            t2.append(t1[i]/s*100)
        return jsonify({'task': t2[0:5]})
    else:
        return jsonify({'no such parameter ':p})


from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
