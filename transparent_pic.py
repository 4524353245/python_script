import PIL.Image as Image #导入image函数
def transparent_png(imgfile,out="out"): 
    img = Image.open(imgfile)
    img = img.convert('RGBA') 
    W, H = img.size 
    white_pixel = (255, 255, 255, 255)  
    for w in range(W):   ###循环图片的每个像素点
        for h in range(H):  
            if img.getpixel((w,h)) == white_pixel:  
                img.putpixel((w,h),(0,0,0,0))
    img.save(out+".png")
transparent_png('forkme.jpg','new_transparent')