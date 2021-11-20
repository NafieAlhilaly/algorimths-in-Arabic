"""
    ======= Algorithms =======
    الباب الثالث


    الخوارزميات :
    هي سلسلة من العمليات او الخطوات الواضحة لحل مشكلة معينة في زمن محدد

    تعتبر الخوارزميات هي العمود الفقري لانواع البيانات
    الخوارزميات تساعد في تطبيق العمليات على هياكل البيانات
"""

f"""
    لاحظ المثال التالي لهيكل بيانات 
    student
    {
        class Student:
            id: int
            name: str
            math_scores: int
            science_scores: int
    }
    حاليا هيكل البيانات فقط يقوم بغرض التخزين او الإرجاع مع محدويتها
    لكن ماذا لو اردت  معرفة مجموع الدرجات ؟

    ببساطة تقوم بعمل خوارزمية تحسب لك المجموع
    مثل :

    {
        class Student:
            id: int
            name: str
            math_scores: int
            science_scores: int

            def total_scores():
                total = math_scores + science_scores
                return total
                
        ahmed = Student()
        ahmed.total_scores()
    }

    اذا الخوارزميات تساعد على هيكلة البيانات بشكل افضل
"""

f"""
    تتكون الخوارزمية او البرنامج من 
    Three Constructs

    - Sequence | وهي سلسة من العمليات
    {
        var1: int = 12 """ sequence 1  """
        var2: float = 87.89 """ sequence 2  """
        var3: float = var1 + var2 """ sequence 2  """
        var4: float = var1 * var2 + var2 + ( var2 / var1) """ sequence 2  """
    }

    - Decision | شرط او مجموعة من الشروط تتنفذ في حال تحققها
    {
        """
        واحد فقط من الشروط قد يتحقق ويتم تنفيذة في كل مرة
        """
        if 1 > 2:
            print("not really")
        elif 2 == 0:
            print("not gonna work")
        else:
            print("true")
    }


    - Repetition | حلقات التكرار
    حلقات التكرار تستخدم لعمل تكرار لعدد معين من المرات

    {
        """
        هنا سوف يقوم بتكرار الحلقة من 0 إلى 9
        """
        
        for x in range(10):
            print(x)

        x = 0
        while x < 10:
            print(x)
            x = x+1
    }
"""

"""
    خصائص الخوارزميات :
    - لها خطوات مرتبة و واضحة
    - تعطي نتيجة
    - تنتهي في زمن محدد
"""