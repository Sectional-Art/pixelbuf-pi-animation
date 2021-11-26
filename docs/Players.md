# Players

All of the players provided by this library can be found in the `pixelbuf_pi_animation.players` module.

Players are classes that can be used to render `Animation`s to LEDs. Since there are different ways to implement these details, it's possible that in the future there will be multiple players. For this release, it just so happens that there is one and only one player. In future releases there will be additional players available.

## SimplePixelBufPlayer

The `pixelbuf_pi_animation.players.SimplePixelBufPlayer` player is the first and simplest of all of the players. It works by accepting an Adafruit driver and animation and then provides a method for rendering that animation.

Examples can be found in the [Notebook section](https://github.com/Sectional-Art/pixelbuf-pi-animation/blob/master/notebooks/) of the code repository.


### Compatibility

S far, this player has only been tested with the [DotStar LEDs](https://learn.adafruit.com/adafruit-dotstar-leds) using the [Adafruit_CircuitPython_DotStar](https://github.com/adafruit/Adafruit_CircuitPython_DotStar) driver.

### Constructor

This class's constructor required an Adafruit driver that is built on top of their `adafruit_pixelbuf` library.


### Loading

Once you have an instance of `SimplePixelBufPlayer`, you can pass it an `Animation` by calling it's `load()` method. You may not play an animation until you have `load()`ed it.

### Playing

Once you have `load()` ed your animation, you may play it by calling `play()`. This function has a few special behaviors you should be aware of:

- It is not interruptable. Once it starts playing, there is no way to tell it to stop early. Be aware of this when playing an animation that is meant to loop infinitely.
- Frame timing is not precise. Let's say that you have an animation with 10 frames and each frame is supposed to show for 100ms. This animation's total play time should be 10 * 100ms, or 1 second. Because we're not using a real-time operating system, each frame may not show for exactly the amount of time asked for. It may skew depending on how busy the device is, the operating system version, etc.
- It does not take transmission delay into account. The player does not know how long it spends sending each pixel down the wire to the LEDs and therefore does not account for this time. The more LEDs you have to render and the shorter your frame display times are, the more pronounced this will become. Basic testing has shown that the animation can fall 10-15 seconds behind on a 100 second animation if the frame rate is too high.
- It does not self-correct it's timing. While such a player is currently being implemented, this player does not keep track of it's own "time drift" and does not attempt to correct for it. That makes this player less suitable for applications that require timing along side of other events, such as music or other light displays.
