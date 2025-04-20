#ini
[app]
# (str) Title of your application
title = SpeechPracticeApp
version=1.0.0
# (str) Package name
package.name = speechpracticeapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,/content/speech_recognition-3.14.2-py3-none-any.whl,transformers,jiwer,pillow

# (str) Supported orientation (one of landscape, sensorLandscape, sensorPortrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android architecture, arm64-v8a by default
android.arch = armeabi-v7a