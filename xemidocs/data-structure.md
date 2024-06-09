### Database Schema Documentation

This document outlines the structure of the database designed for a job search website. The schema is built using MongoDB and follows best practices to ensure scalability, performance, and ease of use.

#### USERS Collection

**Purpose:** Stores information about the users who register on the website.

**Fields:**
- `_id`: ObjectId - Primary Key (PK).
- `username`: String - Unique identifier for the user.
- `password`: String - Encrypted password for user authentication.
- `profile`: Object - Contains detailed user information:
  - `name`: String - User's first name.
  - `surname`: String - User's last name.
  - `date_of_birth`: Date - User's birth date.
  - `location`: String - User's city or region.
  - `address`: String - User's street address.
  - `email`: String - User's email address.
  - `website`: String - User's personal or professional website.
  - `education`: Array of Objects - List of educational qualifications:
    - `institution`: String - Name of the educational institution.
    - `degree`: String - Degree or qualification obtained.
    - `start_date`: Date - Start date of the education.
    - `end_date`: Date - End date of the education.
  - `experience`: Array of Objects - List of professional experiences:
    - `company`: String - Name of the company.
    - `title`: String - Job title.
    - `start_date`: Date - Start date of the job.
    - `end_date`: Date - End date of the job.
    - `description`: String - Description of the job responsibilities.
- `created_on`: Date - Timestamp of when the user account was created.
- `last_session`: Date - Timestamp of the user's last login.

**Reasoning:** 
- Utilises subdocuments (`profile`) to logically group related information, making data retrieval efficient.
- Arrays for `education` and `experience` allow for flexible and scalable storage of multiple entries.
- Clear separation of sensitive information (e.g., password) and profile details ensures better security and organisation.

#### COMPANIES Collection

**Purpose:** Stores information about the companies that register on the website to post job listings.

**Fields:**
- `_id`: ObjectId - Primary Key (PK).
- `username`: String - Unique identifier for the company.
- `password`: String - Encrypted password for company authentication.
- `profile`: Object - Contains detailed company information:
  - `company_name`: String - Name of the company.
  - `since`: Date - Date when the company was established.
  - `location`: String - Company's city or region.
  - `address`: String - Company's street address.
  - `email`: String - Company's email address.
  - `website`: String - Company's official website.
- `created_on`: Date - Timestamp of when the company account was created.
- `last_session`: Date - Timestamp of the company's last login.

**Reasoning:**
- Similar to the `USERS` collection, subdocuments are used to group related information logically.
- Ensures separation of authentication data and profile details for better security and organisation.

#### JOBS Collection

**Purpose:** Stores job listings posted by companies.

**Fields:**
- `_id`: ObjectId - Primary Key (PK).
- `company_id`: ObjectId - Foreign Key (FK) referencing `_id` in the `COMPANIES` collection.
- `title`: String - Title of the advert.
- `description`: String - Brief description of the job.
- `position`: String - Position offered.
- `location`: String - Location of the job.
- `type`: { type: String, enum: ["on-site", "remote"] } - Indicates if the job is on-site or remote.
- `salary`: Number - Salary offered for the position.
- `job_info`: Object - Contains detailed job information:
  - `textual_description`: String - Detailed description of the job.
  - `requirements`: Array of Strings - List of requirements for the job.
- `published_on`: Date - Timestamp of when the job was posted.
- `finishes_on`: Date - Timestamp of when the job posting expires.

**Reasoning:**
- Links job listings to companies via `company_id`, ensuring referential integrity.
- Utilises an `enum` for `type` to enforce valid values, ensuring data consistency.
- Arrays for `requirements` allow for flexible and scalable storage of multiple entries.

#### APPLICATIONS Collection

**Purpose:** Tracks applications submitted by users for job listings.

**Fields:**
- `_id`: ObjectId - Primary Key (PK).
- `job_id`: ObjectId - Foreign Key (FK) referencing `_id` in the `JOBS` collection.
- `user_id`: ObjectId - Foreign Key (FK) referencing `_id` in the `USERS` collection.
- `applied_on`: Date - Timestamp of when the application was submitted.

**Reasoning:**
- Establishes many-to-many relationships between users and jobs through foreign keys.
- Tracks the date of application to provide a timeline of user activities and for potential analysis of application trends.

### Conclusion

This schema is designed to efficiently organise and manage data for a job search website. By leveraging MongoDB's document-oriented structure, it ensures flexibility and scalability. The use of subdocuments, arrays, and clear separation of concerns enhances data retrieval and management, ultimately providing a robust foundation for the application.