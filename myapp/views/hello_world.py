from flask import jsonify, request, render_template


def view():
    if request.method == 'GET':
        return render_template('index.html')

    body = request.get_json(force=True)
    
    return jsonify({'hello': body.get('name', 'world')})
