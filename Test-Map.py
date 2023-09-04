from pyecharts.charts import  Map
from pyecharts.options import  VisualMapOpts

map = Map()

data =[
    ("Hamburg",9),
    ("Berlin",89),
    ("Hesse",299),
    ("Saarland",5),
    ("Thuringia",499)
]

map.add("Test-Map",data,"德国")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"lable":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"lable":"10-99","color":"#FF6666"},
            {"min":100,"max":500,"lable":"100-500","color":"#990033"}
        ]
    )
)

map.render("test_map.html")