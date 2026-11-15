from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 3655

server = ThreadingHTTPServer(
    (HOST, PORT),
    SimpleHTTPRequestHandler
)

print("===================================")
print("       XDL OS UPDATE SERVER")
print("===================================")
print(f"Server running at http://{HOST}:{PORT}")
print("Press CTRL+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nXDL server shutting down...")
    server.server_close()
