
name: Build Android APK

on:
push:
branches: [ "main" ]
workflow_dispatch:

jobs:
build:
runs-on: ubuntu-22.04

steps:
- name: Checkout code
uses: actions/checkout@v4

- name: Set up Python
uses: actions/setup-python@v5
with:
python-version: '3.10'

- name: Set up JDK
uses: actions/setup-java@v4
with:
distribution: 'temurin'
java-version: '17'

- name: Cache Buildozer
uses: actions/cache@v4
with:
path: .buildozer
key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}
restore-keys: |
${{ runner.os }}-buildozer-

- name: Install Buildozer and Dependencies
run: |
sudo apt-get update
sudo apt-get install -y build-essential ccache git libffi-dev libssl-dev autoconf automake libtool pkg-config zlib1g-dev python3-pip cmake g++
pip install --upgrade pip
pip install buildozer cython virtualenv

- name: Build APK with Buildozer
run: |
# Переменная для автоматического согласия внутри самого Buildozer
export APP_ALLOW_SDK_WARNINGS=1
buildozer android debug
