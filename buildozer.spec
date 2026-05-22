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
# Здесь мы четко указываем OpenCV и NumPy, которые нужны для детекции
requirements = python3,kivy,numpy,opencv-python

# (str) Custom source folders for requirements
# This can be comma separated list of folders
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (list) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# =============================================================================
# Android specific
# =============================================================================

# (list) Permissions
# Самое главное — даем приложению легальный доступ к железкам смартфона
android.permissions = CAMERA, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage for binary leak protection
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded)
#android.ant_path =

# (list) Android architectures to build for
# Оптимизируем под современные 64-битные процессоры
android.archs = arm64-v8a

# (bool) Allow service to be foreground
#android.service_foreground = False

# (list) Android application meta-data to set (key=value)
#android.meta_data =

# (list) Android library project to add (paths)
#android.add_libs =

# (str) Android logcat filters to use
# Настройка отладки — чтобы в логах Android было видно ошибки нашего Python-кода
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a symlink
#android.copy_libs = 1

# (str) The Android architectural type to target (either 'main' or 'activity')
android.type = main

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
