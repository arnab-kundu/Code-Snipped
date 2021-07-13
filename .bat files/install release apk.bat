c:
cd C:\Users\Dell\AndroidStudioProjects\ArnabsMessenger\app\release
dir

xcopy /y arnabsmessenger-v2.2.9(15)-release.apk C:\Users\Dell\AppData\Local\Android\Sdk\platform-tools
cd C:\Users\Dell\AppData\Local\Android\Sdk\platform-tools
adb install arnabsmessenger-v2.2.9(15)-release.apk
PAUSE