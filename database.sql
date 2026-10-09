CREATE DATABASE IF NOT EXISTS nestmatch;
USE nestmatch;

CREATE TABLE IF NOT EXISTS pg_listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    area VARCHAR(100),
    location VARCHAR(150),
    rent INT,
    distance_km DECIMAL(5,2),
    pg_type VARCHAR(20),
    room_type VARCHAR(20),
    facilities VARCHAR(500),
    rating DECIMAL(2,1),
    description TEXT,
    featured BOOLEAN
);

CREATE TABLE IF NOT EXISTS visit_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    pg_id INT,
    preferred_date DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pg_id) REFERENCES pg_listings(id)
);

INSERT INTO pg_listings
(title, area, location, rent, distance_km, pg_type, room_type, facilities, rating, description, featured)
VALUES
('Olive House', 'Knowledge Park', 'Greater Noida', 8500, 1.2, 'Girls', 'Double', 'Wi-Fi, Meals, Laundry', 4.8, 'Furnished rooms for students', TRUE),
('Nook Residence', 'Pari Chowk', 'Greater Noida', 10500, 2.1, 'Girls', 'Single', 'Wi-Fi, Meals, AC', 4.7, 'Private rooms with study desks', TRUE),
('Maple Nest', 'Knowledge Park', 'Greater Noida', 7200, 0.8, 'Co-living', 'Triple', 'Wi-Fi, Meals, Security', 4.5, 'Budget-friendly student stay', FALSE),
('Study Loft', 'Alpha 1', 'Greater Noida', 9200, 3.4, 'Boys', 'Double', 'Wi-Fi, AC, Laundry', 4.4, 'Comfortable rooms for students', FALSE),
('Cedar Court', 'Pari Chowk', 'Greater Noida', 11800, 2.5, 'Girls', 'Single', 'Wi-Fi, Meals, AC, Security', 4.9, 'Premium furnished rooms', TRUE),
('Campus Corner', 'Knowledge Park', 'Greater Noida', 6500, 1.6, 'Co-living', 'Double', 'Wi-Fi, Meals', 4.2, 'Affordable accommodation', FALSE);
