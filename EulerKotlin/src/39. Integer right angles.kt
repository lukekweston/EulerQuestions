import kotlin.math.roundToInt

fun main() {
    //loop through 12 - 1000 (p)
        //loop 1,p / 2 (a)
            //loop p / 2,1 (b)
                //((a**2 + b**2)**0.5 = c
                //if(a+b+c == p) count per

    var maxTriangles = 0
    var maxP = -1

    for(p in 12..1000){
        var foundTriangles:ArrayList<ArrayList<Int>> = arrayListOf(arrayListOf<Int>())
        for(a in 1..p /2){
            for (b in p/2 downTo 1){
                var c = Math.sqrt(((a * a) + (b * b)).toDouble())
                if(a+b+c.toInt() == p && c - c.toInt() == 0.0){
                    var triangle = arrayListOf<Int>(a, b, c.toInt())
                    triangle.sort()
                    if(!foundTriangles.contains(triangle)){
                        foundTriangles.add(triangle)
                    }
                }
            }
        }
        if(foundTriangles.size > maxTriangles){
            maxTriangles = foundTriangles.size
            maxP = p
        }

    }

    println("Perimeter that has max right abgle triangles is: $maxP with $maxTriangles triangles")


}