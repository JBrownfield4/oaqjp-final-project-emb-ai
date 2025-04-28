from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection")

@app.route('/emotionDetection')
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detection(text_to_analyze)

    label = response['label']
    score = response['emotions']

    return "For the given statement, the system response is 'anger': {formated_response['anger']} 'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, 'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. The dominant emotion is {formated_response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
