from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emotion_detection():
    analyzed_text = request.args.get('textToAnalyze')

    response = emotion_detector(analyzed_text)
    
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion == None:
        return "Invalid input! Try again."
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
