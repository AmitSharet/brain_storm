parsers
*******
About:
======
The following parsers are currently implemented:

You're expected to implement the following parsers:

**Pose**
Collects the translation and the rotation of the user's head at a given timestamp, and publishes the result to a dedicated topic.

**Color Image**
Collects the color image of what the user was seeing at a given timestamp, and publishes the result to a dedicated topic.
Note: the data itself should be stored to disk, and only the metadata published.

**Depth Image**
Collects the depth image of what the user was seeing at a given timestamp, and publishes the result to a dedicated topic.
A depth image is a width × height array of floats, where each float represents how far the nearest surface from the user was, in meters. So, if the user was looking at a chair, the depth of its outline would be its proximity to her (for example, 0.5 for half a meter), and the wall behind it would be farther (for example, 1.0 for one meter).
The best (2D) way to represent it is using matplotlib's heatmap.
Note: the data itself should be stored to disk, and only the metadata published.

**Feelings**
Collects the feelings the user was experiencing at any timestamp, and publishes the result to a dedicated topic.



How to add a new parser:
========================

Adding a new parser is simple:

1. Create a file with the field name .py: for example if the new field you'd like to add is size just name the file size.py

2. In the file you created in step 1 create a single function with the name of the field which gets the whole data as input.

3. Parse the input data and return the results.

4. Put the new parser file you created in **brain_storm/parsers/parser_fields directory**



CLI and API:
============

Parsers implementation is located in brain_storm.parsers.
**and expose the following API:**







>>> from cortex.parsers import run_parser
>>> data = …
>>> result = run_parser('pose', data)





Which accepts a parser name and some raw data, as consumed from the message queue, and returns the result, as published to the message queue. Also we provide this cli CLI:






  toctree::
   :maxdepth: 2
