Here's a **comprehensive API documentation** for your **Crypto Market API**, similar to what you’d see in **Swagger/OpenAPI**.  

---

# 📌 **Crypto Market API Documentation**
🚀 **Version: 1.0**  
🔑 **Authentication: API Key (Query Parameter: `api_key`)**  
🌍 **Base URL:** `http://your-api-domain.com`  

---

## 📍 **Authentication**
All endpoints require an **API Key** as a query parameter.  
**Example:**  
```
?api_key=123
```
Available API Keys: `123`, `456`, `789`  
If an invalid or missing API key is provided, a `401 Unauthorized` or `422 Unprocessable Entity` error will be returned.

---

## 🏥 **Health Check**  
🔗 **Endpoint:**  
`GET /health`  
📜 **Description:** Checks if the API is running.  

✅ **Response:**  
```json
{
  "status": "healthy",
  "version": "1.0"
}
```

---

## 🪙 **List Coins**  
🔗 **Endpoint:**  
`GET /coins`  
📜 **Description:** Fetches a paginated list of cryptocurrency market data.  

📥 **Query Parameters:**  
| Parameter  | Type   | Required | Default | Description |
|------------|--------|----------|---------|-------------|
| `api_key`  | `str`  | ✅ Yes   | `None`  | API Key for authentication. |
| `page_num` | `int`  | ❌ No    | `1`     | Page number for pagination. |
| `per_page` | `int`  | ❌ No    | `10`    | Number of coins per page. |

✅ **Response Example:**  
```json
[
  {
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "btc",
    "current_price": 64830.5
  },
  {
    "id": "ethereum",
    "name": "Ethereum",
    "symbol": "eth",
    "current_price": 3130.2
  }
]
```

---

## 📂 **List Coin Categories**  
🔗 **Endpoint:**  
`GET /categories`  
📜 **Description:** Fetches a paginated list of cryptocurrency categories.  

📥 **Query Parameters:**  
| Parameter  | Type   | Required | Default | Description |
|------------|--------|----------|---------|-------------|
| `api_key`  | `str`  | ✅ Yes   | `None`  | API Key for authentication. |
| `page_num` | `int`  | ❌ No    | `1`     | Page number for pagination. |
| `per_page` | `int`  | ❌ No    | `10`    | Number of categories per page. |

✅ **Response Example:**  
```json
[
  {
    "id": "defi",
    "name": "Decentralized Finance"
  },
  {
    "id": "gaming",
    "name": "Gaming and Metaverse"
  }
]
```

---

## 💰 **Get Coin Details**  
🔗 **Endpoint:**  
`GET /coin/{coin_id}`  
📜 **Description:** Fetches details of a specific cryptocurrency.  

📥 **Path Parameters:**  
| Parameter  | Type   | Required | Description |
|------------|--------|----------|-------------|
| `coin_id`  | `str`  | ✅ Yes   | The ID of the cryptocurrency (e.g., `bitcoin`, `ethereum`). |

📥 **Query Parameters:**  
| Parameter  | Type   | Required | Default | Description |
|------------|--------|----------|---------|-------------|
| `api_key`  | `str`  | ✅ Yes   | `None`  | API Key for authentication. |

✅ **Response Example:**  
```json
{
  "id": "bitcoin",
  "name": "Bitcoin",
  "symbol": "btc",
  "current_price": 64830.5
}
```

🚨 **Error Handling:**  
- If the coin does not exist, returns:  
  ```json
  {
    "detail": "Coin not found"
  }
  ```
  **Status Code:** `404 Not Found`

---

# 🛠 **Testing Endpoints**
### 📌 **Test Suite Setup**
This API includes unit tests written with **pytest** and **FastAPI TestClient**.

### 🚀 **Run Tests**
```bash
pytest test_main.py
```

### ✅ **Test Cases**
| Test Case                 | Endpoint               | Expected Result |
|---------------------------|-----------------------|----------------|
| `test_health_check`       | `GET /health`         | `{ "status": "healthy", "version": "1.0" }` |
| `test_unauthorized_access` | `GET /coins`          | `422 Unprocessable Entity` |
| `test_invalid_authentication` | `GET /coins?api_key=wrong_key` | `401 Unauthorized` |
| `test_list_coins`         | `GET /coins?api_key=123&page_num=1&per_page=5` | Returns a list of coins |
| `test_list_categories`    | `GET /categories?api_key=456&page_num=1&per_page=5` | Returns a list of categories |
| `test_get_coin`           | `GET /coin/bitcoin?api_key=123` | Returns details of Bitcoin |

---

# 📘 **Error Responses**
### 🔴 **401 Unauthorized**
Occurs when an invalid API key is used.  
```json
{
  "detail": "Unauthorized"
}
```

### 🔴 **404 Not Found**
Occurs when requesting a coin that does not exist.  
```json
{
  "detail": "Coin not found"
}
```

### 🔴 **422 Unprocessable Entity**
Occurs when API key is missing.  
```json
{
  "detail": "Unprocessable Entity"
}
```

---

# 📜 **Conclusion**
This API allows users to fetch real-time cryptocurrency market data, coin categories, and specific coin details using the **CoinGecko API**.  
Authentication is done via API keys. 🚀
