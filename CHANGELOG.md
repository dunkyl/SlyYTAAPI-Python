# Change Log

## [Unreleased]

---

## [0.2.0] - 2023-03-01

### Added
- `QueryResult.columnHeaders` now has a corresponding `TypedDict` for `ColumnHeader`.
    - Acts the same as before but can have better feedback for things like linters.
- Type annotation for the scalar values in `QueryResult.rows`

### Changes
- Updated for SlyAPI 0.4.3
- Awaiting `YouTubeAnalytics` is no longer necessary
- Passing scopes to `YouTubeAnalytics` is no longer necessary
- Methods now take `T|set[T]` for enum parameters
- `Dimensions` and `Metrics` are now just plain enums
    - the `+` operator has been overloaded to make a `set`, so they can be used like before.

## [0.1.0] - 2022-02-26

Initial release.