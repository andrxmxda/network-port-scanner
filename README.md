#  CyberScan: Full-Stack Asynchronous Network Port Scanner

CyberScan is a modern, multi-tier network security application that transitions a low-level command-line utility into a scalable web application. Built with a high-performance Python FastAPI backend and a sleek, custom-designed JavaScript frontend dashboard, it enables users to securely audit network targets for open TCP ports in real-time.

---

##  Features

* **Multi-Tier Architecture:** Complete decoupling of the backend data engine from the presentation layer.
* **Low-Level Socket Auditing:** Uses Python's native `socket` library to programmatically initiate TCP handshakes and determine port availability.
* **Asynchronous Web API:** Exposes lightweight REST endpoints managed by FastAPI with custom CORS configuration for secure cross-origin data fetching.
* **Premium Cyber-Aesthetic UI:** A responsive, glassmorphic client-side dashboard featuring soft pastel gradients, neon accents, and interactive state management.

---

##  Tech Stack

* **Backend:** Python 3, FastAPI, Uvicorn, Native Socket Programming
* **Frontend:** HTML5, CSS3 (Custom Glassmorphism & Animations), JavaScript (ES6+ Async/Fetch API)
* **DevOps/Workflow:** Linux, Git/GitHub, GitHub Codespaces

---

##  How It Works

[ Frontend Dashboard ]
(HTML5/CSS3/JS Fetch)
│
▼  HTTP GET Request
[ FastAPI Backend API ]
(main.py)
│
▼  TCP Connect Handshake
[ Target Network Host ]


1. **Client Request:** The user inputs a target host (e.g., `8.8.8.8`) and a specific port range via the dashboard.
2. **API Processing:** The frontend dispatches an asynchronous network fetch request to the FastAPI layer.
3. **Network Audit:** The backend executes non-blocking socket checks across the chosen ports, cataloging successful connections.
4. **Dynamic Update:** The API returns a structured JSON payload, prompting the frontend to instantly display live findings without page refreshes.

---

##  Local Setup & Deployment

Clone the repository to your local development workspace or spin it up inside a cloud container environment:

```bash
git clone [https://github.com/andrxmxda/network-port-scanner.git](https://github.com/andrxmxda/network-port-scanner.git)
cd network-port-scanner
1. Start the Backend API
Install the required dependencies and start the development server using Uvicorn:

Bash
pip install fastapi uvicorn
uvicorn main:app --reload
The API engine will initialize and begin listening for requests on http://127.0.0.1:8000.

2. Launch the Frontend UI
In a separate terminal directory window, launch a local HTTP routing server to view the interface:

Bash
python3 -m http.server 8080
Open your browser and navigate to http://127.0.0.1:8080 to access the live dashboard.

