from time import sleep

from adafruit_pixelbuf import PixelBuf

from pixelbuf_pi_animation.data import Animation


class SimplePixelBufPlayer:
    """
    This class is able to take Animation objects and render them via any class that inherits from Adafruit's Pixelbuf
    class.

    Adafruit publishes a Python library called
    [Adafruit_CircuitPython_Pixelbuf](https://github.com/adafruit/Adafruit_CircuitPython_Pixelbuf). This library serves
    as the base class for many of their LED drivers. `PixelBufPlayer` is able to take anything that inherits from
    `PixelBuf` and use it to render output.

    An example of this is using the DotStar driver to handle the actual rendering:

    ```
    import adafruit_dotstar
    import board


    num_leds = 11
    controller = adafruit_dotstar.DotStar(board.SCLK, board.MOSI, num_leds, pixel_order=adafruit_dotstar.BGR, auto_write=False)
    animation = ...
    player = PixelBufPlayer(controller)
    player.load(animation)
    player.play()
    ```

    This player is the simple and most naive implementation you could imagine. Since the Pi is not a real-time computer,
    there are no guarantees around timing made. It also makes no attempt to correct for these things as the animation
    plays on. That will come in another release.
    """

    def __init__(self, controller: PixelBuf):
        """
        Constructor for creating SimplePixelBufPlayer objects. It takes an Adafruit driver that is built on the
        `adafruit_pixelbuf` library.
        :param controller: an Adafruit driver
        """
        self._controller: PixelBuf = controller
        self._animation: Animation = None

    def load(self, animation: Animation) -> None:
        """
        Pass the player the animation to play.


        :param animation: the animation to play
        :return: None
        """
        # TODO Are there any sanity checks we wish to run here?
        self._animation = animation

    def play(self) -> None:
        """
        Renders the frames to the controller device.

        Before calling this method, the user must call load() and pass in the Animation. Once that is done, the user can
        call this method to start the rendering. This function will parse and read the next frame, send it to the
        LED controller, and wait the specified amount of time before moving on.

        :return: None
        """
        # TODO We probably want to implement some sort of interrupt system here

        if not self._animation:
            raise RuntimeError('The load() function must be called before playing an animation can happen.')

        loop_count = 0
        while True:
            # TODO We need some sort of timing to help us with figuring out slow-downs so we know when to skip frames
            # Overall animation loop
            for frame_idx, frame in enumerate(self._animation.frames):

                # Loops the frames
                for pixel_idx, pixel in enumerate(frame.pixels):

                    # Loops the pixels
                    # TODO There is an efficiency that can possibly be gained here by "parsing" these frames earlier
                    if pixel is None:
                        self._controller[pixel_idx] = (0, 0, 0, 1.0)
                    else:
                        self._controller[pixel_idx] = (pixel.red, pixel.blue, pixel.green, pixel.brightness)

                # Show the frame for a while
                self._controller.show()
                sleep(frame.display_ms / 1000)

            # The animation is complete; do some book-keeping after
            sleep(self._animation.pause_between_play_ms / 1000)
            if self._animation.loop_infinitely:
                continue

            loop_count += 1
            if loop_count >= self._animation.max_plays:
                break

        self._controller.fill((0, 0, 0))
        self._controller.show()
