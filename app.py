from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/post/<int:index>')
def post(index):
    post = posts[index]
    return render_template('post.html', post=post)

posts = [
    {'title': '첫 번째 글','content': '이것은 첫 번째 글의 내용입니다.'},
    {'title': '두 번째 글','content': '이것은 두 번째 글의 내용입니다.'},
]


if __name__ == '__main__':
    app.run(debug=True)
