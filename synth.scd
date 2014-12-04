s.boot

// Synths
(

    // Acid note

    SynthDef(\acid,{ arg freq, gain = 1, pos = 0, swoopfreq = 4000;
	    var envy = EnvGen.ar(Env.perc,doneAction: 2);
	    var outsnd = Saw.ar(freq, envy * gain);
	    var fline = Line.ar(swoopfreq,400,0.15);
	    var acid = Resonz.ar(outsnd,fline, 0.1);
	    Out.ar(0, Pan2.ar( acid, pos ) );
    }).add;

    // Drum sounds

    // load the snare, bass drum, hat, and clap into the buffer
    ~snare = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/SNARE.WAV");
    ~kick = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/BD.wav");
    ~hat = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/HAT.WAV");
    ~clap = Buffer.read(s, "/Users/thrax/Google Drive/fall_2014/MUS_2984/assignments/final-project/mus2984_final/drumsounds/CLAP.WAV");

    // synthdef that can play from a buffer
    SynthDef(\playSound,{arg buf, pos = 0, gain = 0.1;
	    Out.ar(0,
		    Pan2.ar( PlayBuf.ar(1,buf, doneAction:2),pos,gain ) );
    }).add;

    // message must start with /acid
    ~one = OSCFunc( { | msg, time, addr, port |
	    // frequency is first element in message array
	    var pyFreq = msg[1].asFloat;

	    // play the synth with the user's input
	    Synth(\acid,[\freq,pyFreq, \gain, 2]);
    }, '/acid' );

    // create a synth that plays snare on /snare OSC command
    ~two = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~snare]);
    }, '/snare' );

    // create a synth that plays snare on /snare OSC command
    ~three = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~kick]);
    }, '/kick' );

    // create a synth that plays snare on /snare OSC command
    ~four = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~hat]);
    }, '/hat' );

    // create a synth that plays snare on /clap OSC command
    ~five = OSCFunc( { | msg, time, addr, port |
	    Synth(\playSound, [\buf, ~clap]);
    }, '/clap' );

    "Done loading synths";

)

s.quit