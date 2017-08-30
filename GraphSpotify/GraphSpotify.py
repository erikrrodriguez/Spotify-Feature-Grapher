import os
import sys
from .lastfm import LastFM
from flask import Flask

app = Flask(__name__)

# TODO: move to separate configuration file
LOG_FILE = "/var/www/apps/SpotifyGraph/logs/SpotifyGraph.log"

if not app.debug:
    import logging
    from logging import FileHandler
    from logging import Formatter

    # TODO: fix permissions on this file to be more restrictive
    file_handler = FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(Formatter(
        "%(asctime)s %(levelname)s: %(pathname)s:"
        + "%(lineno)d %(module)s:%(funcName)s %(message)s"))
    app.logger.addHandler(file_handler)

# TODO:
@app.route("/")
def home():
    app.logger.debug("Beginning to serve home page.")
    return "<h1>Front page of GraphSpotify</h1>" + sys.version

# TODO:
@app.route("/artist/<artist_id>")
def show_artist(artist_id):
    app.logger.debug("Beginning to serve artist %s." % artist_id)
    return "Page for artist: %s" % artist_id

# TODO:
@app.route("/album/<album_id>")
def show_album(album_id):
    app.logger.debug("Beginning to serve album %s." % album_id)
    return "Page for album: %s" % album_id

# TODO:
#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('404.html'), 404
