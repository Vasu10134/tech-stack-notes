# 📌 JSON (JavaScript Object Notation)
 
## What is JSON
#### • Lightweight, text-based format to store & exchange data
#### • Easy for humans to read & machines to parse
#### • Derived from JavaScript, but supported by almost every language
#### • Common use: APIs, configs, and data transfer
### Think of JSON like a digital notepad storing **key : value** data cleanly.
---

## JSON Data Flow : From Server to Client

### Backend (Server):
```bash
json Data → JS Object → JSON.stringify() → JSON string
```

### Frontend (Client):
```bash
Receive JSON string → JSON.parse() → usable JS object
```

### Example:
#### const jsonStr = '{"name":"Mohit","age":30}';
#### const obj = JSON.parse(jsonStr);
#### console.log(obj.name);   // Mohit
---

## ⚔️ JSON vs XML: A Quick Comparison
  
|   Feature   |        JSON            |         XML           |
|-------------|------------------------|-----------------------|
| Readability | Simple, clean          | Verbose, messy        |
| Data Size   | Compact, light         | Larger due to tags    |
| Parsing     | Easy in JS, Python     | Needs extra libs      |
| Popularity  | Dominates in APIs      | Mostly legacy systems |
  
#### JSON wins in 95% of modern web use-cases.
---

## 🧱 JSON Structure
### 1. Object:
```bash
{ "name": "Mohit", "age": 30 }
```
#### Curly braces **{}** with key-value pairs
#### Keys: strings | Values: any valid type
  
### 2. Array:
```bash
{ "fruits": ["apple", "banana", "cherry"] }
```
#### Square brackets **[]** holding ordered values
---

## 🔤 JSON Data Types
#### • String: "text"
#### • Number: 10, 3.14
#### • Boolean: true, false
#### • Array: [1, 2, 3]
#### • Object: { "a": 1 }
#### • Null: null
---
  
## 🛠️ Applications of JSON
#### • APIs: Most web APIs return JSON
#### • Config Files: Used in **.json** config setups (Node, React, etc.)
#### • Databases: MongoDB uses JSON-like BSON format
#### • Data Transfer: Core of frontend-backend communication
---
  
## 🧠 Conclusion
### JSON is non-negotiable for modern devs. Mastering it means you can:
#### • Build APIs
#### • Parse data easily
#### • Structure backend/frontend interactions smoothly
---
  
