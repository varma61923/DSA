# System Design

## Scalability
Scalability is the system's ability to handle increased load. There are two types of scalability:
- **Vertical Scaling (Scaling Up)**: This involves adding more resources such as CPU, RAM to an existing machine.
- **Horizontal Scaling (Scaling Out)**: This involves adding more machines into the existing pool.

## Availability
Availability is the time a system remains operational to perform its required function in a specific period. It's usually measured as a percentage of uptime in a year.

- **High Availability**: Systems designed to be operational at all times without any downtime.
- **Fault Tolerance**: The ability of a system to continue operating properly in the event of a failure of some of its components.

## Reliability
Reliability is the probability that a system will fail in a given period. A reliable system should be able to handle different types of failures.

- **Redundancy**: Having backup components in case of a system failure. 
- **Recovery Strategy**: Procedures and measures that can bring back a system up from a failure.

Remember, designing a system with high scalability, availability, and reliability requires a good understanding of the system requirements, a good architecture, and also involves trade-offs.

# Client-Server Model

## Understanding the Client-Server Architecture
The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

- **Client**: Clients are devices like your personal computer, smartphone, or any machine that requests for the services or resources from the Server.
- **Server**: Servers are powerful machines or software programs that store and supply the requested resources or services to the clients over a network.

## Advantages of Client-Server Model
- **Centralization**: Easy to manage data, resources and can control each client’s access and permissions to the centralized server.
- **Scalability**: Can serve multiple clients.
- **Security**: Since the data is stored on the server, it's more secure.

## Limitations of Client-Server Model
- **Single point of failure**: If the server goes down, services can be interrupted.
- **Performance bottleneck**: With many clients or large amounts of data, the server can become a bottleneck.
- **Cost**: Servers can be expensive to set up and maintain.

Remember, understanding the client-server model is crucial as it forms the basis of network computing.

# Client-Server Model

## Overview

The **Client-Server Model** is a distributed application structure that partitions tasks or workloads between servers (providers of a resource or service) and clients (service requesters). In this model, clients send a request for data to the server via the internet, which the server processes and delivers back to the client.

## Working of the Client-Server Model

1. User enters the URL of the website or file.
2. The browser requests the DNS Server.
3. DNS Server looks up for the address of the Web Server.
4. The DNS Server responds with the IP address of the Web Server.
5. The browser sends an HTTP/HTTPS request to the Web Server’s IP.
6. The Server sends the necessary files for the website.
7. The browser renders the files and displays the website.

## Advantages

- **Centralized system**: All data is stored in a single place, making management easier.
- **Cost-efficient**: Lower maintenance cost and data recovery is possible.
- **Scalability**: The capacity of the client and servers can be adjusted separately.
- **Control and Security**: Consolidates resources on servers for greater control and security.

## Limitations

- **Prone to viruses**: If a server is infected, clients are at risk.
- **Prone to DOS attacks**: Servers can be targeted by Denial of Service (DOS) attacks.
- **Data integrity**: Data packets may be spoofed or modified during transmission.
- **Security risks**: Phishing or capturing login credentials are common, as are Man in the Middle (MITM) attacks.

## Key Takeaways

The client-server architecture allows for flexible client options and relies on a robust network for scalability and efficiency. Despite cost implications, the client-server model remains fundamental and has been shaped by trends such as cloud computing.

# Peer-to-Peer Model

## Overview

The **Peer-to-Peer (P2P) Model** is a network architecture that allows participants to carry out transactions without requiring a middle-man, central server, or an intermediary. In this decentralized model, each node, or peer, in the network acts both as a client and server. This design allows the direct sharing of resources, be it bandwidth, storage, or processing power, creating cooperative networking and efficient resource discovery without relying on a central server.

## Working of the Peer-to-Peer Model

In the P2P network architecture, the computers connect with each other in a workgroup to share files, and access to internet and printers. Each computer in the network has the same set of responsibilities and capabilities. Each device in the network serves as both a client and server.

## Advantages

- **Decentralization**: Instead of a central server, every peer shares resources directly with others, leading to a shared workload.
- **Autonomy**: Each node functions independently. No single node can control or govern the entire network, making P2P networks fundamentally democratic.
- **Anonymity**: Since direct communication happens between peers without a central server tracking the data transfer process, users can maintain their confidentiality.
- **Resource Sharing**: As each node in the network serves as both a client and provider, the network can share, replicate, and synchronize resources effectively and equitably.

## Limitations

- **Security Risks**: Since the nodes act as clients and servers, there is a constant threat of attack.
- **Data Integrity**: Data packets may be spoofed or modified during transmission.
- **Prone to Viruses**: If a node is infected, other nodes are at risk.
- **Prone to DOS Attacks**: Nodes can be targeted by Denial of Service (DOS) attacks.

## Key Takeaways

The P2P networks, with their myriad of features, offer a viable alternative to traditional client-server networks. Their shared, autonomous, and resilient nature, combined with high scalability and improved latency, make these networks well-suited to handle varying workloads and continually evolving digital ecosystems. However, it's crucial to use them judiciously and incorporate apt security measures to offset potential threats.

# Distributed Ledger Technology (DLT)

## Overview

**Distributed Ledger Technology (DLT)** is the technological infrastructure and protocols that allow simultaneous access, validation, and record updating across a networked database. It's the technology blockchains are created from.

## DLT Architecture

DLTs allow information to be stored securely and accurately using cryptography. The data can be accessed using "keys" and cryptographic signatures. Once the information is stored, it can become an immutable database.

## Advantages

- **Decentralization**: There is no central point of control or failure, making DLT more resilient to attacks.
- **Security**: DLT enhances accountability and accessibility.
- **Transparency**: The infrastructure allows users to view any changes and who made them.

## Limitations

- **Complexity**: DLT is still complex and difficult to scale.
- **Regulation**: It is not subject to strong regulation.

# Hybrid Model

## Overview

A **Hybrid Model** is a model developed by combining two traditional models. The base models can be anyone like a spiral model, V&V model, prototype model, etc., and the selection of models is as per requirements.

## Hybrid Model Architecture

The hybrid model follows all phases of SDLC along with flexibility in using the required models. Planning includes requirement ideas and inputs that help in getting the project execution approach and choosing the correct base models.

## Advantages

- **Flexibility**: It has the benefits of two individual models.
- **Fixed Pattern**: A defined pattern of base models is to be followed to carry out the whole processing.

## Limitations

The limitations of the Hybrid Model are not explicitly mentioned in the sources. However, one can infer that the limitations would depend on the specific models being combined. For instance, if a model with high complexity is combined with another, the resulting Hybrid Model might also be complex.

## Key Takeaways

The choice of network model depends on the specific requirements of the system. Each model has its own set of advantages and limitations, and the choice of model should align with the system's needs and constraints.

# Monolithic Architecture

## Overview
**Monolithic Architecture** is a traditional way of building applications. This software architecture principle has both advantages and disadvantages.

## Monolithic Architecture Overview
In Monolithic Architecture, all components of an application are integrated into a single, indivisible unit. The entire application, including the user interface, business logic, and data access layers, is developed, deployed, and maintained as a single entity.

## Advantages
- **Simplicity**: Monolithic architectures offer straightforward development and deployment processes.
- **Cost-Effectiveness**: For small to medium-sized projects or startups, monolithic architectures can be more cost-effective.
- **Performance**: In some cases, monolithic systems can provide better performance due to reduced communication overhead between components.
- **Security**: With fewer inter-service communication points, monolithic systems may have a reduced attack surface.

## Limitations
- **Scalability**: As the size and complexity of the application grow, it can become complex and difficult to maintain.
- **Flexibility**: Changes in the system can require significant effort and resources, as changes in one area can impact the entire system.

# Microservices Architecture

## Overview
**Microservices Architecture** is an approach to system design that breaks complex systems into more minor, more manageable services.

## Microservices Architecture Overview
In a Microservices Architecture, an application is broken down into a series of independently deployable services. Each of these services fulfills a specific purpose or meets a specific business need.

## Advantages
- **Independent Development and Deployment**: Each of the services in microservice is deployed independently. This enables faster development.
- **Small Focused Team**: To work on a single service, a small team is targeted.
- **Small CodeBase**: In a microservice architecture, a codebase or database is not shared.
- **Accelerate scalability**: Improve fault isolation.
- **Enhance team productivity**: Quicker deployment time.
- **Increase cost-efficiency**: This guide explains the advantages and disadvantages of microservices and how to manage and streamline microservices to simplify scalable app development.

## Limitations
- **Increased Complexity**: Microservices architecture provides many benefits, such as scalability, agility, fault isolation, technology diversity, and improved scalability. On the other hand, it also brings challenges like increased complexity, distributed system challenges, operational overhead, data management complexity, and service discovery and communication issues.
- **Higher Operational Costs**: Better scalability, faster deployment, and increased flexibility are among the advantages of microservices architecture. However, it comes with increased complexity, higher operational costs, and the potential for communication issues between services.

## Key Takeaways
The choice between Monolithic and Microservices Architectures depends on the specific requirements of the system. Each architecture has its own set of advantages and limitations, and the choice should align with the system's needs and constraints.

# SQL Databases: Structure, Operations, and Basic SQL Queries

## 1. Structure of SQL Databases

- **Databases**: In SQL, a database is a structured set of data. It serves as the main container that holds tables and other SQL structures like views, indexes, stored procedures, and functions.

- **Tables**: Tables are the fundamental building blocks of a database where data is stored. Each table represents a specific entity and consists of rows and columns.

- **Columns and Data Types**: Each column in a table has a unique name and a defined data type (like INT, VARCHAR, DATE, etc.) that dictates the kind of data it can store.

- **Rows**: Rows, also referred to as records, represent individual, implicitly structured data items in a table.

- **Primary Key**: A primary key is a unique identifier for each record in a table.

- **Foreign Key**: A foreign key is a field in a table that is a primary key in another table. It’s used to create a link between data in two tables.

## 2. Core SQL Operations (CRUD)

- **Create**: Creating new databases and tables, or adding new records to a table.

```sql
-- Creating a new database
CREATE DATABASE database_name;

-- Creating a new table
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);

-- Inserting data into a table
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

-- Selecting data from a table
SELECT * FROM table_name;
SELECT column1, column2 FROM table_name WHERE condition;

-- Updating data in a table
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;

-- Deleting data from a table
DELETE FROM table_name WHERE condition;

-- Selecting data from a database
SELECT column1, column2, ... FROM table_name WHERE condition;

-- Joining tables
SELECT columns FROM table1 JOIN table2 ON table1.column = table2.column;

-- Using aggregate functions
SELECT COUNT(column_name), AVG(column_name), MAX(column_name), MIN(column_name) FROM table_name WHERE condition;

-- Grouping data
SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;

```
# NoSQL Databases: Structure, Operations, and Basic NoSQL Queries

## 1. NoSQL Databases

NoSQL (Not Only SQL) databases are non-relational databases designed to handle data models other than the tabular relations used in relational databases. They are often used when dealing with large amounts of distributed data.

## 2. Structure

The primary components of a NoSQL database can vary greatly depending on the type of NoSQL database. There are four main types:

- **Document databases** (like MongoDB) store data in documents similar to JSON objects. Each document contains pairs of fields and values.
- **Key-value stores** (like Redis) are the simplest NoSQL databases. Every single item in the database is stored as an attribute name (or 'key'), together with its value.
- **Wide-column stores** (like Cassandra) store data in tables, rows, and dynamic columns.
- **Graph databases** (like Neo4j) are used to store information about networks, such as social connections.

## 3. Operations

The basic operations that can be performed on a NoSQL database are similar to SQL CRUD operations:

- **Create**: This involves creating new databases, tables (or other relevant data structures), or adding new data into a table.
- **Read (Retrieve)**: This involves fetching or retrieving the data from a database.
- **Update**: This involves modifying or updating existing data in a database.
- **Delete (Destroy)**: This involves removing existing data from a database.

## 4. Basic NoSQL Queries

Here are some basic NoSQL queries related to the CRUD operations:

```javascript
// Create
db.collection.insertOne({
    key1: "value1",
    key2: "value2",
    ...
});

// Read
db.collection.find({ key: "value" });

// Update
db.collection.updateOne({ key: "value" }, { $set: { key2: "newvalue" } });

// Delete
db.collection.deleteOne({ key: "value" });
```
# SQL vs NoSQL Databases: When to Use?

## SQL Databases

- **Use Case**: Ideal for applications with complex transactions or systems that require multi-row transactions. Examples include accounting systems or systems that need to comply with ACID (Atomicity, Consistency, Isolation, Durability) properties. They are also a good fit when the data structure is not expected to change frequently, meaning the schema is fairly static and unchanging.

- **Advantages**:
    - Provide a high degree of data consistency and integrity.
    - Excellent for complex queries due to their robust querying capabilities.
    - Widely adopted, meaning many developers have SQL skills and there are many resources available for SQL database management.

- **Disadvantages**:
    - Can become inefficient as the amount of data grows, and horizontal scaling (adding more servers) is often difficult.
    - May not be the best choice for hierarchical or multi-valued data sets.

## NoSQL Databases

- **Use Case**: Good fit for applications that require large amounts of data, low latency, and flexible data models, which are easy to update and change. They are often used with real-time web applications, content management systems, and big data analytics.

- **Advantages**:
    - Can handle large volumes of data at high speed (high read/write speeds).
    - Designed to excel in speed and volume (big data) and are capable of horizontal scaling, which means they can handle increased traffic simply by adding more servers to the database.

- **Disadvantages**:
    - Typically don't support ACID transactions and can have less consistency compared to SQL databases.
    - Querying capabilities are not as robust as SQL, and there is a lack of standardization since NoSQL is still relatively new compared to SQL.

# Database Sharding

**Database Sharding** is a technique to horizontally partition a large database into smaller pieces called shards. Each shard is an independent database instance holding a subset of the overall data, improving scalability, performance, and maintainability of databases in high-traffic and data-intensive applications.

## Key Concepts and Characteristics

- **Horizontal Partitioning**: Rows of a table are distributed across multiple database instances.
- **Shard Key**: A column or a set of columns used to determine how data is distributed across shards.
- **Data Distribution**: Implemented using strategies such as range-based, hash-based, or directory-based sharding.
- **Independent Shards**: Each shard operates independently, allowing for distributed data storage and processing.
- **Improved Performance**: By distributing data across multiple shards, the load on each shard is reduced, allowing for faster query execution.

## Use Cases

- **High-Traffic Applications**: Beneficial for applications that experience high levels of traffic and require the ability to handle a large number of concurrent users and requests.
- **Large Datasets**: Allows for distributing the data across multiple instances when dealing with massive datasets.
- **Geo-Distributed Data**: Can be used to store data closer to the users in different geographical regions, reducing latency.
- **Horizontal Scaling**: Enables horizontal scaling of databases, allowing for the addition of more shards as the data and traffic grow.
- **Improved Fault Tolerance**: If one shard experiences a failure, the other shards can continue operating independently.

## Challenges and Considerations

- **Complexity**: Implementing and managing a sharded database architecture can be complex.
- **Data Consistency**: Maintaining data consistency across shards can be challenging.
- **Query Complexity**: Some queries may need to be executed across multiple shards.
- **Data Skew**: If the shard key is not chosen carefully, it can lead to uneven data distribution across shards.

## Popular Databases that Support Sharding

MongoDB, Cassandra, MySQL (with manual sharding), and Redis (with client-side sharding).

## Example

Consider an e-commerce application that sells products worldwide. As the business grows, the application needs to handle a large number of users, process a high volume of transactions, and store a massive amount of product and user data. In this scenario, database sharding can be applied to improve scalability and performance.

Suppose the e-commerce application has a "Products" table that stores information about various products. The table has grown to millions of records, and the queries on this table are becoming slow due to the large dataset.

To apply sharding, we can use the "ProductID" column as the shard key. We can distribute the data across multiple shards based on a range of product IDs. For instance:

- Shard 1: ProductID range 1 to 1,000,000
- Shard 2: ProductID range 1,000,001 to 2,000,000
- Shard 3: ProductID range 2,000,001 to 3,000,000

Each shard is hosted on a separate database instance. When a query is executed to retrieve a specific product, the application determines the appropriate shard based on the ProductID and routes the query to the corresponding shard.

## Benefits

- **Improved Query Performance**: Each shard handles a smaller dataset, resulting in faster query execution.
- **Scalability**: Additional shards can be added to accommodate the increased data volume and traffic.
- **Fault Tolerance**: If one shard experiences a failure, the other shards can continue serving requests.

## Considerations

- **Data Distribution**: Choosing the appropriate shard key is crucial to ensure an even distribution of data across shards.
- **Cross-Shard Queries**: Queries that require data from multiple shards can be more challenging.
- **Data Consistency**: When data is updated or deleted, it's important to ensure consistency across shards.
