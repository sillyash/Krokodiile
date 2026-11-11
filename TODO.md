# TODO

## Tooling

justfile
- [x] setup
- [x] web-setup
- [x] api-setup

pre-commit
- [x] api
  - [x] ruff lint + format
  - [x] uv lock
  - [x] django check + migrations
- [x] web
  - [x] lint + format + type-check
- [x] general
  - [x] bump version (`just bump`)
  - [x] deploy (push w/ tags) (`just deploy`)


## Web

### Squelette

- [ ] deps + filesystem
- [x] routing
- [x] header
- [x] footer
- [x] css base
  - [x] theme
  - [x] footer/header/main spacing
  - [x] dark mode

## API


### Setup

- [x] settings
- [x] deps (REST Framework + CORS)
- [x] livre d'or (POST only)
- [x] dates de soirees (GET only)
- [x] admin dashboard

### Deploiement

- [x] gunicorn + settings prod (proxy HTTPS, `FIIREFLY_STATIC_ROOT`)
- [x] homelab : systemd + nginx + deploy.sh (`services/fiirefly/`)
- [ ] cert + route Cloudflare Tunnel `fiirefly-api.sillyash.com`
- [ ] redirect URI Arise Connect en prod
