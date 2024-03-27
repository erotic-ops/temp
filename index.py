from os import environ
import json
import redis
import random


# Function to generate a random number
def generate_random_number():
    return random.randint(1, 100)


# Main function executed by Appwrite
def main(context):
    # You can log messages to the console
    context.log("Hello, Logs!")
    context.log(context.req.body_raw)  # Raw request body, contains request data
    context.log(json.dumps(context.req.body))  # Object from parsed JSON request body, otherwise string
    context.log(json.dumps(context.req.headers))  # String key-value pairs of all request headers, keys are lowercase
    context.log(context.req.scheme)  # Value of the x-forwarded-proto header, usually http or https
    context.log(context.req.method)  # Request method, such as GET, POST, PUT, DELETE, PATCH, etc.
    context.log(context.req.url)  # Full URL, for example: http://awesome.appwrite.io:8000/v1/hooks?limit=12&offset=50
    context.log(context.req.host)  # Hostname from the host header, such as awesome.appwrite.io
    context.log(context.req.port)  # Port from the host header, for example 8000
    context.log(context.req.path)  # Path part of URL, for example /v1/hooks
    context.log(context.req.query_string)  # Raw query params string. For example "limit=12&offset=50"
    context.log(json.dumps(context.req.query))  # Parsed query params. For example, req.query.limit

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # Parse the event data
    print(environ)

    r = redis.Redis(
        host=environ.get("REDIS_HOST"), port=int(environ.get("REDIS_PORT")), password=environ.get("REDIS_PASSWORD"), decode_responses=True
    )

    # Get the file id
    file_id = json.loads(context.req.body_raw)["$id"]

    # Generate a random number
    random_number = generate_random_number()

    # Set the file ID and random number in Redis
    r.set(file_id, random_number)
