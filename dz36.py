import asyncio
import aiohttp

async def get_repositories(username):
    url = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()
                repositories = [repo["full_name"] for repo in json_data.get("repos_url")]
                print(f"Репозитории пользователя {username}:")
                for repo in repositories:
                    print(repo)
            else:
                print(f"Ошибка при получении данных пользователя {username}")

# Список пользователей
users = [
    "Arantir1",
    "EgorTimofeychik",
    "maximax15",
    "letov2110",
    "denirix",
    "Noowkies",
    "NikDychek",
    "marinamonit",
    "PolonskyIllya",
    "temabuchka88",
    "LuydmilaKot",
    "katherinepcholka",
    "telenchenkosergey"
]

async def main():
    tasks = [get_repositories(user) for user in users]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
