"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
class stitch_calculator():
    def __init__(self):
        pass
    def rectangle_calculator(self, gauge_w, width, s_multiple, s_remainder, gauge_l, length, r_multiple, r_remainder ):
        stitches = self.one_dim_calculator(gauge_w, width, s_multiple, s_remainder)
        rows = self.one_dim_calculator(gauge_l, length, r_multiple, r_remainder)
        return (stitches, rows)

    def one_dim_calculator(self, gauge, x, multiple , remainder):
        estimate = int(x / gauge)
        difference = estimate % multiple
        if difference == remainder:
            return estimate
        elif difference + 1 == remainder:
            return estimate + 1
        else:
            option1 = difference - remainder
            option2 = difference + remainder
            return min((option1, option2))