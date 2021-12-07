So this project has been a trip for me. My first idea was to make an RPG battle simulator. After our initial meeting I began to investigate different engines to use. I started looking at Aframe, but had trouble installing it which turned me away. Next I followed the other coding link that you sent to me and was unable to follow it, as it is written to accompany a book. This made the tutorials feel very lacking in information, as the people in charge of the repository likely wanted people to buy their book rather than learning the material for free.

After this I decided to try one last attempt at an RPG. I attempted to begin coding a simple game in Godot. After opening the software, I found it to be difficult to format and ran into quite a few errors when trying to make my game appear visually as I desired it to. This left me in a tough spot, as I had no idea what program I was going to write my code with. Then it dawned on me.

Last fall I was involved in a game jame in which we made a short VN using renpy. So I looked it up and sure enough I was able to find a download for mac, so I loaded it up and began to write.

After quickly looking over a list of commands located here (https://www.renpy.org/doc/html/quickstart.html). I had a general idea of where to begin. The first thing I did was start to script the game. I began by using

# Messages following a hash mark

Although this will bold words on the github website, in renpy, this allows for a coder to add notes that are ignored by the rest of the code. I used this to outline my story and add cues where I wanted sprites to be shown and hid.

The next step was actually writing the script. All in all, the entire scripting process likely took over 20 hours of typing and editing. This is because there is a very particular way you must format text for it to appear correctly once implemented into your game.

First you must define characters.

define m = Character("Mingus")

Then each and every line must be written as such

m "Here I am."

Another feature I added was a custom player name, which I learned to do using a NUMBER of different links, as I was struggling to implement it into the text at first

https://www.renpy.org/wiki/renpy/doc/cookbook/Letting_players_choose_their_own_name
https://lemmasoft.renai.us/forums/viewtopic.php?t=37838

Another import aspect of my visual novel was implementing branching story paths. I was able to figure out how to set markers and jump to them on my own, but I also added a couple of exclusive options that lead into others (i.e. If you choose to befriend Maya you can sit with her, but if you don't than you sit alone)

https://www.renpy.org/wiki/renpy/doc/tutorials/Remembering_User_Choices

This article gave me SO MANY ideas, but unfortunately, if I implemented them all I wouldn't have time for any of my other finals...
So alas I settle for a could simple hidden variables to be added to the game and decided not to over complicate things, purely for my own sake.

One key scene in the game is a party that Mingus invites the player character to, for this moment I decide to implement a small mini game. I learned how to do this from these sources

https://github.com/RuolinZheng08/renpy-rhythm
https://www.youtube.com/watch?v=aMMI0nAKgI0&t=552s&ab_channel=Lynn%27sDevLab
https://r3dhummingbird.itch.io/renpy-rhythm-game

She also had a variety of other minigames, but I decided to just stick with the small rhythm game as I felt that it blended with the story quite well.

After I had fully written the spoken script, I went back and I added sprites, which were curated and edited by me. Every background is and image I took or found and then cropped properly as well as added a slight blur to (for effect.)  For each sprite I found an image and cut the character in question out.

I got permission from Maya before using her, but unfortunately I cannot ask Roger Brown or Mingus for their consent to appear in my game. I hope they don't mind.

The commands to add bgs is extremely simple just...

scene imagename

The commands for sprites are equally simple

show sprites

followed by

hide sprite


All in all I am quite happy with the outcome of my project. Although I feel it would be more complete with an OST and SFX, I feel that I have done most of the coding work that I an without expanding the story to an extent far beyond what is reasonable for a class project.

After this experience, I do believe that in the future I will use renpy more and actually intend to make a full length visual novel. It will likely be in the same vein as Hatoful Boyfriend, but nevertheless a full length game would be a project that I would thoroughly enjoy working on. I'm glad that I had the opportunity to do this project and look forward to coding more in the future.
