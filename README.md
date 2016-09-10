# rmotr sakila

Today we will practice how to make complex aggregation queries. For that we will be working with a well known testing database called `sakila`.

`sakila` describes the data model of a DVD rental store. It already provides both the DB schema and data. You will only need to concentrate in making queries and get statistics out of it.

### `sakila` schema

To get a better understanding of how `sakila` DB looks like, you can take a look at this DB schema diagram:

![sakila](http://2.bp.blogspot.com/-kRUKx7DWJ58/VepEHIwEGRI/AAAAAAAAEwc/FGlAO4riOE8/s1600/PostgreSQL-Sample-Database.png)

### Assignments

The goal of this group work is to implement the assignments listed in `sakila/assignments.py`. Each assignment will provide a docstring describing the queries you will need to implement.


### The `runtests` command

As we don't want to loose the DB data while running regular Django test cases, we implemented a way around to evaluate if your assignment solutions are valid. In `sakila/management/commands` you will find a `runtests` custom command. That command is going execute each of the assignments you implemented, and will compare the result with the expected one. If all assignments are working well, you will see a message like `All tests passing!` in the terminal.

### Add more assignments

We already provide a few assignments that you will need to implement. Even though, we also ask you to add a few more assignments with interesting queries or stats that you can imagine. You will need to add both the assignments and tests.

### Read only

All the query tests we implemented are based in the initial status of the DB. If you write or remove data from it, they will probably start failing. Try to not perform any write action on the DB. Just use it to execute your read-only queries.
