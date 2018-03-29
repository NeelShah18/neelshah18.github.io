---
layout: post
title: No-SQL database Redis - PART-2
---

## NoSQL:
<div style="text-align: justify">Hello, welcome to Part -2 of NoSql database blog. Today, we are look into to redis database.</div>
<div style="text-align: justify">Redis is an in-memory key value datastore written in ANSI C programming language by Salvatore Sanfilippo.  Redis not only supports string datatype but it also supports list,  set, sorted sets, hashes datatypes, and provides a rich set of operations to work with these types. If you have worked with Memcached (an in-memory object caching system), you will find that it is very similar, but Redis is Memcached++.  Redis not only supports rich datatypes, but it also supports data replication and can save data to disk.</div>

#### Redis: What for?:
* Cache out-of-process
* Duplicate detector
* LIFO/FIFO Queues
* Priority Queue
* Distributed HashMap
* UID Generator
* Pub/Sub
* Real-time analytics & chat apps
* Counting Stuff
* Metrics DB
* Implement expires on items
* Leaderboards (high game scores)
* Geolocation lookup
* API throttling (rate-limits)
* Autocomplete
* Social activity feed

#### Who's using Redis?:
* Twitter
* Github
* Weibo
* Pinterest
* Snapchat
* Craigslist
* Digg
* StackOverflow
* Flickr
* 220.000.000.000 commands per day
* 500.000.000.000 reads per day
* 50.000.000.000 writes per day
* 500+ servers 2000+ Redis instances!

#### key Features:
* Atomic operations
* Lua Scripting
* Pub/Sub
* Transactions
* Master/Slave replication
* Cluster (with automatic sharding)*
* Automatic failover (Redis Sentinel)
* Append Only File (AOF) persistence
* Snapshot (RDB file) persistence
* Redis can handle up to 232 keys and was tested in practice to handle at least 250 million of keys per instance.
* Every list, set, and sorted set, can hold 232 elements.

#### Advantages:
* Blazing Fast
* Robust
* Easy to setup, Use and maintain
* Extensible with LUA scripting

#### Disadvantages:
* Persistence consumes lot of I/O when using RDB
* All your data must fit in memory

**Best used:** For rapidly changing data with a foreseeable database size (should fit mostly in memory).

**For example:** o store real-time stock prices. Real-time analytics. Leaderboards. Real-time communication. And wherever you used memory cached before.

#### What happens if Redis runs out of memory?:
<div style="text-align: justify">Redis will either be killed by the Linux kernel OOM killer, crash with an error, or will start to slow down. With modern operating systems malloc() returning NULL is not common. Usually the server will start swapping, and Redis performances will degrade so you'll probably notice there is something wrong. The INFO command will report the amount of memory Redis is using so you can write scripts that monitor your Redis servers checking for critical conditions.</div>

#### Supported Language
<div style="text-align: justify">Many languages that have Redis bindings, including : ActionScript, C, C++, C#, Clojure, Common Lisp, Dart, Erlang, Go, Haskell, Haxe, Io, Java, JavaScript (Node.js), Lua, Objective-C, Perl, PHP, Pure Data, Python, R, Ruby, Scala, Smalltalk and Tcl.</div>

#### Redis Data Structure:
* Redis is not a plain key-value store. It is a data structures server, supporting a different kind of values. Here is a list all the data structures supported by Redis.
* Binary-safe strings.
* Lists: collections of string elements sorted according to the order of insertion. They have linked lists.
* Sets: collections of unique, unsorted string elements.
* Sorted sets, similar to Sets but where every string element is associated with a floating number value, called the score.
* Hashes, which are maps composed of fields associated with values. Both the field and the value are strings. This is very similar to Ruby or Python hashes.
* Bit arrays: it is possible, using special commands, to handle String values like an array of bits: the.
* HyperLogLogs: this is a probabilistic data structure which is used to estimate the cardinality of a set.


#### References:
* [https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis](https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
* [https://redis.io/](https://redis.io/)