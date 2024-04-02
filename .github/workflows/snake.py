import requests

def generate_snake_animation(username, size=1, pixel=False, repl=False, emoji=False):
    params = {
        "username": username,
        "size": size,
        "pixel": pixel,
        "repl": repl,
        "emoji": emoji
    }
    response = requests.get("https://github.com/Platane/snk/raw/output/github-contribution-grid-snake.svg", params=params)
    if response.status_code == 200:
        with open("snake_animation.svg", "wb") as f:
            f.write(response.content)
        print("Snake animation generated successfully.")
    else:
        print("Failed to generate snake animation.")

if __name__ == "__main__":
    username = input("Enter your GitHub username: ")
    size = int(input("Enter the size (1-5): "))
    pixel = input("Pixel? (y/n): ").lower() == "y"
    repl = input("REPL.it colors? (y/n): ").lower() == "y"
    emoji = input("Use emoji? (y/n): ").lower() == "y"
    
    generate_snake_animation(username, size=size, pixel=pixel, repl=repl, emoji=emoji)
