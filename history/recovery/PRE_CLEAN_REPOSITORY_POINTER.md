# Pre-clean repository pointer

Repository cleanup intentionally removed migration-era full-text mirrors, migration checkpoints, R2 snapshot copies and migration metadata from the active `main` branch so they cannot pollute normal GitHub search/recovery.

They remain recoverable from Git history.

## Recovery commits

- `5c83f82da95d42efa33cbf2192c95545ab009017`
  - last useful migration-era working tree before temporary reorganization markers;
  - contains the old `sources_text/`, `checkpoints/`, `snapshots/`, migration metadata and pre-clean directory layout.

- `41fc94aea846f05ed98d7099703ec49c9356cf9e`
  - staging tree immediately before the atomic repository reorganization.

## Rule

If an old migration/full-text asset is ever required, read it directly from one of these commits or restore only the needed excerpt. Do **not** merge the old repository layout wholesale back into `main`.
