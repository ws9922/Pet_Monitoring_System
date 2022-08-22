import pyttsx3
import time


def talkWith(engine, content):

    """ the content to read """
    engine.say(content)
    engine.runAndWait()


def talkContent(content):

    """ read the content and convert it to system voice """

    engine = pyttsx3.init()
    # Setting the speed rate
    engine.setProperty('rate', 260)
    # If the content is too long, set a period between them
    if len(content) > 20:
        con_list = content.split('.')
        for item in con_list:
            time.sleep(1)
            talkWith(engine, item)
    else:
        talkWith(engine, content)
