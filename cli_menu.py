import os
import platform

def run_tool(name, command, needs_input=False, input_label="Enter input: "):
    if needs_input:
        user_input = input(f"🔹 {input_label} ").strip()
        if not user_input:
            print("Input is required. Returning to menu.")
            return
        command = f"{command} {user_input}"

    with open("cli_log.txt", "a", encoding="utf-8") as log:
        log.write(f"Running: {name} → Command: {command}\n")

    print(f"\nRunning {name}...\n")
    exit_code = os.system(command)
    if exit_code != 0:
        print(f"{name} exited with code {exit_code}")
    else:
        print(f"{name} finished successfully.")

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def main():
    tools = {
        "1": {
            "name": "DNS Diagnostic",
            "command": "python tools/dns_diag.py",
            "needs_input": True,
            "input_label": "Enter domain for DNS lookup (e.g. google.com)"
        },
        "2": {
            "name": "HTTP Status Checker",
            "command": "python tools/http_status.py",
            "needs_input": True,
            "input_label": "Enter URL to check (e.g. https://example.com)"
        },
        "3": {
            "name": "SSO Metadata Extractor",
            "command": "python tools/sso_metadata.py",
            "needs_input": True,
            "input_label": "Enter IdP metadata URL (e.g. https://idp.example.com/metadata)"
        },
        "4": {
            "name": "Ping Check",
            "command": "bash tools/ping_check.sh",
            "needs_input": True,
            "input_label": "Enter space-separated hostnames/IPs to ping (e.g. google.com github.com)"
        },

        "5": {
            "name": "Exit"
        }
    }

    while True:
        print("Cloud Support Toolkit CLI Menu\n")
        for key in sorted(tools.keys()):
            print(f"{key}. {tools[key]['name']}")

        choice = input("\nEnter your choice: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in tools:
            tool = tools[choice]
            run_tool(
                name=tool["name"],
                command=tool.get("command", ""),
                needs_input=tool.get("needs_input", False),
                input_label=tool.get("input_label", "Enter input:")
            )
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid choice. Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
