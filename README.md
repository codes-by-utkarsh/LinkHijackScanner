# 🔗 LinkHijackScanner

LinkHijackScanner is a Python-based **social media broken link checker** designed for **pentesters, bug bounty hunters, and security teams**.  

It crawls a target website, extracts **social media profile links** (LinkedIn, Instagram, YouTube, Twitter/X), and checks whether they are:
- ✅ Valid  
- ❌ Broken / Not Found (potentially hijackable)  
- ⚠️ Unusual (redirects, errors, unexpected responses)  

This helps detect **social media account takeover risks** caused by dangling links.

---

## 🚀 Features
- Extracts links from **LinkedIn, Instagram, YouTube, Twitter/X**.  
- Detects hijackable links by flagging invalid/broken profiles.  
- Simple CLI tool, lightweight, fast.  
- Works with both HTTP & HTTPS sites.  

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/LinkHijackScanner.git
cd LinkHijackScanner
pip install -r requirements.txt
```
