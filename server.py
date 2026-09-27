
from http.server import HTTPServer, BaseHTTPRequestHandler
import platform
import socket

class LaptopHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            hostname = socket.gethostname()
            processor = platform.processor()
            system = platform.system()
            version = platform.version()
            architecture = platform.machine()
            python_version = platform.python_version()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Laptop Specifications</title>
                <style>
                    body {{
                        font-family: Arial;
                        background-color: #eef2f7;
                        text-align: center;
                        padding: 30px;
                    }}
                    h1 {{ color: navy; }}
                    table {{
                        margin: auto;
                        border-collapse: collapse;
                        width: 80%;
                        background: white;
                    }}
                    th, td {{
                        border: 1px solid black;
                        padding: 12px;
                    }}
                    th {{ background-color: lightblue; }}
                </style>
            </head>
            <body>
                <h1>Laptop Device Specifications</h1>
                <h3>Name: Harish S</h3>
                <h3>Register Number: 26018137 </h3>

                <table>
                    <tr>
                        <th>Specification</th>
                        <th>Details</th>
                    </tr>
                    <tr>
                        <td>Computer Name</td>
                        <td>{hostname}</td>
                    </tr>
                    <tr>
                        <td>Operating System</td>
                        <td>{system}</td>
                    </tr>
                    <tr>
                        <td>OS Version</td>
                        <td>{version}</td>
                    </tr>
                    <tr>
                        <td>Processor</td>
                        <td>{processor or "Not available"}</td>
                    </tr>
                    <tr>
                        <td>Architecture</td>
                        <td>{architecture}</td>
                    </tr>
                    <tr>
                        <td>Python Version</td>
                        <td>{python_version}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header(
                "Content-type", "text/html; charset=utf-8"
            )
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        else:
            self.send_error(404, "Page Not Found")


server = HTTPServer(("127.0.0.1", 8000), LaptopHandler)

print("Server is running at http://127.0.0.1:8000")

server.serve_forever()
