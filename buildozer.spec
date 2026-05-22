
[app]

# (str) Title of your application
title = MeltDetector

# (str) Package name
package.name = meltdetector

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3, kivy, numpy, opencv-python, pyjnius

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# =============================================================================
# Android specific
# =============================================================================

# (list) Permissions
android.permissions = CAMERA, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage for binary leak protection
android.private_storage = True

# (list) Android architectures to build for
android.archs = arm64-v8a

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android architectural type to target (either 'main' or 'activity')
android.type = main

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
