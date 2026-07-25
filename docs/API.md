// Documentation
# DevForge API Documentation

## Authentication
- JWT-based authentication
- Token refresh mechanism
- OAuth2 support (Google)

## Endpoints

### Problems
- GET /api/v1/problems/ - List all problems
- GET /api/v1/problems/{slug}/ - Get problem details
- POST /api/v1/problems/{slug}/submit/ - Submit solution

### Submissions
- GET /api/v1/submissions/ - List user submissions
- GET /api/v1/submissions/{id}/ - Get submission details

### Contests
- GET /api/v1/contests/ - List contests
- GET /api/v1/contests/{id}/leaderboard/ - Get leaderboard

### Community
- GET /api/v1/community/feed/ - Get user feed
- POST /api/v1/community/follow/{user_id}/ - Follow user

## WebSocket Events
- submission.started
- submission.completed
- contest.started
- notification.sent
