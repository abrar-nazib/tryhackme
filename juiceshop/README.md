# Owasp Juice Shop

- Null Termination URL Technique: %2500 -> here, %25 = %
- Json Web Tokens are Base64url encoded. Base64 encoding and Base64 URL encoding are completely different things
  - `signature = HMAC-SHA256(base64urlEncode(header) + '.' + base64urlEncode(payload), secret_key)`
