# First Exercise:
This exercise is simply in Python, and is focused on functionality with system libraries, package inclusion, and maybe some file IO.
This is not object-oriented, multithreaded, or any of that fancy stuff. When we get working, things will be such, but all of that
complexity will be handled for us in the ROS and AUVSI libraries. Aside from conceptual issues, we should only have to think *procedurally.*

## The plan:
    This program is meant to read in a file with a bunch of data, pack these into a bunch of JSON objects (this is as OO as we will get),
    and save those out into other JSON files. Essentially, this is a parser or formatter. We have similar things in interop-giraffe currently.
    Not JSON, though, I don't think.

## The structure:
    root dir
        src
            main.py - The main loop of the program. Needs includes and some completion.
        include
            util.py - functions for filio, string parse, etc. May need some completion.
