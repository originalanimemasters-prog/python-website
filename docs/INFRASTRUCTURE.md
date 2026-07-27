# DevForge Infrastructure

> This document tracks all services used in DevForge and future upgrade plans.

---

# Database

Current
- PostgreSQL (Supabase Free)

Upgrade
- Supabase Pro / Managed PostgreSQL

Reason
- More storage
- Better backups
- Higher limits

Status
- ⏳ Planned

---

# Backend Hosting

Current
- Render Free

Upgrade
- Render Starter

Reason
- No cold starts
- Better performance

Status
- ⏳ Planned

---

# Frontend Hosting

Current
- Vercel Free

Upgrade
- Vercel Pro

Reason
- Better bandwidth
- Analytics

Status
- ⏳ Planned

---

# Emails

Current
- Brevo Free

Upgrade
- Brevo Starter

Reason
- Higher daily email limit

Status
- ⏳ Planned

---

# Static Files

Current
- WhiteNoise

Upgrade
- Cloudflare R2

Reason
- Faster delivery
- Cheaper storage

Status
- ⏳ Planned

---

# Media Files

Current
- Local Storage

Upgrade
- Cloudflare R2

Reason
- Unlimited scalable storage

Status
- ⏳ Planned

---

# Cache

Current
- None

Upgrade
- Redis (Upstash)

Reason
- Faster APIs
- Session cache

Status
- ⏳ Planned

---

# Monitoring

Current
- Django Logs

Upgrade
- Sentry

Reason
- Error tracking

Status
- ⏳ Planned

---

# Judge Engine

Current
- Local Docker

Upgrade
- Dedicated VPS

Reason
- Better isolation
- More concurrent submissions

Status
- ⏳ Planned

---

# Domain

Current
- Render/Vercel Subdomain

Upgrade
- devforge.com

Status
- ⏳ Planned

---

# SSL

Current
- Free SSL

Upgrade
- Managed SSL

Status
- ✅ Free SSL is sufficient

---

# CDN

Current
- None

Upgrade
- Cloudflare CDN

Status
- ⏳ Planned

---

# Cost Policy

Rule:

- Until DevForge generates revenue:
    - Only Free Tier services
    - Prefer Open Source software
    - Avoid paid subscriptions

- After stable revenue:
    - Upgrade infrastructure gradually
    - Keep migration without rewriting code
