import requests

#GET
get_one = requests.get("https://jsonplaceholder.typicode.com/posts")
first_get = get_one.json()
print(first_get)

get_two = requests.get("https://jsonplaceholder.typicode.com/posts/1")
second_get = get_two.json()
print(second_get)

get_user = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
third_get = get_user.json()
print(third_get)

get_comment = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
fourth_get = get_comment.json()
print(fourth_get)

# POST
new_post = {
    "title": "My New Post",
    "body": "This is the content of my post.",
    "userId": 1
}
first_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
post_response = first_post.json()
print(post_response)

# PUT
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Completely new content.",
    "userId": 1
}
first_put = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
put_response = first_put.json()
print(put_response)

#PATCH
updated_patch = {
    "title": "Only the Title Changed"
}
first_patch = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=updated_patch)
patch_response = first_patch.json()
print(patch_response)

# DELETE
first_delete = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
delete_response = first_delete.json()
print(delete_response)

next_post = {
    "username": "emilys",
    "password": "emilyspass"
}
second_post = requests.post("https://dummyjson.com/auth/login", json=next_post)
token_needed = second_post.json()
print(token_needed)

auth_get = requests.get("https://dummyjson.com/auth/me", headers={"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3NzAzNTAxODksImV4cCI6MTc3MDM1Mzc4OX0.ZDhDvpTTmbvUb1gyogrZQyxHIphbIe4_LOZYOL5IIS4"})
next_get = auth_get.json()
print(next_get)

bad_log = {
    "username": "emilys",
    "password": "wrongpassword"
}
incorrect_pass = requests.post("https://dummyjson.com/auth/login", json=bad_log)
wrong_pass = incorrect_pass.json()
print(wrong_pass)

#Exercize 7:
get_products = requests.get("https://dummyjson.com/products?limit=5")
products_list = get_products.json()
print(products_list)

get_specific = requests.get("https://dummyjson.com/products/1")
one_product = get_specific.json()
print(one_product)

# POST
new_product = {
    "title": "New Product",
    "price": 99.99,
    "description": "A test product",
    "category": "electronics"
}
add_product = requests.post("https://dummyjson.com/products/add", json=new_product)
product_response = add_product.json()
print(product_response)

# PUT
updated_product = {
    "title": "Updated Product Name",
    "price": 149.99
}
edit_product = requests.put("https://dummyjson.com/products/1", json=updated_product)
edit_response = edit_product.json()
print(edit_response)


# DELETE
delete_product = requests.delete("https://dummyjson.com/products/1")
remove_product = delete_product.json()
print(remove_product)
