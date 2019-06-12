from django.shortcuts import render

def index(request):
    # context = {
    #     'age':16
    # }
    # context = {
    #     'heros':[
    #         '梅西',
    #         '詹姆斯',
    #     ]
    # }
    # context = {
    #     # 'persons':{
    #     #     'username':'kangbazi',
    #     #     'age':18,
    #     #     'height':'181cm'
    #     # }
    #     # 'persons':[
    #     #     '张三',
    #     #     '李四'
    #     # ]
    #     'books':[
    #         {
    #             'name':'金什么梅',
    #             'author':'笑笑生',
    #             'price':123.34
    #         },
    #         {
    #             'name': '三国',
    #             'author': '罗贯中',
    #             'price': 223.34
    #         },
    #         {
    #             'name': '水浒传',
    #             'author': '施耐庵',
    #             'price': 23.34
    #         },
    #         {
    #             'name': '西游记',
    #             'author': '吴承恩',
    #             'price':12.34
    #         },
    #         {
    #             'name': '麻辣烫',
    #             'author': '亮哥',
    #             'price': 66.34
    #         },
    #     ],
    #     'comments':[
    #         '不可多得的好书,很暴力',
    #     ]
    # }

    context = {
        'persons':[
            '张三',
            '李四',
            '王五',
            '赵六'
        ]
    }

    return render(request,'index.html',context=context)