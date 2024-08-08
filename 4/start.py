# import fun1
#
# fun1.dodaj()

import pakiet
from pakiet import fun
import pakiet.fun as pk  # import pliku jako alias
import pakiet.fun2 as pk2

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# Dopiero po dopisaniu w __init__.py importu tej metody
pakiet.powitanie()
# Cześć
fun.powitanie()  # Cześć
pk.powitanie()  # Cześć
pk2.powitanie_fun2()  # CZesć 2
