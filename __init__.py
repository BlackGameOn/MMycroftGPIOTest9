from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

class LedControle(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('led_skill.intent')
    def handle_led_skille(self, message):
        self.speak_dialog('led_skill')
        GPIO.output(14,False)
        GPIO.output(15,False)
        GPIO.output(18,False)

def create_skill():
    return LedControle()

