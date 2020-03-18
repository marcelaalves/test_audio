#!/usr/bin/python3

import aiy.voice.audio as audio
import config
import communication
import os
import auxi
import time
import datetime

INIT_SOUND_PATH = 'soundfiles/ready_test.wav'
NO_CONNECTION_PATH = 'soundfiles/fatal_error.wav'
TRY_AGAIN_PATH = 'soundfiles/wait_dutch.wav'
TRY_LATER_PATH = 'soundfiles/error.wav'
NO_LOGIN_PATH = 'soundfiles/fatal_error.wav'
SLEEP_MODE_PATH = 'soundfiles/s00.wav'


def no_login():
    audio.play_wav(NO_LOGIN_PATH)
    return


def init_sound():
    audio.play_wav(INIT_SOUND_PATH)
    return


def no_connection():
    audio.play_wav(NO_CONNECTION_PATH)
    return


def try_again_later():
    audio.play_wav(TRY_LATER_PATH)
    return


def try_again():
    audio.play_wav(TRY_AGAIN_PATH)
    return


def sleep_mode_message():
    audio.play_wav(SLEEP_MODE_PATH)
    return


def play_on_box(path):
    try:
        name = auxi.get_file_name(path)
        if len(name) > 0:
            full_path = config.DIRECTORY_AUDIO_FILES + os.sep + path

            if os.path.exists(full_path):
                print("File available on the box")
                real_path = full_path
            else:
                print('This audio file does not exist on device')
                real_path = communication.download_audio_from_server(path)
            if not real_path is None and len(real_path) > 0:
                talk(real_path)
            else:
                print("Audio file is not available to download")
        else:
            print("Audio file is not available")
    except Exception as e:
        print(e)


def talk(path):
    l = 0
    try:
        if (path is None) or len(path) == 0:
            path = 'SoundFiles/no_audio.wav'
        # l = auxi.get_file_length(path)
        # a = datetime.datetime.now().time()
        # b = auxi.addSecs(a, l)
        audio.play_wav(path)
        """while datetime.datetime.now().time() <b:
            time.sleep(0.00001)"""
    except Exception as e:
        print(e)
