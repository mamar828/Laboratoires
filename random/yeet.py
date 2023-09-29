import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


def linear_function(
        x: float,
        n: float,
        c: float
):
    """
    Defines the linear function as y = nx + c.

    Parameters
    ----------
    x: float
        The independent variable.
    n: float
        The slope of the linear function.
    c: float
        The initial value at x=0.

    Returns
    -------
    y: float
        The result of the computation of y = nx + c.
    """
    return x*n + c


cough_data = np.array([
    [1, 1.309074],
    [2, 13.303334],
    [3, 22.986757],
    [4, 57.138864],
    [5, 92.710502],
    [6, 109.196103],
    [7, 121.104485],
    [8, 134.73874],
    [9, 146.536346],
    [10, 155.267357],
    [11, 161.430652],
    [12, 163.599537],
    [13, 179.646303],
    [14, 195.579392],
    [15, 222.40948],
    [16, 228.360849],
    [17, 236.937637],
    [18, 246.990543],
    [19, 260.163148],
    [20, 290.815082],
    [21, 309.549865],
    [22, 328.144802],
    [23, 336.817265],
    [24, 338.744484],
    [25, 341.504181],
    [26, 355.013342],
    [27, 358.806338],
    [28, 388.910976],
    [29, 397.177176],
    [30, 415.597743],
    [31, 430.763436],
    [32, 434.138442],
    [33, 468.004515],
    [34, 475.779976],
    [35, 483.339317],
    [36, 483.810668],
    [37, 518.525415],
    [38, 519.070381],
    [39, 533.300792],
    [40, 552.229333],
    [41, 567.160013],
    [42, 579.446623],
    [43, 586.734695],
    [44, 614.037575],
    [45, 646.733274],
    [46, 653.649574],
    [47, 654.049353],
    [48, 678.109722],
    [49, 745.208797],
    [50, 758.171821],
    [51, 770.059321],
    [52, 782.85036],
    [53, 805.036269],
    [54, 820.940395],
    [55, 828.143212],
    [56, 830.855469],
    [57, 859.841782],
    [58, 860.245469],
    [59, 884.433347],
    [60, 885.253953],
    [61, 951.143586],
    [62, 979.797184],
    [63, 985.134543],
    [64, 1010.270785],
    [65, 1011.178137],
    [66, 1015.689997],
    [67, 1021.603782],
    [68, 1051.076831],
    [69, 1058.423073],
    [70, 1071.259518],
    [71, 1094.993458],
    [72, 1106.869217],
    [73, 1140.485635],
    [74, 1145.399359],
    [75, 1164.17004],
    [76, 1166.852467],
    [77, 1181.304294],
    [78, 1205.661946],
    [79, 1212.706873],
    [80, 1254.275823],
    [81, 1254.275878],
    [82, 1290.761974],
    [83, 1295.125327],
    [84, 1313.29665],
    [85, 1322.161903],
    [86, 1357.274384],
    [87, 1371.752282],
    [88, 1385.95181],
    [89, 1387.563131],
    [90, 1406.937394],
    [91, 1443.221584],
    [92, 1450.419864],
    [93, 1458.727086],
    [94, 1533.863847],
    [95, 1557.32514],
    [96, 1565.807531],
    [97, 1575.195839],
    [98, 1594.18418],
    [99, 1609.329183],
    [100, 1616.912415],
    [101, 1664.116136],
    [102, 1688.326507],
    [103, 1700.19525],
    [104, 1704.183425],
    [105, 1746.204706],
    [106, 1789.82302],
    [107, 1799.65243],
    [108, 1810.871599],
    [109, 1819.818722],
    [110, 1845.545192],
    [111, 1853.789925],
    [112, 1892.376848],
    [113, 1932.291301],
    [114, 1955.824231],
    [115, 1991.83779],
    [116, 2000.018145],
    [117, 2019.066136],
    [118, 2020.674218],
    [119, 2041.287895],
    [120, 2086.937103],
    [121, 2096.191753],
    [122, 2118.844198],
    [123, 2127.13405],
    [124, 2150.64585],
    [125, 2153.77471],
    [126, 2170.649506],
    [127, 2170.883642],
    [128, 2171.364567],
    [129, 2171.794139],
    [130, 2200.259336],
    [131, 2241.456005],
    [132, 2247.475319],
    [133, 2273.882828],
    [134, 2288.178715],
    [135, 2323.284845],
    [136, 2347.925015],
    [137, 2363.760542],
    [138, 2370.643359],
    [139, 2397.95036],
    [140, 2401.958312],
    [141, 2418.163132],
    [142, 2440.833936],
    [143, 2471.617376],
    [144, 2471.9972],
    [145, 2524.276921],
    [146, 2529.770924],
    [147, 2530.41687],
    [148, 2535.829265],
    [149, 2548.080311],
    [150, 2560.821173],
    [151, 2602.00089],
    [152, 2606.706145],
    [153, 2634.669614],
    [154, 2639.257437],
    [155, 2658.508692],
    [156, 2667.960513],
    [157, 2684.373409],
    [158, 2690.625366],
    [159, 2707.090503],
    [160, 2727.726907],
    [161, 2760.89054],
    [162, 2772.164888],
    [163, 2781.595791],
    [164, 2819.823029],
    [165, 2835.703423],
    [166, 2841.83243],
    [167, 2849.635206],
    [168, 2855.375769],
    [169, 2861.856313],
    [170, 2881.390273],
    [171, 2888.131104],
    [172, 2894.231819],
    [173, 2895.544175],
    [174, 2904.292323],
    [175, 2904.727423],
    [176, 2908.365391],
    [177, 2939.844658],
    [178, 2957.538055],
    [179, 2974.056517],
    [180, 3018.134181],
    [181, 3029.243179],
    [182, 3079.688786],
    [183, 3105.618851],
    [184, 3135.154937],
    [185, 3146.784878],
    [186, 3181.642965],
    [187, 3181.643114],
    [188, 3185.160836],
    [189, 3212.513966],
    [190, 3241.035891],
    [191, 3243.825285],
    [192, 3244.068763],
    [193, 3276.588749],
    [194, 3288.305141],
    [195, 3301.76033],
    [196, 3301.998797],
    [197, 3314.52803],
    [198, 3340.158546],
    [199, 3353.098415],
    [200, 3386.073243],
    [201, 3392.628917],
    [202, 3399.747313],
    [203, 3414.964923],
    [204, 3423.593286],
    [205, 3426.709467],
    [206, 3433.965834],
    [207, 3439.752373],
    [208, 3444.177709],
    [209, 3450.808778],
    [210, 3457.181717],
    [211, 3457.826804],
    [212, 3476.870683],
    [213, 3487.5634],
    [214, 3500.827996],
    [215, 3523.973516],
    [216, 3556.367991],
    [217, 3560.173526],
    [218, 3568.696072],
    [219, 3569.293242],
    [220, 3583.430309],
    [221, 3585.935274],
    [222, 3595.350216],
    [223, 3600.534497],
    [224, 3628.571251],
    [225, 3632.229925],
    [226, 3645.859521],
    [227, 3656.132384],
    [228, 3661.585734],
    [229, 3679.564394],
    [230, 3690.297509],
    [231, 3707.77088],
    [232, 3728.79625],
    [233, 3746.970673],
    [234, 3758.228283],
    [235, 3783.869362],
    [236, 3795.334185],
    [237, 3795.952656],
    [238, 3815.421375],
    [239, 3821.489827],
    [240, 3828.79059],
    [241, 3875.099292],
    [242, 3903.119012],
    [243, 3909.029785],
    [244, 3913.004827],
    [245, 3925.59659],
    [246, 3959.577411],
    [247, 3967.785028],
    [248, 3971.953549],
    [249, 4010.417106],
    [250, 4012.796184],
    [251, 4026.262219],
    [252, 4042.525041],
    [253, 4054.989632],
    [254, 4060.988787],
    [255, 4074.00229],
    [256, 4089.478506],
    [257, 4132.21042],
    [258, 4140.928697],
    [259, 4148.108469],
    [260, 4159.602779],
    [261, 4175.541062],
    [262, 4182.353823],
    [263, 4201.197122],
    [264, 4212.750963],
    [265, 4231.860214],
    [266, 4242.090976],
    [267, 4243.160368],
    [268, 4272.669791],
    [269, 4277.462202],
    [270, 4314.336909],
    [271, 4331.324391],
    [272, 4341.872062],
    [273, 4360.768562],
    [274, 4365.21746],
    [275, 4389.29848],
    [276, 4393.252461],
    [277, 4438.909848],
    [278, 4444.218485],
    [279, 4493.262634],
    [280, 4498.726431],
    [281, 4502.31933],
    [282, 4526.532294],
    [283, 4565.720677],
    [284, 4597.500792],
    [285, 4625.561906],
    [286, 4649.776382],
    [287, 4665.480535],
    [288, 4674.9043],
    [289, 4681.901712],
    [290, 4684.595561],
    [291, 4719.824731],
    [292, 4727.624832],
    [293, 4753.714405],
    [294, 4801.607888],
    [295, 4814.348056],
    [296, 4816.840947],
    [297, 4829.693122],
    [298, 4843.828255],
    [299, 4868.51355],
    [300, 4886.206611],
    [301, 4897.47335],
    [302, 4901.977366],
    [303, 4929.187672],
    [304, 4935.276826],
    [305, 4957.804861],
    [306, 4977.896045],
    [307, 4994.095488],
    [308, 5006.105779],
    [309, 5029.09485],
    [310, 5123.936877],
    [311, 5164.672653],
    [312, 5176.840532]
])

m, b = np.polyfit(cough_data[:, 1], cough_data[:, 0], 1)
popt, pcov = curve_fit(linear_function, cough_data[:, 1], cough_data[:, 0])
y_pred = linear_function(cough_data[:, 1], *popt)
r2 = r2_score(cough_data[:, 0], y_pred)

fig, axe = plt.subplots(figsize=(16, 10))

axe.plot(cough_data[:, 1], cough_data[:, 1] * m + b, c="#FF2F3F", linewidth=3)
axe.scatter(cough_data[:, 1], cough_data[:, 0], c="#000000", s=10)

axe.legend(["Linear regression", "Cumulative coughs"], fontsize=16)

axe.text(300, 110, f"f(t) = {m:.4f}t + {b:.4f}", {"c": "#000000", 'fontsize': 16})
axe.text(300, 95, f"$R^2$: {r2:.4f}", {"c": "#000000", 'fontsize': 16})

axe.set_xlabel("Time [s]", fontsize=16)
axe.set_ylabel("Cumulative instances [Coughs]", fontsize=16)

plt.show()
