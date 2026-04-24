#!/usr/bin/env python3
"""Flask app with mocked user login and i18n messages."""

from flask import Flask, g, render_template, request
from flask_babel import Babel
import flask_babel


class Config:
    """Application configuration for Babel."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """Return locale from query args when valid, otherwise use header match."""
    requested_locale = request.args.get("locale")
    if requested_locale and requested_locale in app.config["LANGUAGES"]:
        return requested_locale
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


def get_user():
    """Return mocked user dict when login_as is provided, else None."""
    login_as = request.args.get("login_as")
    if not login_as:
        return None
    try:
        user_id = int(login_as)
    except (TypeError, ValueError):
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """Populate flask.g.user with the logged-in user for each request."""
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)


def gettext(message_id: str, **kwargs) -> str:
    """Return the localized string for the given message identifier."""
    return flask_babel.gettext(message_id, **kwargs)


@app.route("/", methods=["GET"])
def index():
    """Render localized landing page."""
    return render_template(
        "5-index.html",
        locale=get_locale(),
        gettext=gettext,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
