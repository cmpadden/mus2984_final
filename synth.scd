s.boot


// SINGLE ACID NOTE
(
    SynthDef(\acid,{ arg freq, gain = 1, pos = 0, swoopfreq = 4000;
	    var envy = EnvGen.ar(Env.perc,doneAction: 2);
	    var outsnd = Saw.ar(freq, envy * gain);
	    var fline = Line.ar(swoopfreq,400,0.15);
	    var acid = Resonz.ar(outsnd,fline, 0.1);
	    Out.ar(0, Pan2.ar( acid, pos ) );
    }).add;

    // uses open sound control to retrieve attributes
    // message must start with /acid
    x = OSCFunc( { | msg, time, addr, port |
	    // frequency is first element in message array
	    var pyFreq = msg[1].asFloat;

	    // play the synth with the user's input
	    Synth(\acid,[\freq,pyFreq, \gain, 2]);
    }, '/acid' );
)

// SNARE
(
    // load snare sound into buffer
    ~snare = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/SNARE.WAV");

    // synthdef that can play from a buffer
    SynthDef(\playSound,{arg buf, pos = 0, gain = 0.1;
	    Out.ar(0,
		    Pan2.ar( PlayBuf.ar(1,buf, doneAction:2),pos,gain ) );
    }).add;

    // create a synth that plays snare on /snare OSC command
    x = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~snare]);
    }, '/snare' );
)

// KICK
(
    // load snare sound into buffer
    ~kick = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/BD.wav");

    // synthdef that can play from a buffer
    SynthDef(\playSound,{arg buf, pos = 0, gain = 0.25;
	    Out.ar(0,
		    Pan2.ar( PlayBuf.ar(1,buf, doneAction:2),pos,gain ) );
    }).add;

    // create a synth that plays snare on /snare OSC command
    x = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~kick]);
    }, '/kick' );
)

// HAT
(
    // load snare sound into buffer
    ~hat = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/HAT.WAV");

    // synthdef that can play from a buffer
    SynthDef(\playSound,{arg buf, pos = 0, gain = 0.25;
	    Out.ar(0,
		    Pan2.ar( PlayBuf.ar(1,buf, doneAction:2),pos,gain ) );
    }).add;

    // create a synth that plays snare on /snare OSC command
    x = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~hat]);
    }, '/hat' );
)

s.quit