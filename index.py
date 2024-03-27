from os import environ
import json
import redis
import random


# Function to generate a random number
def generate_random_number():
    return random.randint(1, 100)


# Main function executed by Appwrite
def main(context):
    r = redis.Redis(host=environ.get("HOST"), port=environ.get("PORT"), password=environ.get("PASSWORD"), decode_responses=True)

    # Get the file id
    file_id = json.loads(context.req.body_raw["$id"])

    # Generate a random number
    random_number = generate_random_number()

    # Set the file ID and random number in Redis
    r.set(file_id, random_number)
