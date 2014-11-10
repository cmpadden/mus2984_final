import numpy
from scikits.audiolab import play

def testsignal(frequency, amplitude=0.5, seconds=1., sampleRate=44100.):
    '''
    create a sine wave at hz for n seconds
    '''

    # determine cycles per sample
    cyclesPerSample = frequency / sampleRate

    # determine the total number of samples
    totalSamples = seconds * sampleRate

    return amplitude * numpy.sin( numpy.arange(0, totalSamples*cyclesPerSample, cyclesPerSample) * (2 * numpy.pi) )

# Mids (Middle A) B, C, D, E, F, G, A
scale = [246.94, 261.63, 293.66, 329.63, 349.23, 392, 440]
for note in scale:
    samples = testsignal(int(note))
    print samples
    play(samples)


