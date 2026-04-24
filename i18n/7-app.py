#!/usr/bin/env python3
"""Flask app with user-aware locale and timezone selection."""

from flask import Flask, g, render_template, request
from flask_babel import Babel
import flask_babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    """Resolve locale using URL param,
        user preference, headers, and default."""
    languages = app.config["LANGUAGES"]
    requested_locale = request.args.get("locale")
    if requested_locale and requested_locale in languages:
        return requested_locale

    user_locale = None
    if getattr(g, "user", None):
        user_locale = getattr(g, "user", {}).get("locale")
    if user_locale and user_locale in languages:
        return user_locale

    return (
        request.accept_languages.best_match(languages)
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


def validate_timezone(tz: str) -> str | None:
    """Return tz if valid, otherwise None."""
    if not tz:
        return None
    try:
        pytz.timezone(tz)
    except UnknownTimeZoneError:
        return None
    return tz


def get_timezone():
    """Resolve timezone using URL param, user preference, and default."""
    tz_param = validate_timezone(request.args.get("timezone"))
    if tz_param:
        return tz_param

    user_tz = None
    if getattr(g, "user", None):
        user_tz = validate_timezone(getattr(g, "user", {}).get("timezone"))
    if user_tz:
        return user_tz

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


def gettext(message_id: str, **kwargs) -> str:
    """Return the localized string for the given message identifier."""
    return flask_babel.gettext(message_id, **kwargs)


@app.route("/", methods=["GET"])
def index():
    """Render localized landing page."""
    return render_template(
        "7-index.html",
        locale=get_locale(),
        gettext=gettext,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
