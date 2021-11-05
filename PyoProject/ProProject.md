I had no trouble with the first steps of the download process, but once I reach the final step I encountered an error message.

          include/servermodule.h:31:10: fatal error: 'sndfile.h' file not found
          #include "sndfile.h"

To attempt to fix it I tried to install 4 additional files

        brew install libsndfile

          brew install portaudio

          brew install portmidi

          brew install liblo

This did not work and after much head scratching I attempted to start from the very beginning and reinstall everything.

When I got to homebrew it seemed to not be working but I was assured that it was in fact downloading.

After about 15minutes of waiting homebrew successfully confirmed its download.

Unfortunately this did not fix any of my issues. The "brew install" series of commands still did not work and I still was unable to complete the last task.

Rachel theorized that I may not be the admin on my laptop, which we investigated and found that I am in fact the admin on my computer, so there must be another issue.

I scoured the internet for many hours and finally found code that fixed my issue...

      git -C $(brew --repo homebrew/core) checkout master

After this i was able to complete the brew install series of commands.

Unfortunately

      /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/CoreAudio.framework/Headers/AudioHardwareDeprecated.h:736:1: note: 'AudioDeviceRemoveIOProc' has been explicitly marked deprecated here
          AudioDeviceRemoveIOProc(    AudioDeviceID       inDevice,
                ^
36 warnings and 1 error generated.

I still was having trouble. My audio driver was not set up in a way that thee terminal liked

As a last ditch effort to fix things I ran this line of code

      brew install liblo libsndfile portaudio portmidi

AND WOW SOMETHING HAPPENED

        Warning: liblo 0.31 is already installed and up-to-date.
            To reinstall 0.31, run:
                  brew reinstall liblo
                    Warning: libsndfile 1.0.31 is already installed and up-to-date.
                    To reinstall 1.0.31, run:
                    brew reinstall libsndfile
                    Warning: portaudio 19.7.0 is already installed and up-to-date.
                    To reinstall 19.7.0, run:
                    brew reinstall portaudio
                    Warning: portmidi 217_2 is already installed and up-to-date.
                To reinstall 217_2, run:
                  brew reinstall portmidi

I reinstalled everything but alas...

              command '/usr/bin/gcc' failed with exit code 1

Back to square one

I downloaded

            brew install openssl

due to web reccomendations
and... nope
No improvements

I installed Jack, becuase you mentioned it to me, but again...
no change


i tried again the next day, because I was frustrated and couldn't get it out of my head and now when I tried to play the files I was told this.

            -bash: /Users/courtney/Documents/Apps/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py: Permission denied

I HAVE NO IDEA WHY
So I changed my privacy settings and gave terminal full disk access and still...
nothing...
no change...
nada...
I quit like seriously I give up what the heck why isn't anything working it worked for everyone else so why wont it work for me seriously what am i doing wrong this is so stupid like so incredibly stupid not one good thing about it

              sudo python3 setup.py install --use-coreaudio --debug

For the heck of it I tried this puppy out again and still no success

            36 warnings and 1 error generated.

At this point, i've given up
