# tools/dns_diag.py
import sys
import dns.resolver

def run_dns_checks(domain):
    record_types = ['A', 'CNAME', 'MX', 'TXT']
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            print(f"\n{rtype} Records:")
            for rdata in answers:
                print(f"  {rdata}")
        except Exception as e:
            print(f"{rtype} lookup failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dns_diag.py <domain>")
        sys.exit(1)
    run_dns_checks(sys.argv[1])