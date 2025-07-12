const ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36";

fetch("https://api.internal.temp-mail.io/api/v3/email/new", {
  method: "POST",
  headers: {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "application-name": "web",
    "application-version": "4.0.0",
    "content-type": "application/json",
    "User-Agent": ua
  },
  body: JSON.stringify({
    "name": "xx1",        // desired local part (username)
    "domain": "grgrgr.com" // desired domain (must be supported/public)
  })
})
.then(res => res.json())
.then(data => {
  if (data.email) {
    console.log("Custom email created:", data.email);
  } else {
    console.error("Failed to create custom email", data);
  }
})
.catch(console.error);


https://api.internal.temp-mail.io/api/v4/domains
