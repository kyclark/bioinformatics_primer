PRG="../commoner.py"
FX='fox.txt'
AM='american.txt'
BR='british.txt'
NB='nobody.txt'

$PRG $FX $FX > 'fox-fox.out'

$PRG $FX $FX -t > 'fox-fox.table.out'

$PRG $FX $FX -m 4 > 'fox-fox.min4.out'

$PRG $FX $FX -m 10 > 'fox-fox.min10.out'

$PRG $NB $FX > 'fox-nobody.out'

$PRG -m 3 $NB $FX > 'fox-nobody.min3.out'

$PRG -t -m 3 $NB $FX > 'fox-nobody.table.min3.out'

$PRG -m 5 $NB $FX > 'fox-nobody.min5.out'

$PRG $AM $BR > 'am-br.out'

$PRG -t $AM $BR > 'am-br.table.out'

$PRG -m 3 $AM $BR > 'am-br.min3.out'

$PRG -t -m 3 $AM $BR > 'am-br.table.min3.out'

$PRG -n 1 -m 4 $AM $BR > 'am-br.min4.n1.out'

$PRG -n 1 -t -m 4 $AM $BR > 'am-br.table.min4.n1.out'

$PRG -n 2 -m 3 $AM $BR > 'am-br.min3.n2.out'

$PRG -n 2 -t -m 3 $AM $BR > 'am-br.table.min3.n2.out'
