from PIL import Image

class Elevation_Map:
        def __init__(self, width,height):
                self.width = width
                self.height = height
                self.image = Image.new("RGBA", (width, height))
                with open("elevation_small.txt") as file:
                        self.matrix = [[int(line) for line in line.split()] for line in file]
                        self.max_elev = max([max(line) for line in self.matrix]) #find highest max in each line

        def save(self, filename):
            self.image.save(filename)
        
        def draw_point(self, xy , color):
            self.image.putpixel(xy, color)

        def map(self,filename):
            for y, row in enumerate(self.matrix):
                for x, num in enumerate(row):
                        pos = int((num/self.max_elev)*255)
                        self.image.putpixel((x,y),(pos, pos, pos))                        
            return self


if __name__=="__main__":
    
    my_map = Elevation_Map(600,600) 
    my_map = my_map.map("elevation_small.txt")
    my_map.save("map.png")
    my_map.image.show("map.png")