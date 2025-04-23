import json
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import (
    test_users, test_teams, test_activities, test_leaderboard, test_workouts
)

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Insert test data into collections
        db["users"].insert_many(test_users)
        db["teams"].insert_many(test_teams)
        db["activity"].insert_many(test_activities)
        db["leaderboard"].insert_many(test_leaderboard)
        db["workouts"].insert_many(test_workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
