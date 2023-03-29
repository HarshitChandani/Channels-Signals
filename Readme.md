In this project I have used channel layer concept that is groups because to communicate with fixed channel name ,channel layer must not be in-memory.

## Channels documentation wording's

While channel layers are primarily designed for communicating between different instances of ASGI applications, they can also be used to offload work to a set of worker servers listening on fixed channel names, as a simple, very-low-latency task queue.

This feature does not work with the in-memory channel layer.

