
## AsyncIO

Any task that doesn’t give up control to the event loop will block all of the other tasks.

Python’s async model is built around concepts such as callbacks, events, transports, protocols, and futures.

At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.