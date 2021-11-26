# Data Structures

All of the data structures used by this project can be found in `pixelbuf_pi_animation.data`.

This section covers the data structures that are used by the rest of the parts of this project. They are meant to be as simple as possible while allowing for some advanced behavior. They are all built on top of Python's [`dataclasses` module](https://docs.python.org/3/library/dataclasses.html). Users are free to extend these classes to hold additional fields. As long as they adhere to the basic contracts set forth, the underlying classes that operate on these data structures won't be negatively impacted.

All of these classes are related by their hierarchy. An `Animation` contains one or many `Frame`s, each of which contain one or many `Pixel`s.

## Pixel Class

The `pixelbuf_pi_animation.data.Pixel` data class is the base of the object hierarchy. It represents the color and brightness state for a single LED. An instance of this class does not know which LED it represents, but rather only it's color values. It's up to other data structures to determine where a given `Pixel` is positioned in an animation.

## Frame Class

The `pixelbuf_pi_animation.data.Frame` data class represents some collection of `Pixel`s and how long they should be displayed for. Internally, the `Pixel`s are stored as a list. The order of the list matters. The `Frame` assumes that it is rendering to a LED strip and that the order of the list matches the order of the strip. Generally speaking, this is useful since the Adafruit LEDs chain together to form a "virtual" strip.

It's worth noting that this data class may be one that users consider creating derivatives of. For instance, if you are playing animations on something that is the shape of a star, you may wish to have some sort of data class that allows you to more easily represent the points on that star, perhaps by having properties like `top_point` or `left_point`. So long as that data class somehow ends up as a `Frame` with those `Pixel`s listed in the order that they are connected, the rest of the underlying system will work correctly.

## Animation Class

The `pixelbuf_pi_animation.data.Animation` data class represents some collection of `Frame`s, how many times they should be played on a loop, and if it should pause between plays. This is the parent-most class in this object hierarchy and is what gets passed to the various classes that are responsible for saving and playing animations.