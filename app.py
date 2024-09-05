from flask import Flask, render_template, request, redirect, url_for, flash
from timeline_manager import TimelineManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages
manager = TimelineManager()

@app.route('/')
def index():
    return render_template('index.html', timelines=manager.timelines)

@app.route('/create_timeline', methods=['GET', 'POST'])
def create_timeline():
    if request.method == 'POST':
        name = request.form['name']
        manager.create_timeline(name)
        flash(f"Timeline '{name}' created successfully!")
        return redirect(url_for('index'))
    return render_template('create_timeline.html')

@app.route('/add_event/<timeline_name>', methods=['GET', 'POST'])
def add_event(timeline_name):
    timeline = manager.timelines.get(timeline_name.lower())
    if timeline is None:
        flash(f"Timeline '{timeline_name}' not found.")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        manager.add_event_to_timeline(timeline_name, name, date)
        flash(f"Event '{name}' added to '{timeline_name}'!")
        return redirect(url_for('view_timeline', name=timeline_name))
    
    return render_template('add_event.html', timeline_name=timeline_name)

@app.route('/view_timeline/<name>')
def view_timeline(name):
    timeline = manager.timelines.get(name.lower())
    if timeline is None:
        flash(f"Timeline '{name}' not found.")
        return redirect(url_for('index'))
    return render_template('view_timeline.html', timeline=timeline)

if __name__ == '__main__':
    app.run(debug=True)