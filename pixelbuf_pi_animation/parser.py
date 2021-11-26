import abc
import dataclasses
import json
from typing import IO

import dacite
import msgpack

from pixelbuf_pi_animation.data import Animation


class AnimationParser(abc.ABC):
    """
    Base class for all animation parsers.

    This base class defines all methods that are required for implementing an animation parser.
    """

    @staticmethod
    @abc.abstractmethod
    def read(file_input: IO) -> Animation:
        """
        Given some sort of file input, this method will read that file and return an Animation object.
        :param file_input:
        :return: an Animation object
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def write(writable_file: IO, animation: Animation) -> None:
        """
        Given a writable file and an animation, this method will write the given animation into that file. This method
        does not handle file cleanup or closing.
        :param writable_file:
        :param animation:
        :return:
        """
        pass


class JsonAnimationParser(AnimationParser):
    """
    Defines how to read Animations to/from JSON.
    """

    @staticmethod
    def read(file_input: IO) -> Animation:
        parsed_dict = json.load(file_input)
        return dacite.from_dict(data_class=Animation, data=parsed_dict)

    @staticmethod
    def write(writable_file: IO, animation: Animation) -> None:
        json.dump(dataclasses.asdict(animation), writable_file)


class MsgPackAnimationParser(AnimationParser):
    """
    Defines how to read/write animations in a compact MessagePack binary format.
    """

    @staticmethod
    def read(file_input: IO) -> Animation:
        parsed_dict = msgpack.unpack(file_input)
        return dacite.from_dict(data_class=Animation, data=parsed_dict)

    @staticmethod
    def write(writable_file: IO, animation: Animation) -> None:
        msgpack.pack(dataclasses.asdict(animation), writable_file)
