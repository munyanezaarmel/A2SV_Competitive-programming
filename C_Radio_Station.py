# Read inputs
n, m = map(int, input().split())

# Dictionary to store mappings of IPs to names
ip_to_name = {}

# Read server details and populate dictionary
for _ in range(n):
    name, ip = input().split()
    ip_to_name[ip] = name

# Process and print the commands with server names as comments
for _ in range(m):
    command, ip = input().split()
    print(f"{command} {ip}; #{ip_to_name[ip]}")
