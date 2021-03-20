# Microservices

## What is a Microservice?

* A software architecture pattern
* An alternative to monolithic applications
* A small, self-contained application

The term "microservices" tends to imply RESTful web APIs.

                                       +----------------+     +------------+
                       +-- REST API -->| Microservice A |<--->| Database A |
                       |               +----------------+     +------------+
    +-------------+    |
    |             |<---+               +----------------+     +------------+
    | API Gateway |<------ REST API -->| Microservice B |<--->| Database B |
    |             |<---+               +----------------+     +------------+
    +-------------+    |
                       |               +----------------+     +------------+
                       +-- REST API -->| Microservice C |<--->| Database C |
                                       +----------------+     +------------+

Key concepts:

* REST
* API endpoint
* HTTP methods
* Serialization

## REST Principles

1. Client-server architecture
    * Client: user interface
    * Server: data storage
2. Statelessness
    * Server does not maintain state (state is maintained client-side)
    * Client must include state in each message
3. Cacheability
    * Responses must define whether they are cacheable
4. Layered system
    * System architecture supports separating concerns across multiple servers, invisibly to the client
5. Uniform interface
    1. Resource identification in requests
        * Client identifies resources by URI
        * Server returns representation of the resource
    2. Resource manipulation through representations
        * Representations give the client enough information to modify the resource's state
    3. Self-descriptive messages
        * Messages explain how to interpret themselves
    4. Hypermedia as the engine of application state (HATEOAS)
        * Server provides links to client so client can discover resources it needs
6. Code-on-demand (optional)
    * Client-side scripting

Sources:

1. https://en.wikipedia.org/wiki/Representational_state_transfer
2. https://restfulapi.net/rest-architectural-constraints/

## Resources

* Each resource gets its own URI
* URIs are nouns, not verbs
* Representations contain
    1. The state of a resource at a specific point in time
    2. Metadata describing the resource
    3. Links to related resources

## HTTP Methods

There are several HTTP methods. The four most common correspond to the CRUD operations.

* GET
    * = Read
    * safe
    * idempotent
    * cacheable
* POST
    * = Create (kinda)
    * cacheable
* PUT
    * = Update (and Create)
    * idempotent
* DELETE
    * = Delete
    * idempotent

## HTTP Status Codes

* 1xx: Informational response
* 2xx: Successful
* 3xx: Redirection
* 4xx: Client error
* 5xx: Server error

See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

