
# python file to generate different color variations using hsla color scheme

class hsla_color: 
    def __init__(self, hue, sat, lum, alpha): 
        self.hue = str(hue)
        self.sat = str(sat)
        self.lum = str(lum)
        self.alpha = str(alpha)


# global list of variations
variations_names = ["lightest", "lighter", "light", "dark", "darker", "darkest"]
luminances = [24, 16, 8, -8, -16, -24]

# function wrapper for generation code
def printVariations(input_color_name, input_color): 
    for i in range(len(variations_names)): 
        output = input_color_name + '-' + variations_names[i] + ': hsla(' + input_color.hue + ', ' + input_color.sat + '%, '+ str(int(input_color.lum) + luminances[i]) + '%, ' + input_color.alpha + ');'
        print(output)

# print variations
printVariations("color-1", hsla_color(210, 33, 66, 1))
printVariations("color-2", hsla_color(265, 33, 66, 1))
printVariations("color-3", hsla_color(120, 33, 66, 1))