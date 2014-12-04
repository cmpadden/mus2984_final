MUSIC 2984 Final Project
========================
Controls multiple SuperCollider synthesizers through an internet relay chat (IRC) bot. 

Setup
-------
 1. Run the IRC bot using: python2 ircBot.py
 2. Modify the sound file paths for SuperCollider
 3. Start the SuperCollider server using: s.boot;
 4. Start the SynthDefs
 5. Send commands!

Available Commands
--------------------

Command | Description
--- | ---
!musbot acid <freq> | Plays a single note of the acid synthesizer at a desired frequency.
!musbot snare | Plays the snare sound file.
!musbot kick | Plays the bass-drum sound file.
!musbot hat | Plays the hi-hat sound file.
!musbot clap | Plays the clap sound file.
