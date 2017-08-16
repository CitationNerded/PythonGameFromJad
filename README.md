# Python-game-example README

This is a crappy base project implemented and refactored by Jad Pamment

### What is it?

This is basic *game* built using the [pygame](http://pygame.org/lofi.html) library as part of the python library. The examples at [pygame](http://pygame.org/lofi.html) contains the outline for this project.

Is relies on a basic [mvc*ish*](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) structure to display and manipulate objects in a window. At this point it's pretty barebones - has lots of tweaks that can be made and lots of tests to be added.

### How to get it running....

The ```main()``` method sits inside ```baseApp.py``` and is used to run the entire project. All model, view and controller components are called from inside that method.

Just run ```baseApp.py``` and the in-built methods should do the rest.

### How to run tests...
Fucked if I know?
I'll build some unit tests and add them into the gradle task list.

### Important Notes

If you do fix something, or add in something useful. Please comment your commits and your code inapproriately. The only requirement is that it relates to your changes. Swearing and sarcasm are not required by are highly fucking recommended.

### Current State

* Basic mvc structure
* Basic hardwired window
* Basic directional keyboard controls
* Documentation can be found under /docs
* Now with virtualenv integration - (because it makes shit easy)
* Fuckin {py}gradle and shit. Why is this here? Because I'd rather shit in my
hand and clap than use maven. Also because virtualenv is too difficult apparently.

### TODO

* Add a unit test suite using [pyTest](http://doc.pytest.org/en/latest/)
* Implement CI test build
* I'll setup an artefactory. The linkedin one only has a small number of the artefacts that
I need.
* Someone needs to fix {py}gradle or at least build an artefactory to use with it - looking at you Keiran.
* Test suite should probably avoid anything fancy pants. I tried that in another branch. Didn't go to well.

### Contacts
* CitationNerded
* [HawkBaby](mailto:jad.pamment@gmail.com)
