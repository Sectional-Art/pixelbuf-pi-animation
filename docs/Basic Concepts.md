# Basic Concepts

This project is made up of a few basic data structures to represent animations and some classes for doing things with those animations.

Data structures are Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) that represent the data within our system. They provide some basic validation, but generally speaking don't "do" anything. They just contain data.

Players are classes that can be used to turn the data structures into LED displays. Currently, there is only one type of player, but it's intended for this to change in the future.

Parsers are classes that can be used to convert the data structures to or from some sort of format so that they can be saved to disk or shared across a network. They're serializers with a more friendly name.

These three components combine to create a simple system where a user can define some sort of animation, play that animation, and save it or transmit it elsewhere for later use. This opens up a few few interesting possibilities:

- A user could generate the animation elsewhere (like on their desktop computer) and then send it to their Pi for playing
- A user could write a program to generate an animation and then play that on loop or even save it
- A user could write a program that generates an animation based on some sort of dynamic input, such as the weather, or the stock market, and then send that animation to a player for rendering

These use-cases were the sorts of things that were considered when writing this library.