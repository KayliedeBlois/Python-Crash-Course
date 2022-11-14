sentence = "Just as I arrived at Place, I realized I had forgotten my Object."

place = input("Tell me a place.")

object = input("Now give me an object.")

madLib = sentence.replace("Place", place).replace("Object", object)

print(madLib)