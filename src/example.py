from CLR import Renderer

renderer = Renderer()
res = renderer.renderIMG("testIMG.jpg", (32, 32), 9)

print(res)