python_devs = {"pepa","python", "jirka": "python", "honza": "python", "martin": "python", "petr": "python"}
java_devs = {"pepa","java", "jirka": "java", "honza": "java", "martin": "java", "janka": "java"}

#operace sjednoceni (nebo)
vsichni_devs = python_devs | java_devs
print("vsichni vyvojari (sjednoceni):", vsichni_devs)

#operace prunik (A)
polyglot_devs = python_devs & java_devs
print("vyvojari kteri umi oboje (prunik):", polyglot_devs)


      
      