---
layout: post
title: No-SQL database- PART-1: MongoDB
---

## NoSQL:
<div style="text-align: justify"><b>NoSQL</b> can mean <b>"not SQL"</b> or <b>"not only SQL"</b>. It is used for storing unstructured data, which increasing far more rapidly than structured data and which does not fit in <b>RDBMS</b> such as user and session data; chat, messaging, and log data; time series data such as IoT and device data; and large objects such as video and images.</div>

**NoSQL Database Types:**
* **Document databases** pair each key with a complex data structure known as a document. Documents can contain many different key-value pairs, or key-array pairs, or even nested documents.
* **Graph stores** are used to store information about networks of data, such as social connections. Graph stores include Neo4J and Giraph.
* **Key-value stores** are the simplest NoSQL databases. Every single item in the database is stored as an attribute name (or 'key'), together with its value. Examples of key-value stores are Riak and Berkeley DB. Some key-value stores, such as Redis, allow each value to have a type, such as 'integer', which adds functionality.
* **Wide-column stores** such as Cassandra and HBase are optimized for queries over large datasets, and store columns of data together, instead of rows.

## List of NoSQL database widely used:
* MongoDB
* Redis
* HBase
* BigTable
* Neo4j

## Let's start with MongoDB:

#### MongoDB introduction:
* Written in: C++
* Main point: JSON document store
* License: AGPL (Drivers: Apache)
* Protocol: Custom, binary (BSON)
* Master/slave replication (auto failover with replica sets)
* Sharding built-in
* Queries are javascript expressions
* Run arbitrary javascript functions server-side
* Geospatial queries
* Multiple storage engines with different performance characteristics
* Performance over features
* Document validation
* Journaling
* Powerful aggregation framework
* On 32bit systems, limited to ~2.5Gb
* Text search integrated
* GridFS to store big data + metadata (not actually an FS)
* Has geospatial indexing
* Data center aware
* **Best used:** If you need dynamic queries. If you prefer to define indexes, not map/reduce functions. If you need good performance on a big DB. If you wanted CouchDB, but your data changes too much, filling up disks.
* **For example:** For most things that you would do with MySQL or PostgreSQL, but having predefined columns really holds you back.

#### References:
[1: https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis](https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
[2: https://www.mongodb.com/nosql-explained](https://www.mongodb.com/nosql-explained)
[3: https://www.mongodb.com/what-is-mongodb](https://www.mongodb.com/what-is-mongodb)
[4: https://www.tutorialspoint.com/mongodb/](https://www.tutorialspoint.com/mongodb/)