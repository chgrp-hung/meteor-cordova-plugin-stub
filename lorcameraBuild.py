from subprocess import call
call(["meteor remove cordova:lorcamera"], shell=True)
call(["meteor add cordova:lorcamera@file://../lorcameraswift/LORCamera"], shell=True)
call(["meteor run ios-device"], shell=True)
