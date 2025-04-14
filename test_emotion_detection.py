from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        #Joy
        result_1 = emotion_detection("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        #Anger
        result_2 = emotion_detection("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        #Disgust
        result_3 = emotion_detection("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        #Sadness
        result_4 = emotion_detection("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        #Fear
        result_5 = emotion_detection("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()
