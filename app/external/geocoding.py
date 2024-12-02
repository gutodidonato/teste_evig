import httpx

async def geocode_address(address: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json")
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return float(data['lat']), float(data['lon'])
    return 0.0, 0.0  # Retorna zero se não encontrar