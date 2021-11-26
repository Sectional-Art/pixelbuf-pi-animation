# Parsers

All parsers that come with this librar can be found in the `pixelbuf_pi_animation.parser` module.

Parsers are serializers. They allow a user to take an `Animation` and convert it to a string of characters or bytes for writing to a file or across a network. There are different parsers that support different formats. They all share an abstract base class, so it's possible for a user to come along and write their own parser to support whatever format they desire. Of course, it's also possible to save `Animation`s without using these abstractions.

Examples can be found in the [Notebook section](https://github.com/Sectional-Art/pixelbuf-pi-animation/blob/master/notebooks/) of the code repository.

## AnimationParser Class

This is the abstract base class that all other parsers inherit from. It defines the signature for a read and write method.

### Reading

The `AnimationParser.read(file_input: IO)` method is meant to read some sort of input and return an `Animation`. The function's signature defines the input as an `IO` object. This could be a file returned from `open()` or an in-memory buffer from `io.StringIO()` or `io.BytesIO()`.

The use of the `IO` generic was to signal that this method was primarily designed for file input. For example, it makes this pretty easy:

```python
with open('animation.json') as f:
    animation = JsonParser.read(f)
```

Of course, you're not limited to just a file. Let's say that you had data in memory (maybe from an HTTP call or from a message queue), you can still use these parsers by wrapping your input:

```python
input = read_from_message_queue()  # Some pretend method for reading strings (JSON) from a queue
memory_file = io.StringIO(input)
animation = JsonParser.read(memory_file)
```

As long as it is some sort of IO object, `read()` will understand it.

### Writing

The `AnimationParser.write(writable_file: IO, animation: Animation)` is the opposite of read, but works in a similar way. Given some `Animation` and some sort of IO object, this function will serialize and write that out to the IO object. The IO object could be a file returned from `open()` or an in-memory buffer from `io.StringIO()` or `io.BytesIO()`.

The use of the `IO` generic was to signal that this method was primarily designed for file output. For example, it makes this pretty easy:

```python
animation = ...  # Let's pretend we wrote a program to generate an animation
with open('animation.json', 'w') as f:
    animation = JsonParser.write(f, animation)
```

Of course, you're not limited to just a file. Let's say you wanted to write the `Animation` out to a JSON string so you could send it to a database or over a network:

```python
animation = ...  # Let's pretend we wrote a program to generate an animation
memory_file = io.StringIO(input)
JsonParser.write(memory_file, animation)

# Let's say we want it as a string. The first step is to reset the buffer's position:
memory_file.seek(0)

# Let's read it into a string:
animation_json = memory_file.read()
```

You could do anything you please with that output IO object, including controlling how it gets written to disk, manipulating it in memory, or creating your own custom file format that could contain many `Animation`s.

## JsonAnimationParser Class

The `pixelbuf_pi_animation.parser.JsonAnimationParser` class is used read and write `Animation`s as JSON. This is useful if you wish to be able to edit an `Animation` with a text editor. 

This parser assumes that any IO objects that it is dealing with are in text mode.

## MsgPackAnimationParser

The `pixelbuf_pi_animation.parser.MsgPackAnimationParser` class is used read and write `Animation`s in a binary format defined by the [MessagePack protocol](https://msgpack.org/index.html). This binary format allows for smaller files than the JSON format in case space or transmission time are of concern. MessagePack is certainly not the most compact binary format available, but it does give the user a commonly understood binary protocol that they could use in other languages and libraries if desired.

This parser assumes that any IO objects it is dealing with are in binary mode.
