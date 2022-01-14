#Temps
temps_F = [45.7, 55.3, 62.1, 75.4, 32.0, 0.0, 100.0]
# Your code here to map temps_F



original_headings = [(30, 'N'), (359, 'N'), (340, 'N'), (270, 'W'), (124, 'E'), (149, 'S'), (219, 'S')]
# Your code here to map original_headings



s = """
gnidroccA ot lla nwonk swal fo ,noitaiva ereht si on yaw a eeb dluohs eb 
elba ot .ylf stI sgniw era oot llams ot teg sti taf elttil ydob ffo eht 
.dnuorg ehT ,eeb fo ,esruoc seilf yawyna esuaceb seeb t'nod erac tahw snamuh 
kniht si .elbissopmi
"""
# Your code here to map s




# Your code below to transform a vector using map
def linear_transform(vector, scale, shift):
    """
    Takes in a vector (list of numbers), a scale factor, and a shift constant and returns the vector
    where the ith term is equivalent to the ith term of the original vector multiplied by the scale
    and added to the shift.
    >>> linear_transform([1,2], 5, 6)
    [11, 16]
    """
    pass




def convert_times(times):
    """
    takes the horses' times (in terms of # seconds / 1.25 miles) and returns the horses' 100
    yard dash times (# seconds / 100 yards). Assume that the horses run at a constant speed
    and at the same pace as in their Kentucky Derby times. For reference, there are 1760 yards
    in 1 mile. Use your map lambda skills :)
    >>> convert_times([121.3, 124.1, 119.7, 122.4])
    [5.513636363636364, 5.640909090909091, 5.440909090909091, 5.5636363636363635]
    """
    pass