CREATE DATABASE IF NOT EXISTS nestmatch CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE nestmatch;

-- Account table is needed for real login/create-account functionality.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(190) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Required table 1: PG details
CREATE TABLE IF NOT EXISTS pg_listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL,
    location VARCHAR(150) NOT NULL,
    rent INT NOT NULL,
    distance_km DECIMAL(5,2) NOT NULL DEFAULT 0,
    pg_type ENUM('Girls','Boys','Co-living') NOT NULL,
    room_type ENUM('Single','Double','Triple') NOT NULL,
    facilities VARCHAR(500) NOT NULL,
    rating DECIMAL(2,1) NOT NULL DEFAULT 0,
    description TEXT,
    image_url VARCHAR(500),
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Required table 2: Visit requests. FIFO order is created_at, then id.
CREATE TABLE IF NOT EXISTS visit_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(190) NOT NULL,
    pg_id INT NOT NULL,
    preferred_date DATE NOT NULL,
    status ENUM('Pending','Confirmed','Completed','Cancelled') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_visit_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_visit_pg FOREIGN KEY (pg_id) REFERENCES pg_listings(id) ON DELETE CASCADE
);

INSERT INTO pg_listings
(title, area, location, rent, distance_km, pg_type, room_type, facilities, rating, description, image_url, featured)
SELECT * FROM (
    SELECT 'Olive House', 'Knowledge Park', 'Greater Noida', 8500, 1.2, 'Girls', 'Double',
    'Wi-Fi, Meals, Laundry, Security', 4.8, 'Warm, furnished rooms with a quiet study corner.',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=900&q=80', TRUE
    UNION ALL SELECT 'Nook Residence', 'Pari Chowk', 'Greater Noida', 10500, 2.1, 'Girls', 'Single',
    'Wi-Fi, Meals, AC, Security', 4.7, 'Private rooms with study desks and natural light.',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=900&q=80', TRUE
    UNION ALL SELECT 'Maple Nest', 'Knowledge Park', 'Greater Noida', 7200, 0.8, 'Co-living', 'Triple',
    'Wi-Fi, Meals, Security', 4.5, 'Budget-friendly student stay close to campus.',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=900&q=80', FALSE
    UNION ALL SELECT 'Study Loft', 'Alpha 1', 'Greater Noida', 9200, 3.4, 'Boys', 'Double',
    'Wi-Fi, AC, Laundry, Security', 4.4, 'Comfortable rooms with practical amenities.',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80', FALSE
    UNION ALL SELECT 'Cedar Court', 'Pari Chowk', 'Greater Noida', 11800, 2.5, 'Girls', 'Single',
    'Wi-Fi, Meals, AC, Laundry, Security', 4.9, 'Premium furnished rooms and a peaceful atmosphere.',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=80', TRUE
    UNION ALL SELECT 'Campus Corner', 'Knowledge Park', 'Greater Noida', 6500, 1.6, 'Co-living', 'Double',
    'Wi-Fi, Meals', 4.2, 'A simple affordable option for students.',
    'https://images.unsplash.com/photo-1560185008-b033106af5c3?auto=format&fit=crop&w=900&q=80', FALSE
) AS sample
WHERE NOT EXISTS (SELECT 1 FROM pg_listings LIMIT 1);
