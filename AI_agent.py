import base64
import requests
import io
from PIL import Image, ImageEnhance, ImageFilter

#API_KEY
ENDPOINT = "https://brightskillsai.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2025-01-01-preview"

IMAGE_PATH = "/Users/kevin/Documents/Github/Auto-Blueprints/Blåsväder3_0_fö_20250423_102752.png"

def enhance_image(image_path, scale=2.0):
    try:
        img = Image.open(image_path)

        if scale != 1.0:
            img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)

        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = ImageEnhance.Sharpness(img).enhance(2.0)
        img = img.filter(ImageFilter.EDGE_ENHANCE)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()
    except Exception as e:
        print(f"Enhancement failed: {e}")
        return None

def ask_gpt_with_red_boxes(image_b64):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    system_prompt = """
  Din uppgift:
- Identifiera varje rödmarkerat objekt i ritningen (markerade med röda rutor).
- För varje röd ruta, försök hitta:
    - id: Objektets ID (t.ex. FTF09, FT017, TF10a)
    - type: Typen (window, door, other)
    - width_M: Bredden i modulmått (t.ex. 9M)
    - height_M: Höjden i modulmått (t.ex. 21M)
    - antal: Antal om det finns, annars null

💡 Viktigt:
- Identifiera endast det som är inom de röda rutorna.
- Om något saknas, sätt värdet till null.

🔁 Returnera datan som en JSON-array, exempel:
[
  {
    "id": "FTF09",
    "type": "window",
    "width_M": "9M",
    "height_M": "21M",
    "antal": 4
  }
]
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Här är ritningen. Identifiera alla objekt inom de röda rutorna."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
            ]
        }
    ]

    payload = {
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 1500
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")
        print(response.text)
        return None

def main():
    print("Förbereder bilden...")
    image_b64 = enhance_image(IMAGE_PATH)

    if not image_b64:
        print("Kunde inte bearbeta bilden.")
        return

    print("Skickar till GPT...")
    result = ask_gpt_with_red_boxes(image_b64)

    if result:
        print("Result")
        print(result)
        with open("output_redboxes.json", "w") as f:
            f.write(result)
    else:
        print("Inget resultat.")

if __name__ == "__main__":
    main()
