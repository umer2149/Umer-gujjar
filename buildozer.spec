[app]
title = Umar Gujjar
package.name = umargujjar
package.domain = com.umar.gujjar
source.dir = .
version = 1.0
requirements = python3,kivy==2.3.0,pyjnius,android
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, QUERY_ALL_PACKAGES
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
