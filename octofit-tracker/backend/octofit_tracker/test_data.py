# Test data for the Octofit Tracker app

test_users = [
    {"email": "john.doe@example.com", "name": "John Doe", "age": 25, "team": "Team A"},
    {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30, "team": "Team B"},
]

test_teams = [
    {"name": "Team A", "members": ["john.doe@example.com"]},
    {"name": "Team B", "members": ["jane.smith@example.com"]},
]

test_activities = [
    {"user": "john.doe@example.com", "activity": "Running", "duration": 30},
    {"user": "jane.smith@example.com", "activity": "Cycling", "duration": 45},
]

test_leaderboard = [
    {"user": "jane.smith@example.com", "score": 100},
    {"user": "john.doe@example.com", "score": 80},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick morning run to start the day", "duration": 30},
    {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 45},
]
