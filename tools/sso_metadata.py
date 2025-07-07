# tools/sso_metadata.py
import sys

def show_mock_metadata():
    print("""
<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
    entityID="https://example-idp.com">
  <IDPSSODescriptor>
    <SingleSignOnService 
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
      Location="https://example-idp.com/sso" />
    <KeyDescriptor use="signing">
      <KeyInfo>
        <X509Data>
          <X509Certificate>MIIC...FAKE-CERT-HERE...IDAQAB</X509Certificate>
        </X509Data>
      </KeyInfo>
    </KeyDescriptor>
  </IDPSSODescriptor>
</EntityDescriptor>
""")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sso_metadata.py <idp-url>")
        sys.exit(1)
    print(f"Fetching SSO metadata from {sys.argv[1]}...\n")
    show_mock_metadata()
