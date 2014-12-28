shortimer
=========

shortimer is a [django](http://www.djangoproject.com) web app that collects job 
announcements from the code4lib discussion list and puts them on the Web. 
Basically shortimer subscribes to the code4lib discussion list, and periodically
pops its email account looking for job advertisements. When it notices what
looks like a job ad it adds it to the database, where it can be curated by
folks who have an account.

Install
-------

To get shortimer running locally you will need to follow these instructions. 
The first step installs virtualenv which provides a Python sandbox environment 
for you to install the other dependencies. Clearly apt-get is only available 
on Debian based systems, but you will probably have a similar mechanism to 
get virtualenv installed using other packages managers (homebrew, rpm, etc).
From there on things should work independent of what operating system you are
using.

### Steps you do only the first time you set up the project
1. `sudo apt-get install python-virtualenv mysql-server libmysqlclient-dev`
1. `git clone git://github.com/code4lib/shortimer.git`
1. `cd shortimer`
1. `virtualenv --no-site-packages ENV`
1. `source ENV/bin/activate`
1. Set up your settings file (see `settings/README.md` for details)
1. In your python shell: `import nltk`, then `nltk.download()` (this will open up a new GUI window outside your shell). Download Models > maxent_treebank_pos_tagger
1. Acquire a Google public API key and turn on the Freebase API for your Google account. (The specifics of how to do this change on Google's whim, so Googling for them is your best bet.)

### Steps you do the first time and every time things may have changed
1. `pip install -r requirements.txt`
1. `export DJANGO_SETTINGS_MODULE=shortimer.settings.dev.yoursettingsmodule` 
1. In order for people to login with their github, facebook, twitter, linkedin
credentials you will need to create applications on those sites, and set their oauth keys as environment variables with the names referenced in settings/base.py. For development you can probably get by with just one login provider.
1. Set the `GOOGLE_API_KEY` environment variable (this enables Freebase to work, which is required for some tests and functionality).
1. `python manage.py syncdb --migrate --noinput`
1. `python manage.py runserver`
1. Point your web browser at http://locahost:8000 .
1. If you are doing development and want a snapshot of the db just ask edsu.

If you install virtualenvwrapper on top of virtualenv, you can set all the environment variables in `~/.virtualenvs/customfit/bin/postactivate` the first time you set up the project, and you won't need to do those steps again.

### If you want to develop on localhost without setting up socialauth login providers
1. `python manage.py createsuperuser` and follow the prompts
1. Add the following to your personal settings file:
'''
AUTHENTICATION_BACKENDS += (
'django.contrib.auth.backends.ModelBackend',
)
'''

Your superuser can now log in at `/admin`.

Ideas
-----

It might be useful for shortimer to monitor places where jobs are posted on the
web and scrape them, where they could then be approved (or deleted) in the queue. Here are some sites that might be useful to watch:

* [Digital Preservation Coalition](http://www.dpconline.org/newsroom/vacancies)
* [Library jobs in the Chronicle of Higher Education](http://chronicle.com/jobSearch?searchQueryString=&search_sortedBy=publicationDate+DESC&facetName%5B0%5D=jobadposition&facetName%5B1%5D=jobadcategory&facetValue%5B0%5D=54&facetValue%5B1%5D=58&facetCaption%5B0%5D=Professional+fields&facetCaption%5B1%5D=Library%2F+information+sciences&omni_mfs=true)
* [Digital Humanities Job Archive](http://jobs.lofhm.org/)
* [ALA Job List](http://joblist.ala.org/)
* [libjobs](http://infoserv.inist.fr/wwsympa.fcgi/subrequest/libjobs)
* [LITA Jobs](http://www.ala.org/lita/professional/jobs/looking)
* [NDIIPP on Twitter](https://twitter.com/#!/ndiipp)
* [metadatalibrarians](http://lists.monarchos.com/listinfo.cgi/metadatalibrarians-monarchos.com)
* [Archives Gig](http://archivesgig.livejournal.com/) also available on [Twitter](https://twitter.com/#!/archivesgig)
* [Canadian Libraries Association Jobs](http://www.cla.ca/AM/Template.cfm?Section=Job_Search&Template=/CM/HTMLDisplay.cfm&ContentID=1964)
* [Society of American Archivists](http://careers.archivists.org/)
* [libgig](http://publicboard.libgig.com/)
* [DigitalKoans](http://digital-scholarship.org/digitalkoans/category/digital-library-jobs/) also on [Twitter](https://twitter.com/DigitalKoans)
* [idealist](http://www.idealist.org/)

License
-------

* [CC0](https://creativecommons.org/about/cc0)
