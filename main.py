import requests
import concurrent.futures

def request(user_id, asset_id):
    url = f"https://inventory.roblox.com/v1/users/{user_id}/items/{num}/{asset_id}/is-owned"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Owned: {user_id}, {asset_id}")
        with open("output.txt", "a") as file:
            file.write(f'"{user_id}:{asset_id}"\n')

def user_thread(user_id, asset_ids):
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_c) as executor:
        executor.map(request, [user_id]*len(asset_ids), asset_ids)

def main():
    global thread_c
    thread_c = int(input("Enter the number of threads: "))
    global num
    num = int(input("Enter asset type (1 for asset, 4 for bundle): "))

    with open("user_ids.txt", "r") as user_file:
        user_ids = user_file.read().splitlines()

    with open("asset_ids.txt", "r") as asset_file:
        asset_ids = asset_file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_c) as executor:
        executor.map(user_thread, user_ids, [asset_ids]*len(user_ids))

if __name__ == "__main__":
    main()