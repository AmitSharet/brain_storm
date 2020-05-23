"""
Server - gets the uploads of thoughts from the client and publishes them to the parsers and saver through
a queue.
"""

from .server import run_server

