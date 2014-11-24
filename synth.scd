s.boot

(
// single acid note
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


s.quit