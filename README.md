# Python-game-example README

This is a crappy base project implemented and refactored by Jad Pamment

### What is it?

This is basic *game* built using the [pygame](http://pygame.org/lofi.html) library as part of the python library. The examples at [pygame](http://pygame.org/lofi.html) contains the outline for this project.

Is relies on a basic [mvc*ish*](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) structure to display and manipulate objects in a window. At this point it's pretty barebones - has lots of tweaks that can be made and lots of tests to be added.

### How to get it running....
The ```main()``` method sits inside ```baseApp.py``` and is used to run the entire project. All model, view and controller components are called from inside that method.

Just run ```baseApp.py``` and the in-built methods should do the rest.

### Current State

* Basic mvc structure
* Basic hardwired window
* Basic directional keyboard controls

### TODO

* Add a unit test suite using [pyTest](http://doc.pytest.org/en/latest/)
* Implement CI test build
