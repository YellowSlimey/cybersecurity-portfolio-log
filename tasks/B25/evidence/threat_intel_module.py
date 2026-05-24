class ThreatIntelModule:
    def __init__(self):
        # Simulated threat intelligence feed (IOCs)
        self.malicious_ips = {
            "185.220.101.1",
            "45.33.32.156",
            "103.21.244.0",
            "198.98.51.101"
        }

    def check_ip(self, ip_address):
        if ip_address in self.malicious_ips:
            return f"ALERT: {ip_address} is flagged as MALICIOUS"
        else:
            return f"SAFE: {ip_address} is not in threat database"

    def batch_check(self, ip_list):
        results = []
        for ip in ip_list:
            results.append(self.check_ip(ip))
        return results


# Example usage
ti = ThreatIntelModule()

test_ips = [
    "185.220.101.1",
    "8.8.8.8",
    "1.1.1.1",
    "45.33.32.156"
]

results = ti.batch_check(test_ips)

for r in results:
    print(r)