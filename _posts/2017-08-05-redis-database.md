---
layout: post
title: No-SQL database MongoDB - PART-1
---

## NoSQL:
<div style="text-align: justify"><b>NoSQL</b> can mean <b>"not SQL"</b> or <b>"not only SQL"</b>. It is used for storing unstructured data, which increasing far more rapidly than structured data and which does not fit in <b>RDBMS</b> such as user and session data; chat, messaging, and log data; time series data such as IoT and device data; and large objects such as video and images.</div>

**NoSQL Database Types:**
* **Document databases** pair each key with a complex data structure known as a document. Documents can contain many different key-value pairs, or key-array pairs, or even nested documents.
* **Graph stores** are used to store information about networks of data, such as social connections. Graph stores include Neo4J and Giraph.
* **Key-value stores** are the simplest NoSQL databases. Every single item in the database is stored as an attribute name (or 'key'), together with its value. Examples of key-value stores are Riak and Berkeley DB. Some key-value stores, such as Redis, allow each value to have a type, such as 'integer', which adds functionality.
* **Wide-column stores** such as Cassandra and HBase are optimized for queries over large datasets, and store columns of data together, instead of rows.

## List of NoSQL database which are widely used:
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
#### History of MongoDB:
<div style="text-align: justify">The database was released to open source in 2009 and is available under the terms of the Free Software Foundation's GNU AGPL Version 3.0 commercial license. At the time of this writing, among other users, the insurance company MetLife is using MongoDB for customer service applications, the website Craigslist is using it for archiving data, the CERN physics lab is using it for data aggregation and discovery and the The New York Times newspaper is using MongoDB to support a form-building application for photo submissions.</div>

#### Use of MongoDB:
<div style="text-align: justify">Like other NoSQL databases, MongoDB supports dynamic schema design, allowing the documents in a collection to have different fields and structures. The database uses a document storage and data interchange format called BSON, which provides a binary representation of JSON-like documents. Automatic sharding enables data in a collection to be distributed across multiple systems for horizontal scalability as data volumes increase.</div> 

#### Why MongoDB?
* MongoDB stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time

* The document model maps to the objects in your application code, making data easy to work with

* Ad hoc queries, indexing, and real time aggregation provide powerful ways to access and analyze your data

* MongoDB is a distributed database at its core, so high availability, horizontal scaling, and geographic distribution are built in and easy to use

* MongoDB is free and open-source, published under the GNU Affero General Public License

#### Limitation of MongoDB:
* Max document size is 16 MB.
* Max document nesting level: 100 (documents inside documents inside documents).
* Indexed field can’t contain more than 1024 bytes.
* Max 64 indexes per collection.
* Max 31 fields can be used to create a compound index.
* Full-text search and geo indexes are mutually exclusive.
* Limit of documents in a capped collection can’t be more than 2**32. Otherwise, number of documents is unlimited.
* On windows, mongodb can’t store more than 4 TB of data (8 TB without journal)
* Max 12 nodes in a replica set.
* Max 7 voting nodes in a replica set.
* To rollback more than 300 MB of data manual intervention is needed.
* Group command doesn’t work in sharded cluster.
* $isolated, $snapshot, geoSearch don’t work in a sharded cluster.
* You can’t refer to db object in $where
* For sharding a collection it must be less than 256 GB.
* Individual (not multi) updates/removes in a sharded cluster must include shard key. Multi versions of these commands may not include shard key.
* Max 512 bytes for shard key values.
* Shard key values of a collection cannot be changed once sharding is done.

#### References:
* [https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis](https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
* [https://www.mongodb.com/nosql-explained](https://www.mongodb.com/nosql-explained)
* [https://www.mongodb.com/what-is-mongodb](https://www.mongodb.com/what-is-mongodb)
* [https://www.tutorialspoint.com/mongodb/](https://www.tutorialspoint.com/mongodb/)