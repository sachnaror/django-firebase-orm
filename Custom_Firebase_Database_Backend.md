What does the database backend do? It sits between the Django ORM and the actual database driver. There’s a PEP249, the DB-API 2.0 specification for python code to talk to the actual database driver.

Django abstracts away many of the differences between databases. But not all databases are created equal, so sometimes supporting what django expects is hard. Michael maintains the microsoft sql backend and showed some of the differences.



If you need a custom database backend, you could subclass an existing django database backend. There’s a read-only postgres db backend that has only a few lines of code. But if you create one from scratch, you need to implement about 8 classes.

- The **DatabaseWrapper** talks to the PEP249 python database library. Important: the “vendor” string to help django do specific things when it uses your database.
    column types,lookup and pattern operators
    There are other attributes that tell django how to map simple queries to actual SQL. iexact, less than, stuff like that.

- **CursorWrapper**. This one wraps the database cursor. So it tranlates execute, executemany, fetchone, fetchmany, fetchall, etc., to how the database talks.
- **CursorDebugWrapper** :  the same as above, only it adds timing information
    and logging everywhere. Django uses it in DEBUG mode.

- **DatabaseFeatures**: a list of features that the database supports. It is mainly used to automatically exclude/include tests from django’s testcase.
    how NULL Ordering works, SELECT FOR,
- **DatabaseSchemaEditor** : used by the migration mechanism to change your database schema. Altering a field is complex.
- **DatabaseIntrospection**. Used by the inspectdb management command. For his mssql database backend, it is important functionality. It is used relatively often.
- **DatabaseValidation** : this hooks the backend into django’s upon-startup validation mechanism.
- **DatabaseOperations** is where various bits and pieces that didn’t fit elsewhere went. A big part: date and time helpers.
    type casting and value extractions

There’s more than these classes, though.

If you make a query, in the end the .as_sql() method is called on an “sql compiler”. For a custom database backend, you might need to do customization here. Internally, django seems to prefer Postgresql’s sql style.

You need to look at database-specific ways in which you could do database injection. And catch it.

You need custom tests. And you’ll sometimes need to monkeypatch existing tests with @expectedFailure. But the good thing is that there’s a huge amount of existing tests that will be run on your database.

# Down the Rabbit Hole
1. Models
2. Managers
3. Queryset
4. Query
Data structure and methods representing a database query
Lives in django.db.models.sql
Two flavours: **Query** normal ORM operations and **RawQuery** for raw()
5. SQLCompiler
Turns Django Query instances into SQL for your database, Subclasses for
non-SELECT queries: SQLInsertCompiler and SQLDeleteCompiler for INSERT and
DELETE respectively
6. Database Backend
## Database Backend
- Base Implemetation,plus one per supported database (built-in ones in
    django.db.models.backends)

- Goes in the ENGINE part of database settings
- Specifies extremely low-level behaviour
- Is the boundary between Django and the Database drivers
    (psycopg2,cx_Oracle,etc.)


