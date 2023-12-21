import hashlib

def calculate_sha256(text):
    # 將文本轉換為字節
    text_bytes = text.encode('utf-8')

    # 使用hashlib庫創建一個sha256對象
    sha256_hash = hashlib.sha256()

    # 對字節數據進行哈希運算
    sha256_hash.update(text_bytes)

    # 獲取最終的哈希值（16進制格式）
    hash_value = sha256_hash.hexdigest()

    return hash_value

# 測試函數
text = "Hello, World!!"
hash_value = calculate_sha256(text)
print("SHA-256 Hash:", hash_value)
