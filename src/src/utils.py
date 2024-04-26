async def like_format(query: str | None):
    if query is None:
        return "%"
    else:
        return f"%{query}%"
