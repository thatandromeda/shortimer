settings
=========

Settings files follow best practices laid out in _Two Scoops of Django_:

* All settings should be kept in version control.
* All settings should inherit from `base.py`.
* Add your personal development settings file under settings/dev. Pillage others' settings files for helpful tricks! It's fun.
* Secrets should be stored as environment variables (and kept _out_ of version control).
* Never hardcode file paths.
* Set `DJANGO_SETTINGS_MODULE` in your environment to your desired settings file. (If using virtualenvwrapper for local development, you can add `export DJANGO_SETTINGS_MODULE=shortimer.settings.dev.yoursettingsmodule` to `~/.virtualenvs/customfit/bin/postactivate`. If not using virtualenvwrapper, why not?)