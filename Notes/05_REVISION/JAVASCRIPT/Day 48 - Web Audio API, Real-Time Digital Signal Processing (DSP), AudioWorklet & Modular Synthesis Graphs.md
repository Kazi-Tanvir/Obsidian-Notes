---
tags:
  - javascript
  - web-audio
  - dsp
  - audioworklet
  - audio-nodes
  - realtime
  - performance
  - browser-api
date: 2026-09-17
---

# Day 48 - Web Audio API, Real-Time Digital Signal Processing (DSP), AudioWorklet & Modular Synthesis Graphs

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Web Audio Graph Architecture & Audio Rendering Thread

The Web Audio API is fundamentally different from the simple HTML5 <audio> element. It does not simply stream media files; it implements a high-performance **modular audio routing graph** (a Directed Acyclic Graph, or DAG) capable of sample-level manipulation, spatial 3D audio, and real-time synthesis.

#### The Dual-Thread Architectural Separation:

Audio requires continuous, glitch-free execution. If an audio buffer misses its delivery window by even \$5\\text{ms}\$, the operating system's audio output hardware suffers a **buffer underrun**, producing an audible click, pop, or drop-out.

```text
┌────────────────────────────────────── Web Audio Dual-Thread Architecture ──────────────────────────────────────┐
│                                                                                                                │
│  Main Browser Thread (V8 JavaScript Engine)                                                                    │
│  • Manages DOM, styling, layout, user clicks, React renders, garbage collection pauses.                        │
│  • Constructs the Audio Graph: ctx.createGain(), ctx.createOscillator(), nodeA.connect(nodeB).                 │
│  • Dispatches automation timelines: param.setValueAtTime(), param.exponentialRampToValueAtTime().             │
│                                                                                                                │
│  ══════════════════════════════ Boundary: Non-blocking IPC / Lock-free Queues ═══════════════════════════════  │
│                                                                                                                │
│  Real-Time Audio Rendering Thread (Native OS High-Priority Thread)                                            │
│  • Pulls 128-sample audio frames ("render quanta") at fixed sample rates (44.1 kHz or 48 kHz).                 │
│  • At 48 kHz, 128 samples must be computed every 2.67 milliseconds! (128 / 48000 ≈ 0.00267s)                  │
│  • Runs entirely in C++ (Blink/Gecko native core) or inside dedicated AudioWorklet sandboxes.                  │
│  • Completely immune to Main Thread UI freezes, layout recalculations, and JS GC pauses! ⚡                    │
│                                                                                                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. AudioWorklet vs. Deprecated ScriptProcessorNode

Prior to the modern AudioWorklet specification, custom audio manipulation relied on ScriptProcessorNode.

- **The Fatal Flaw of ScriptProcessorNode**: It ran user JavaScript callbacks directly on the **Main Thread**. Whenever the user scrolled a webpage, clicked a button, or V8 ran a Garbage Collection sweep, the main thread lagged, resulting in constant audio glitching.

- **AudioWorklet Solution**: An AudioWorkletProcessor runs user-supplied JavaScript inside a lightweight, dedicated audio thread sandbox. It has zero access to the DOM, window, or standard Web APIs, guaranteeing real-time priority.

#### Anatomy of an AudioWorkletProcessor:

```javascript
// custom-bitcrusher-processor.js (Loaded into AudioWorklet thread)
class BitcrusherProcessor extends AudioWorkletProcessor {
  static get parameterDescriptors() {
    return [
      {
        name: 'bitDepth',
        defaultValue: 8,
        minValue: 1,
        maxValue: 16,
        automationRate: 'a-rate', // Sample-accurate automation (128 values per quantum)
      },
      {
        name: 'frequencyReduction',
        defaultValue: 0.1,
        minValue: 0.01,
        maxValue: 1.0,
        automationRate: 'k-rate', // Block-level automation (1 value per quantum)
      }
    ];
  }
  constructor() {
    super();
    this.lastSampleValue = 0;
    this.phase = 0;
  }
  // CRITICAL V8 PERFORMANCE RULE: NEVER allocate objects, arrays, or closures inside process()!
  // Allocations trigger Garbage Collection, destroying real-time audio guarantees.
  process(inputs, outputs, parameters) {
    const input = inputs[0];
    const output = outputs[0];
    if (!input || input.length === 0) return true;
    const inputChannel0 = input[0];
    const outputChannel0 = output[0];
    const bitDepthParam = parameters.bitDepth;
    const freqReductionParam = parameters.frequencyReduction[0];
    const isBitDepthConstant = bitDepthParam.length === 1;
    for (let i = 0; i < inputChannel0.length; i++) {
      this.phase += freqReductionParam;
      if (this.phase >= 1.0) {
        this.phase -= 1.0;
        const currentBitDepth = isBitDepthConstant ? bitDepthParam[0] : bitDepthParam[i];
        const step = Math.pow(0.5, currentBitDepth);
        // Quantize float sample (-1.0 to +1.0) to discrete bit levels
        this.lastSampleValue = step * Math.floor(inputChannel0[i] / step + 0.5);
      }
      outputChannel0[i] = this.lastSampleValue;
    }
    // Returning true keeps the processor alive in the audio graph
    return true;
  }
}
registerProcessor('bitcrusher-processor', BitcrusherProcessor);
```

### 3. AudioParam Automation Curves & Glitch-Free Scheduling

Setting properties directly via assignment (e.g., gainNode.gain.value = 0.5) introduces immediate step discontinuities in the output waveform, manifesting as annoying "clicks" or "zipper noise". To achieve smooth parameter transitions, developers must use **AudioParam Timeline Automation**:

```javascript
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
const gainNode = audioCtx.createGain();

// Antipattern: Immediate mutation causes audio pop!
// gainNode.gain.value = 0.0;

// Production Pattern: Sample-accurate scheduling via AudioParam
const now = audioCtx.currentTime;

// 1. Cancel any active automations scheduled in the future
gainNode.gain.cancelScheduledValues(now);

// 2. Lock current baseline value
gainNode.gain.setValueAtTime(gainNode.gain.value, now);

// 3. Linear or Exponential Ramp to eliminate discontinuities
// Note: exponentialRamp cannot approach exactly 0.0 (mathematical singularity), use 0.0001
gainNode.gain.exponentialRampToValueAtTime(0.0001, now + 0.3); // 300ms smooth fadeout
```

```text
┌────────────────────────────────────── AudioParam Automation Curves ──────────────────────────────────────┐
│ Gain                                                                                                     │
│ 1.0 ┬───────┐ (setValueAtTime)                                                                           │
│     │        \                                                                                           │
│     │         \  linearRampToValueAtTime()                                                               │
│     │          \                                                                                         │
│ 0.5 │           └───┐ (setValueAtTime)                                                                   │
│     │                \                                                                                   │
│     │                 `.  exponentialRampToValueAtTime() (Natural acoustic decay)                         │
│     │                   `..                                                                              │
│ 0.0 ┴──────────────────────┴──────────────────────► Time                                                 │
│    t=0             t=1     t=2                    t=3                                                    │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4. Fast Fourier Transform (FFT) & Real-Time Spectral Analysis

The AnalyserNode provides real-time frequency-domain and time-domain analysis without modifying the audio signal pass-through.

- **Frequency Domain (getByteFrequencyData)**: Converts the time-series audio signal into frequency bins using the Fast Fourier Transform (FFT). Each bin represents signal amplitude across a frequency range (\$\\Delta f = \\frac{\\text{SampleRate}}{\\text{fftSize}}\$).

- **Time Domain (getByteTimeDomainData)**: Captures raw oscilloscope waveform values.

```javascript
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 2048; // Must be power of 2 between 32 and 32768
analyser.smoothingTimeConstant = 0.8; // Smooths transitions between frequency frames

const bufferLength = analyser.frequencyBinCount; // Exactly fftSize / 2 (1024)
const frequencyData = new Uint8Array(bufferLength);

function renderVisualizer() {
  requestAnimationFrame(renderVisualizer);
  analyser.getByteFrequencyData(frequencyData);
  // frequencyData[0] = Lowest bass frequencies
  // frequencyData[bufferLength - 1] = Nyquist frequency (SampleRate / 2, e.g., 24 kHz)
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Web Audio API Core Nodes & Methods:

-------------------------------------------------------------------------------------------------------- **Node / Interface**    **Category**      **Primary Method / Property**          **Description & Usage** ----------------------- ----------------- -------------------------------------- ----------------------- AudioContext            Engine            currentTime, sampleRate, state         The master audio environment; clock advances continuously in seconds.

AudioContext            Lifecycle         resume(), suspend(), close()           Required to resume context after user interaction (browser autoplay policy).

AudioWorklet            Engine            audioCtx.audioWorklet.addModule(url)   Asynchronously registers an AudioWorkletProcessor script into the audio thread.

OscillatorNode          Source            type, frequency, detune, start()       Generates periodic waveforms (sine, square, sawtooth, triangle).

GainNode                Processing        gain (AudioParam)                      Controls amplitude/volume; supports timeline automation.

BiquadFilterNode        Processing        type, frequency, Q, gain               Standard filters: lowpass, highpass, bandpass, notch, peaking.

AnalyserNode            Analysis          fftSize, getByteFrequencyData()        Non-destructive real-time FFT spectrum analyzer.

AudioBufferSourceNode   Source            buffer, playbackRate, loop             Plays in-memory decoded PCM audio chunks (AudioBuffer). --------------------------------------------------------------------------------------------------------

### AudioParam Automation Reference:

---------------------------------------------------------------------------------------------------------- **Method**                          **Target Behavior**     **Formula / Curve Shape** ----------------------------------- ----------------------- ---------------------------------------------- setValueAtTime(val, t)              Instantaneous change    Step function starting at time \$t\$.

linearRampToValueAtTime(val, t)     Linear transition       \$V(t) = V_0 + (V_1 - V_0) \\cdot \\frac{t - t_0}{t_1 - t_0}\$

exponentialRampToValueAtTime(val,   Perceptually natural    \$V(t) = V_0 \\cdot t)                                  decay                   \\left(\\frac{V_1}{V_0}\\right)^{\\frac{t - t_0}{t_1 - t_0}}\$ (Requires \$V_0, V_1 > 0\$)

setTargetAtTime(target, t, tau)     Asymptotic exponential  \$V(t) = \\text{target} + (V_0 - decay                   \\text{target}) \\cdot e^{-\\frac{t - t_0}{\\tau}}\$

cancelScheduledValues(t)            Clears timeline         Cancels all future automation events scheduled at or after time \$t\$. ----------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Problem 1 (Basic): Click-Free ADSR Envelope Generator

**Context**: Synthesizers shape raw oscillator tones using an **ADSR Envelope** (Attack, Decay, Sustain, Release) mapped to a GainNode. Poorly scheduled envelopes cause audible speaker pops whenever notes are triggered or released rapidly.

**Challenge**: Implement a class ADSREnvelope:

1.  Constructor accepts parameters: { attackTime: number, decayTime: number, sustainLevel: number, releaseTime: number }.

2.  triggerAttack(gainNode: GainNode, audioCtx: AudioContext): void:

    - Smoothly ramps from the current gain value to 1.0 over attackTime.

    - Ramps down from 1.0 to sustainLevel over decayTime.

3.  triggerRelease(gainNode: GainNode, audioCtx: AudioContext): void:

    - Smoothly ramps from the current sustain gain level down to 0.0001 over releaseTime.

    - Ensures that rapid re-triggering cancels existing schedules without causing discontinuous audio pops.

*Hint: Remember to use cancelScheduledValues(audioCtx.currentTime) and anchor the starting ramp with setValueAtTime(gainNode.gain.value, audioCtx.currentTime) before applying ramps!*

### Problem 2 (Intermediate): Real-Time Audio Energy & Bass-Drop Detector

**Context**: Interactive music visualizers and rhythm games need to detect high-energy frequency transients (e.g., bass drum hits) in real time from live streaming microphone or playback audio.

**Challenge**: Build a BassDropDetector class:

1.  Connects an AudioNode source through an AnalyserNode with fftSize = 512.

2.  Implements a processing loop utilizing requestAnimationFrame that monitors frequency bins corresponding to the sub-bass and bass spectrum (\$20\\text{Hz} - 150\\text{Hz}\$).

3.  Calculates the dynamic average energy over a rolling window of 40 frames.

4.  When current bass energy exceeds the rolling average by a configurable threshold multiplier (e.g., \$1.5\\times\$), fires an onBeat({ energy: number, variance: number }) callback.

5.  Implements a cooldown refractory period (e.g., \$250\\text{ms}\$) to prevent multiple duplicate triggers on a single acoustic transient.

*Hint: Calculate the frequency range for each bin using binIndex * (audioCtx.sampleRate / fftSize). Only evaluate bins whose frequencies fall inside the \$[20, 150]\\text{Hz}\$ range.*

### Problem 3 (Advanced): Custom Ring Modulator AudioWorklet with Zero Allocations

**Context**: High-performance audio DSP nodes cannot afford the memory or GC overhead of object allocations inside their per-quantum render loop. A **Ring Modulator** multiplies an incoming carrier signal by an internal carrier oscillator, creating futuristic metallic and robotic acoustic textures.

**Challenge**: Develop a complete two-part implementation:

1.  **The Processor (RingModulatorProcessor - AudioWorklet script string)**:

    - Exposes an AudioParam 'carrierFrequency' with defaultValue: 440, minValue: 20, maxValue: 5000, supporting sample-accurate 'a-rate' automation.

    - Maintains an internal carrier phase counter.

    - Multiplies each incoming audio sample \$x[n]\$ by \$\\sin(2\\pi \\cdot f_c \\cdot t)\$ on a sample-by-sample basis.

    - **Zero Allocation Invariant**: Strictly zero object, array, or closure creations inside process().

2.  **The Host Node Wrapper (RingModulatorNode extending AudioWorkletNode)**:

    - Registers the processor script dynamically via an in-memory Blob URL (URL.createObjectURL).

    - Exposes a typed TypeScript/JavaScript API to modulate carrierFrequency via standard AudioParam automations.

    - Provides a clean dispose() method that disconnects nodes and revokes object URLs.

*Hint: To avoid hosting an external .js file, package the worker script code inside a template literal string, convert it to a Blob([code], { type: 'application/javascript' }), and pass the blob URL to audioCtx.audioWorklet.addModule().*
