import matplotlib.pyplot as plt


class PlotHelper():
    def __init__(self, dataset, title='sample'):
        self.dataset = dataset
        self.title = title

    def draw_plot(self, key1, key2):
        for key in self.dataset:
            x = self.dataset[key][key1]
            y = self.dataset[key][key2]
            plt.scatter(x, y, label=key, edgecolors='none')
            plt.annotate(key,  # this is the text
                         (x, y),  # this is the point to label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')
        plt.title(self.title)
        plt.xlabel(key1)
        plt.ylabel(key2)

        # increase axes range
        bottom, top = plt.ylim()
        plt.ylim((bottom-1, top+1))
        left, right = plt.xlim()
        plt.xlim((left-1, right+1))

        plt.tight_layout(pad=2, w_pad=0.5, h_pad=1.0)

        plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

        plt.show()
        return

    def get_minkowski_distance(self, rating1, rating2, q):
        distance = 0
        commonRatings = False
        for key in rating2:
            if key in rating2:
                distance += pow(abs(rating1[key]-rating2[key]), q)
                commonRatings = True
            if(commonRatings):
                return pow(distance, 1/q)
            else:
                return 0

    def get_minkowski_distance(self, rating1, rating2, q):
        distance = 0
        commonRatings = False
        for key in rating2:
            if key in rating2:
                distance += pow(abs(rating1[key]-rating2[key]), q)
                commonRatings = True
            if(commonRatings):
                return pow(distance, 1/q)
            else:
                return 0

    def get_minkowski_distance(self, rating1, rating2, q):
        distance = 0
        commonRatings = False
        for key in rating2:
            if key in rating2:
                distance += pow(abs(rating1[key]-rating2[key]), q)
                commonRatings = True
            if(commonRatings):
                return pow(distance, 1/q)
            else:
                return 0


def get_minkowski_distance(rating1, rating2, q):
    distance = 0
    commonRatings = False
    for key in rating2:
        if key in rating2:
            distance += pow(abs(rating1[key]-rating2[key]), q)
            commonRatings = True
        if(commonRatings):
            return pow(distance, 1/q)
        else:
            int.sys
            return 0
