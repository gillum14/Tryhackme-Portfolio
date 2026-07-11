HTTP in Detail

Learning Objectives:
~ Understand the purpose of HTTP and HTTPS.
~ Learn the structure of a URL.
~ Identify common HTTP methods, status codes, headers, and cookies.
~ Practice analyzing HTTP requests and responses.

Notes:
- **HTTP (HyperText Transfer Protocol)** is the protocol used to transfer web content such as HTML, images, videos, and other resources.
- **HTTPS** is the secure version of HTTP, encrypting data and verifying the identity of the web server.
- A **URL (Uniform Resource Locator)** identifies a web resource and typically includes:
  - **Scheme:** HTTP or HTTPS
  - **Host:** Domain name or IP address
  - **Port:** Default 80 (HTTP) or 443 (HTTPS)
  - **Path:** Resource location
  - **Query String:** Sends additional parameters
  - **Fragment:** Links to a specific section of a webpage
- HTTP follows a **request-response** model:
  - Client sends a request.
  - Server returns a response with a status code and requested data.
- **Common HTTP Methods:**
  - **GET** – Retrieve data
  - **POST** – Submit new data
  - **PUT** – Update existing data
  - **DELETE** – Remove data
- **HTTP Status Code Categories:**
  - **1xx** – Informational
  - **2xx** – Success (200 OK, 201 Created)
  - **3xx** – Redirection
  - **4xx** – Client errors (400, 401, 403, 404)
  - **5xx** – Server errors (500, 503)
- **Common Headers:**
  - **Request:** Host, User-Agent, Content-Length, Cookie
  - **Response:** Content-Type, Set-Cookie, Cache-Control, Content-Encoding
- **Cookies** store small pieces of data that allow websites to remember users, maintain sessions, and save preferences.

** Complede a lab using the HTTP request emulator to inspect requests and responses, identify HTTP methods, status codes, headers, and observe how cookies are used during web communication.

Conclusion:
HTTP enables communication between web browsers and servers, while HTTPS secures that communication through encryption. Understanding URLs, requests, responses, methods, headers, status codes, and cookies is fundamental for analyzing web traffic and identifying web-based security issues.
