## Description

This application contains API with CRUD (built with Django Rest Framework) for contacts, segments, email templates and 
email settings (flyps credentials, header name and email). 

The API endpoints will be described below.

**CAUTION**: This API doesn't contain any authentication system.

## Installation

For development: all you need to do is to have docker installed and repo locally, then type this line in directory with 
`docker-compose.yml` file:

```
docker-compose up
```

For other usages: image for this app is available at DockerHub, it's called `python-email-marketing-demo-recruitment-app` 

## Usage

At first, let's say you are using this app locally, so we can work on host `127.0.0.1`.

You can check and test API with Swagger - it's on main address - `127.0.0.1:8000`

At the begin we should add our Flyps settings to the database, so we can use `/update-config/` endpoint to do that: 
"flyps_login" and "flyps_password" should be filled with Flyps test account credentials.
Now we can define contacts, segments and email templates. 

There is a many-to-one relationship between contacts and segments. 
To assign contact to segment, we have to give segment primary key value to 
"segment" field in contact, using POST, PUT or PATCH method.

To send emails to specified contact or to all contacts in segment, we use `/send-emails/` endpoint.
It's forbidden to specify both contact and segment primary keys, but it's necessary to specify one of them. 

## License
[MIT](https://choosealicense.com/licenses/mit/)