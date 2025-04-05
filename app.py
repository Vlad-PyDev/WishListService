from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'project29_secret'
wishlists = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    if request.method == 'POST':
        item = request.form.get('item')
        if 'wishlist_id' not in session:
            session['wishlist_id'] = str(uuid.uuid4())
            wishlists[session['wishlist_id']] = []
        wishlists[session['wishlist_id']].append(item)
        return redirect(url_for('wishlist'))
    current_list = wishlists.get(session.get('wishlist_id'), [])
    return render_template('main.html', wishlist=current_list, wishlist_id=session.get('wishlist_id'))


if __name__ == '__main__':
    app.run(debug=True)