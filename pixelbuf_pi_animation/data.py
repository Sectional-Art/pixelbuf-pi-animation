import functools
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pixel:
    """
    This class represents a single pixel within some Frame. One or more pixels together make up a Frame.
    """

    brightness: float
    """Represents the brightness of a pixel; must be between 0.0 and 1.0, inclusive."""

    red: int
    """Represents the red value of a pixel; must be between 0 and 255, inclusive."""

    green: int
    """Represents the green value of a pixel; must be between 0 and 255, inclusive."""

    blue: int
    """Represents the blue value of a pixel; must be between 0 and 255, inclusive."""

    def __post_init__(self):
        self._validate_brightness()
        self._validate_color()

    def _validate_brightness(self):
        min_b = 0.0
        max_b = 1.0
        if self.brightness < min_b or self.brightness > max_b:
            raise ValueError(f'Brightness must be between {min_b} and {max_b}, inclusive. '
                             f'The brightness for this pixel was set to {self.brightness}')

    def _validate_color(self):
        colors = {
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }
        min_c = 0
        max_c = 255

        for color, value in colors.items():
            if value < min_c or value > max_c:
                raise ValueError(f'Colors must be between {min_c} and {max_c}, inclusive. '
                                 f'The color {color} for this pixel was set to {value}')


@dataclass
class Frame:
    """
    This class represents a single frame of animation. One or more Frames stitched together create an Animation.
    """
    display_ms: int
    """The amount of time this frame should be displayed for, in milliseconds"""

    pixels: List[Pixel]
    """A list of Pixels that compose this frame, in the order that they are connected to the strand"""

    def __post_init__(self):
        self._validate_display_ms()
        self._validate_pixels()

    def _validate_display_ms(self):
        min_d = 1
        if self.display_ms < min_d:
            raise ValueError(f'Display ms must be a positive integer and not less than {min_d}. '
                             f'The display for this frame was set to {self.display_ms}')

    def _validate_pixels(self):
        min_p = 1
        if len(self.pixels) < min_p:
            raise ValueError(f'There must be a least {min_p} pixel(s) within this frame.')


@dataclass
class Animation:
    """
    This class represents a collection of frames that are to be played as an animation
    """

    frames: List[Frame]
    """A list of Frames in the order that they should be rendered"""

    loop_infinitely: bool
    """Determines if this animation should be shown in an infinite loop"""

    pause_between_play_ms: int
    """How many milliseconds to pause between animation loops; will be applied after showing all frames"""

    max_plays: Optional[int]
    """How many times to show the animation; Must be set to `None` if `loop_infinitely` is True"""

    def __post_init__(self):
        self._validate_frames()
        self._validate_pause_between_play_ms()
        self._validate_max_plays()

    def __len__(self):
        return len(self.frames)

    @property
    def frame_total_time_ms(self) -> int:
        """
        This property loops through all of the frames, sums the delay on each one, and returns the total.
        :return: total expected delay, in ms, of this animation
        """
        return functools.reduce(lambda value, element: value+element.display_ms, self.frames, 0)

    def _validate_frames(self):
        min_f = 1
        if len(self.frames) < min_f:
            raise ValueError(f'There must be at least {min_f} frame(s) within this animation.')

    def _validate_pause_between_play_ms(self):
        if self.pause_between_play_ms < 0:
            raise ValueError(f'The pause between plays cannot be negative.')

    def _validate_max_plays(self):
        if self.max_plays and self.max_plays < 0:
            raise ValueError(f'The max plays cannot be negative.')

        if self.max_plays and self.loop_infinitely:
            raise ValueError('max_plays must be set to None if loop_infinitely is set to True')

