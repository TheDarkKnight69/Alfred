  if any(word in message.content for word in sad_words):
    await message.channel.send("React to get a compliment DM'ed to you!! ")
    await message.add_reaction('<:ducklove:955328384546791455>')
    await message.author.send(compliment)