# Basic project with Flask

This folder contains the basis of Flask framework. I created it for snipet purposes and as a notebook. 
Big projects are not more than lots of basic projects.

Flask contains a version of logger, it will deactivate it in production mode so you must take advantage of it.
To use is as easy as write ``app.logger`` and then the level of the logger: info, warning, error.

-------
## Route creation.

I'm assuming that your IDE automatically creates the @app.route('/') so we're gonna create
another route to check how to do that.

The new route will be called ``say_hey``. This new will be write inside the route decorator
and then, create a function. Can have the name you want but i'll use the same.

To indicate that we can receive data we must give a variable name in the route inside '< >' chars
by default flask will indicate is a string with no slashes. By now we add ``<name>``, put it as a
parameter in our function and use it in the return.

To parse an integer we must write '<int:age>' in path. To show that we create a new route
called age. You will see that is almost identically to how we use string in name, but now with
an integer.
