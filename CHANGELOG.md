# Change Log

## [Unreleased]

### Changes
- Updated for SlyAPI 0.4
- Awaiting `YouTubeAnalytics` is not longer necessary
- Methods now take `T|set[T]` for enum parameters
- `Dimensions` and `Metrics` are now just plain enums
    - the `+` operator has been overloaded to make a `set`