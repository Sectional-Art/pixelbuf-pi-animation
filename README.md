# Pixelbuf Pi Animation

This is a convenience library for building animations using a Raspberry Pi, an LED that Adafruit supports, and the Adafruit PixelBuf library. It allows users to model individual pixels into frames, individual frames into animations, and a player and serialization for those animations. This library was developed to allow makers to generate animations and be able to easily save them or send them to a player, which in some cases might be much easier than writing code to control the LEDs directly. Because the animation is serlaizeable, users could build tools to simulate animations in a way that makes sense for them and their project.

This is meant to work on top of LED libraries provided by Adafruit and run on a Raspberry Pi. Please read the rest of this document to find out if this project is useful for you before continuing onto the detailed documentation.

Important links:
- [Source code](https://github.com/Sectional-Art/pixelbuf-pi-animation)
- [Detailed Documentation](https://pixelbuf-pi-animation.readthedocs.io/en/latest/)

## Basic Structure and Concepts

This project presents 3 basic datastructures: a `Pixel`, a `Frame`, and an `Animation`. A pixel represents the color and brightness value for a single LED. A frame contains a list of pixels, in order of display, and some duration that frame should be showed for. An animation contains a list of frames, in order of display, with some settings around delays between plays and looping. 

To do something interesting with thees datastructures, this project also contains a player. Given an animation and some Adafruit LED library (internally called a "controller"), the player can render animations to the user's LEDs. This allows the user to separate the concerns of generating some "image" or desired animation from how it's rendered.

To make the animations reusable, this project provides an interface for serializing the animations so that they can be stored in disk, transmitted via networks, or created elsewhere altogether, or shared like source code or images.

## Compatibility

If you use any of the Adafruit CircuitPython LED libraries (such as [Adafruit_CircuitPython_DotStar](https://github.com/adafruit/Adafruit_CircuitPython_DotStar) or [Adafruit_CircuitPython_NeoPixel_SPI](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel_SPI)), they you may know that all of these libraries really build on top of [Adafruit_CircuitPython_Pixelbuf](https://github.com/adafruit/Adafruit_CircuitPython_Pixelbuf). Pixelbuf defines a base class for being able to set LED color, LED brightness, and rendering.

This library supports any Adafruit library that uses Pixelbuf as a base. It was specifically tested on [DotStars](https://learn.adafruit.com/adafruit-dotstar-leds) by using the [Adafruit_CircuitPython_DotStar library](https://github.com/adafruit/Adafruit_CircuitPython_DotStar).

## Comparison to Other Tools

In this section, we'll briefly discuss a few other tools and discuss some differences between them and `pixelbuf_pi_animation`.

### Adafruit_CircuitPython_framebuf and Related Libraries

[Adafruit_CircuitPython_framebuf](https://github.com/adafruit/Adafruit_CircuitPython_framebuf) is, as the name implies, a library (driver) written by Adafruit to represent frames. It represents a 2D rectangular grid of LEDs and provides functions for setting individual pixels, drawing shapes, displaying text, and more. For some use cases, especially LED grids with simple animations, this is perfect. It can also handle advanced animations and loading images.

This library is similar in that it also represents pixels and frames, so some of the concepts are familiar.

Some of the things that `pixelbuf_pi_animation` offers that Adafruit_CircuitPython_framebuf library doesn't are:
- basic timing control
- the ability to save and load animations (it can load images, but not whole animations)

Some of the things offered by Adafruit_CircuitPython_framebuf that `pixelbuf_pi_animation` doesn't are:
- higher-level functions, such as drawing shapes or loading images from common formats
- a greater number of tested platforms and LEDs

### Others

As of the time of this writing, there haven't been that many hours of research conducted. If you're aware of other libraries, I'd love to hear about it via a GitHub PR or Issue!
