CREATE TABLE ocr_result (
    id SERIAL PRIMARY KEY,
    file_path VARCHAR(255) NOT NULL,
    extracted_text TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);