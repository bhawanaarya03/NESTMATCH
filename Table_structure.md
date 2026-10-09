# NestMatch — Database Table Structures

## 1. PG Listings

The `pg_listings` table stores details of available PG accommodations, helping students find suitable options based on their preferences.

**Key Attributes:**
- `id` – Unique ID (Primary Key)
- `title` – PG name
- `area` and `location` – Location details
- `rent` – Monthly rent
- `distance_km` – Distance in kilometres
- `pg_type` and `room_type` – Accommodation categories
- `facilities`, `rating`, `description` – PG details

This table supports PG searching and filtering based on budget, location, room type, and facilities.

### Table Structure

![PG Listings Table Structure](pg_listings.png)

## 2. Visit Requests

![Visit Requests](visit_requests.png)
