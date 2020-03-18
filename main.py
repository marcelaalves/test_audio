#!/usr/bin/python3

import RPi.GPIO as GPIO

import sys
import time
import threading

import speak
from volumecontroller import VolumeController

_volume_controller = VolumeController()


def test():
    speak.play_on_box("file_example.wav")
    while True:
        _volume_controller.handle()


if __name__ == '__main__':
    test()
