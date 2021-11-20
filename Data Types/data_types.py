"""
========== Data Types =============

الباب الأول


data type 
او انواع البيانات

هو اسلوب لبناء نماذج لحفظ البانات في جهاز الكمبيوتر واسترجاعها

عندما تقوم بتعريف كلاس فأنت تقوم بإنشاء نوع بيانات جديد في اللغة المستخدمة للتعريف
"""

f"""
    ينقسم البرنامج او الخوارزمية إلى :
    - بيانات
    البيانات مثل الارقام او النصوص
    {
        number = 1
        string = "a string"

}
"""

f"""
    - عمليات 
    العمليات مثل الجمع والطرح
    {
        result1 = 1 + 1
        result2 = 2 * 9 + (2/5)
}
"""


f"""
    تكون البيانات بأحد الأشكال التالية :
    - أولية | Scalar or premitive data types
    يراد بالأنواع البيانات الأولية هنا البسيطة التي تأتي مدمجة مع اللغة مثل :
    integer, float, string, boolean ..etc
    {
        variable1: int = 12 # Integer
        variable2: float = 69.89 # Float
        variable3: str = "nafie" # String
        variable4: bool = True # Boolean
    }
"""

f"""
    - مركبة | composite data types
    البيانات المركبة تكون من إنشاء المستخدم بالإعتماد على البيانات الأولية مثل
    الكلاسات التي يعرفها المسخدم
    {
        class Animal:
            """
            نوع معرف من قبل المستخدم
            """
            id: int
            name: str
            age: int

        class Car:
            """
            نوع معرف من قبل المستخدم
            """
            id: int
            name: str
            model: str
            max_speed: float

    }
"""


f"""
- معقدة | complex data type

انواع البيانات المعقدة تكون خليط من الأنواع السابقة
{
    class Student:
        id: int
        name: str
    class University:
        id: int
        name: str
        
        """
        متغير نوعه
        Student
        من الكلاس السابق المعرف من قبل المستخدم
        """
        student1: Student
}
"""


"""
معلومة عن البايثون :

في الحقيقة البايثن ليس لديها اواع اولية لان كل شيء في البايثون 
يعتبر كائن او نوع مركب

لمعلومات أكثر:
https://stackoverflow.com/questions/50534394/what-does-it-mean-by-passed-by-assignment
"""