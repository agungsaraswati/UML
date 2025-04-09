from elevenlabs.client import ElevenLabs

# Ganti dengan API key kamu
client = ElevenLabs(api_key="sk_3abbf75a9f3f87134b25d0f31475450015d259c0eb2cac8a")

audio = client.generate(
    text="Halo Petualang, Selamat Menikmati Perjalanan Anda",
    voice="Rachel",
    model="eleven_monolingual_v1"
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("✅ Audio berhasil dibuat sebagai 'output.mp3'")
