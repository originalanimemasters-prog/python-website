# DevForge — Developer Platform Architecture

*A unified platform combining coding practice, backend challenges, an online judge, project/snippet sharing, technical blogging, community, and contests — designed to scale to millions of developers.*

---

## 1. Complete Folder Structure

```
devforge/
├── backend/
│   ├── config/                     # Django settings (base/dev/prod/test), urls, wsgi, asgi
│   ├── apps/
│   │   ├── accounts/                # auth, users, roles, OAuth
│   │   ├── problems/                 # coding practice problems
│   │   ├── submissions/              # code submissions, results
│   │   ├── judge/                    # judge orchestration (dispatch to workers)
│   │   ├── challenges/                # backend challenges (SQL/Docker/Git/etc.)
│   │   ├── snippets/
│   │   ├── projects/
│   │   ├── blogs/
│   │   ├── community/                # follows, feed, discussions, mentions
│   │   ├── contests/
│   │   ├── interview_prep/
│   │   ├── profiles/
│   │   ├── notifications/
│   │   ├── search/
│   │   ├── admin_panel/
│   │   ├── monetization/
│   │   └── common/                   # shared mixins, permissions, pagination
│   ├── workers/
│   │   ├── judge_worker/             # per-language execution runners
│   │   └── celery_tasks/
│   ├── tests/
│   ├── manage.py
│   └── requirements/
├── frontend/
│   ├── src/
│   │   ├── app/                      # routing, layout shells
│   │   ├── features/                 # one folder per module, mirrors backend apps
│   │   ├── components/               # shared UI components
│   │   ├── hooks/
│   │   ├── services/                 # API clients (axios/fetch wrappers)
│   │   ├── store/                    # state management
│   │   ├── types/
│   │   ├── utils/
│   │   └── styles/
│   ├── public/
│   └── package.json
├── judge-engine/
│   ├── docker-images/
│   │   ├── python-runner/
│   │   ├── java-runner/
│   │   ├── cpp-runner/
│   │   └── javascript-runner/
│   ├── isolate-configs/              # sandbox/cgroup configs
│   └── orchestrator/                 # queue consumer, container lifecycle
├── infra/
│   ├── docker/                       # docker-compose files per env
│   ├── nginx/
│   ├── terraform/                    # (future AWS)
│   └── ci-cd/                        # GitHub Actions workflows
├── docs/
└── scripts/
```

---

## 2. System Architecture (High Level)

```
                    ┌─────────────┐
                    │   Clients   │  (Web / Mobile browsers)
                    └──────┬──────┘
                           │ HTTPS
                    ┌──────▼──────┐
                    │    Nginx     │  (reverse proxy, TLS, static/media)
                    └──────┬──────┘
              ┌────────────┼────────────┐
       ┌──────▼─────┐ ┌────▼─────┐ ┌────▼──────┐
       │  Django API │ │ WebSocket │ │  Static    │
       │  (DRF, JWT)  │ │  Server   │ │  (React)   │
       └──────┬───────┘ └────┬──────┘ └────────────┘
              │              │
   ┌──────────┼──────────────┼───────────────┐
   │          │              │                │
┌──▼───┐  ┌───▼────┐   ┌─────▼─────┐   ┌──────▼─────┐
│Postgres│ │ Redis  │   │  Celery   │   │Elasticsearch│
│ (RDS)  │ │(cache/ │   │ (workers) │   │  (search)   │
│        │ │ broker)│   │           │   └─────────────┘
└────────┘ └───┬────┘   └─────┬─────┘
                │              │
        ┌───────▼──────┐ ┌─────▼──────────┐
        │ Judge Queue   │ │  S3 Storage     │
        │ (Redis/RabbitMQ)│ (images, files)│
        └───────┬───────┘ └────────────────┘
                │
        ┌───────▼────────────────────┐
        │  Judge Worker Pool          │
        │  (isolated Docker containers│
        │   per language, per submit) │
        └─────────────────────────────┘
```

Key principle: the **web API tier never executes user code directly**. It only enqueues a job; isolated worker containers do the execution and report results back asynchronously.

---

## 3. Database Schema (Core Tables, Condensed)

**accounts_user**: id, email, username, password_hash, role (user/mod/admin), is_verified, oauth_provider, created_at

**profiles_profile**: id, user_id (FK), bio, skills[], github_url, avatar, contest_rating, badge_ids[]

**problems_problem**: id, title, slug, difficulty, tags[], category_id, description_md, constraints, created_by, is_published

**problems_testcase**: id, problem_id (FK), input, expected_output, is_sample, weight

**submissions_submission**: id, user_id (FK), problem_id (FK), language, source_code_ref (S3), status, runtime_ms, memory_kb, submitted_at

**challenges_challenge**: id, type (sql/docker/git/linux/api/...), title, scenario_md, setup_script_ref, evaluation_script_ref, difficulty

**snippets_snippet**: id, user_id, title, language, content, tags[], forked_from_id (nullable), likes_count

**projects_project**: id, user_id, title, readme_md, github_url, demo_url, tech_stack[], stars_count

**blogs_post**: id, author_id, title, slug, content_md, reading_time, published_at, seo_meta

**community_follow**: follower_id, following_id, created_at

**contests_contest**: id, title, type (weekly/monthly/college), start_time, end_time, problem_ids[]

**contests_leaderboard_entry**: contest_id, user_id, score, rank, penalty_time

**notifications_notification**: id, user_id, type, payload_json, is_read, created_at

Indexes: composite indexes on (user_id, created_at) for feeds; (problem_id, status) for submissions; GIN indexes on tags[] and skills[] (Postgres arrays/JSONB); full-text search vectors on blogs/problems for fallback when Elasticsearch is degraded.

---

## 4. ER Diagram (Textual)

```
User 1───1 Profile
User 1───* Submission *───1 Problem
Problem 1───* TestCase
User 1───* Snippet
Snippet *───1 Snippet (self-ref: forked_from)
User 1───* Project
User 1───* BlogPost
User *───* User (via Follow: follower/following)
Contest *───* Problem (via ContestProblem)
Contest 1───* LeaderboardEntry *───1 User
User 1───* Notification
Challenge 1───* ChallengeAttempt *───1 User
```

---

## 5. Microservice Architecture (Future-Ready)

Start as a **modular monolith** (Django apps as bounded contexts) for MVP speed, with clear seams to extract later:

| Future Service | Extracted From | Why Split Later |
|---|---|---|
| Judge Service | judge + submissions | CPU/security isolation, independent scaling |
| Search Service | search app | Elasticsearch-heavy, different scaling curve |
| Notification Service | notifications | High fan-out, WebSocket-heavy |
| Contest Service | contests | Bursty traffic during live contests |
| Media Service | S3 upload handling | Bandwidth-heavy, separate CDN needs |

Communication between future services: REST/gRPC for sync calls, Redis Streams/Kafka for async events (submission.completed, user.followed, contest.started).

---

## 6. API Structure (REST, versioned)

```
/api/v1/auth/{register,login,refresh,verify-email,forgot-password,google}
/api/v1/users/{id}, /api/v1/users/{id}/profile
/api/v1/problems/, /api/v1/problems/{slug}
/api/v1/problems/{slug}/run
/api/v1/problems/{slug}/submit
/api/v1/submissions/{id}
/api/v1/challenges/{type}/
/api/v1/snippets/
/api/v1/projects/
/api/v1/blogs/
/api/v1/contests/, /api/v1/contests/{id}/leaderboard
/api/v1/community/feed, /api/v1/community/follow/{user_id}
/api/v1/notifications/
/api/v1/search?q=&type=
/api/v1/admin/...
```

All list endpoints: cursor-based pagination (not offset) for scale.

---

## 7. Django App Structure (per app pattern)

```
apps/problems/
├── models.py
├── serializers.py
├── views.py / viewsets.py
├── urls.py
├── permissions.py
├── services.py       # business logic, kept out of views
├── selectors.py       # read/query logic, kept out of models
├── tasks.py            # Celery tasks
├── admin.py
├── tests/
└── migrations/
```

Convention: **views stay thin**; logic lives in `services.py` (writes) and `selectors.py` (reads) — this keeps the codebase testable and ready for service extraction later.

---

## 8. Frontend Folder Structure

```
src/features/problems/
├── api/                # RTK Query or React Query hooks
├── components/          # ProblemList, ProblemEditor, TestCasePanel
├── pages/
├── types.ts
└── slice.ts (or store hooks)
```

Code editor: Monaco Editor with per-language config. Shared `CodeRunner` component reused across Problems, Challenges, and Snippet preview.

---

## 9. Online Judge Architecture

```
Submit → API validates & stores source → enqueue Job(problem_id, lang, code) → Redis/RabbitMQ queue
   → Worker picks job → spins ephemeral Docker container (pre-warmed pool) → 
   → mounts code read-only, no network, non-root user →
   → runs against test cases with rlimits → captures stdout/stderr/exit code/time/memory →
   → writes verdict to DB → publishes result via WebSocket to user
```

**Isolation controls per execution:**
- No network access (`--network none`)
- Read-only root filesystem, writable `/tmp` only, size-capped
- CPU limit (`--cpus`), memory limit (`--memory`, `--memory-swap` disabled)
- Wall-clock + CPU time limit enforced by both container `timeout` and a watchdog process
- Non-root user, dropped Linux capabilities, seccomp profile blocking dangerous syscalls
- Process/thread count limit (`--pids-limit`) to block fork bombs
- Disk write quota
- Containers destroyed immediately after run (never reused across submissions)

**Dangerous code prevention:** static pre-checks (blocklist of obviously malicious patterns as a fast first filter) + the above runtime sandboxing as the real defense — never rely on static analysis alone.

---

## 10. Docker Architecture

- One minimal base image per language (`python-runner`, `java-runner`, `cpp-runner`, `javascript-runner`), each with only the compiler/interpreter + stdlib.
- Multi-stage builds: compile stage separate from a slim runtime stage.
- A **warm pool** of pre-started containers per language to avoid cold-start latency; orchestrator recycles/replaces after each job.
- Image versions pinned and rebuilt on a schedule for security patches.
- Separate Docker network segment for judge workers, isolated from the main app network.

---

## 11. Redis Architecture

| Use Case | Redis Feature |
|---|---|
| Session/JWT blacklist | String keys with TTL |
| Rate limiting | Sorted sets / token bucket via Lua scripts |
| Judge job queue | Lists or Streams (Streams preferred for consumer groups + replay) |
| Celery broker | Standard Redis broker |
| Caching (problem lists, profiles, leaderboards) | Read-through cache, TTL + explicit invalidation on write |
| Live contest leaderboard | Sorted sets (ZADD score, ZRANGE for rank) — O(log N) updates |
| Pub/Sub for WebSocket fan-out | Redis Pub/Sub or Streams behind Django Channels |

---

## 12. Celery Workflow

```
submission.created (task) → dispatch to judge queue → 
judge.result_ready (task) → update Submission row → 
                            → recompute user stats → 
                            → trigger notification.create →
                            → invalidate profile cache
```

Separate Celery queues by priority: `judge_high` (interactive Run), `judge_normal` (Submit), `default` (emails, digests), `low` (analytics rollups). Beat schedule handles: contest start/end triggers, daily digest emails, leaderboard snapshotting, stale-data cleanup.

---

## 13. Development Roadmap (Phased)

**Phase 0 (Weeks 1–3):** Auth, user model, base infra, CI/CD skeleton, Docker Compose local env.
**Phase 1 — MVP core (Weeks 4–10):** Problems + Online Judge (Python & JS only), Submissions, basic Profile.
**Phase 2 (Weeks 11–15):** Snippet Hub, Projects module, Search (Postgres full-text first).
**Phase 3 (Weeks 16–20):** Blogs, Community (follow/feed/notifications), remaining languages (Java, C++).
**Phase 4 (Weeks 21–25):** Contests + leaderboard, Backend Challenges module.
**Phase 5 (Weeks 26–30):** Interview Prep, Admin Panel, Elasticsearch migration, Monetization.
**Phase 6 (ongoing):** Microservice extraction, AWS migration, mobile apps, advanced analytics.

---

## 14. MVP Features

- Auth (email/password + Google OAuth)
- Problems + Run/Submit (Python, JavaScript only)
- Basic public profile
- Snippet Hub (create, view, like)
- Basic search (Postgres full-text)
- Notifications (in-app only, no realtime yet)

## 15. Future Features

- Full 4-language judge, mock interviews, college contests, sponsored challenges, resume review, mobile apps, AI-assisted hints/editorials, plagiarism detection on submissions, team-based contests.

---

## 16. Scaling Strategy

- **Stateless API pods** behind a load balancer → horizontal autoscaling on CPU/RPS.
- **Read replicas** for Postgres; route heavy read endpoints (profiles, leaderboards, problem lists) to replicas.
- **Judge workers autoscale independently** based on queue depth (this is the most spiky component — contests cause 10–50x load).
- **CDN** in front of static assets, blog images, avatars.
- **Cache-aside** heavily on profiles, problem metadata, leaderboards.
- Database sharding/partitioning considered later for `submissions` table (partition by month) once volume is high.
- Move from single Redis instance → Redis Cluster once cache/queue throughput demands it.

---

## 17. Database Indexing Strategy

- B-tree indexes on all FKs and frequently filtered columns (`status`, `difficulty`, `language`, `is_published`).
- Composite index `(user_id, created_at DESC)` for feed/profile queries.
- Composite index `(problem_id, status)` for submission stats/acceptance rate.
- GIN index on `tags` array columns and on `description_md` (full-text `tsvector`) as fallback search.
- Partial index on `submissions(status) WHERE status = 'pending'` to keep judge polling fast.
- Regularly review with `pg_stat_statements` / `EXPLAIN ANALYZE` as data grows; avoid over-indexing write-heavy tables (submissions).

---

## 18. Caching Strategy

| Data | Strategy | TTL |
|---|---|---|
| Problem detail/list | Read-through cache | 10 min, invalidate on edit |
| User profile | Read-through cache | 5 min, invalidate on write |
| Leaderboard (contest) | Redis sorted set (source of truth during contest) | live |
| Search results | Short TTL cache for popular queries | 2 min |
| Session/JWT validation | In-memory + Redis blacklist check | token lifetime |

Avoid caching submission results (must be fresh); cache aggregates (acceptance rate, solved count) instead, recomputed async.

---

## 19. Security Architecture

- **Rate limiting**: per-IP and per-user, stricter on auth and code-execution endpoints (Redis token bucket via Nginx + DRF throttling).
- **CSRF**: Django's CSRF middleware for cookie-based flows; SPA uses JWT in Authorization header (not cookies) to sidestep most CSRF surface, with SameSite cookie protections for refresh tokens.
- **XSS**: sanitize all Markdown output (blogs, problem descriptions, comments) server-side before render; CSP headers.
- **SQL Injection**: ORM-only queries, no raw SQL string interpolation.
- **Docker sandboxing**: as detailed in §9 — the core security boundary for arbitrary code execution.
- **JWT security**: short-lived access tokens, rotating refresh tokens, revocation list in Redis.
- **Password hashing**: Argon2 or bcrypt via Django's password hashers.
- **RBAC**: role checks enforced at the permission-class level in DRF, never just in the frontend.
- **Audit logs**: append-only log of admin/moderator actions.
- **File validation**: strict MIME/type/size checks and virus scanning on any uploaded file (avatars, project screenshots, Dockerfiles in Snippet Hub — these are never executed, only displayed).

---

## 20. Deployment Architecture

**Initial (Render):**
```
Render Web Service (Django+Gunicorn) → Render Postgres → Render Redis
Render Background Worker (Celery) → same Redis broker
Static frontend → Render Static Site or Vercel
Judge workers → separate Render worker service (Docker-in-Docker or a small dedicated VM, since sandboxed execution needs more control than typical PaaS containers offer)
```

**Later (AWS):**
```
ECS/EKS for API + Celery workers (autoscaling groups)
RDS Postgres (Multi-AZ, read replicas)
ElastiCache Redis (cluster mode)
S3 + CloudFront for static/media
Dedicated EC2/Fargate pool with gVisor or Firecracker microVMs for judge workers (stronger isolation than plain Docker at scale)
ALB + WAF in front of everything
Terraform for all infra as code
GitHub Actions → build → push to ECR → deploy
```

---

## Notes on Sequencing

The riskiest, most architecture-defining piece is the **Online Judge** — build and harden that first against real adversarial code before layering on the social/content features, since a sandbox escape is a far worse failure mode than a missing feature.
