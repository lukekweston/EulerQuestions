
import java.lang.Math.sqrt

fun SieveOfEratosthenes(primes: Int):ArrayList<Int>{

    val foundPrimes = arrayListOf<Int>()

    for(i in 0..primes){
        foundPrimes.add(1)
    }

    for(i in 2..Math.sqrt(primes.toDouble()).toInt()){
        if(foundPrimes[i] == 1){
            for(j in i+i..primes step i){
                foundPrimes[j] = 0
            }

        }
    }

    val primesReturn = arrayListOf<Int>()

    for(i in 2..primes - 1){
        if(foundPrimes[i] == 1){
            primesReturn.add(i)
        }
    }

    return primesReturn
}

fun getCirlce(p:Int):ArrayList<Int>{

    var rotations = arrayListOf<Int>()

    var rotate = p.toString()

    for(i in 0..rotate.length - 1){
        rotations.add(rotate.toInt())
        rotate = rotate.substring(1) + rotate.substring(0, 1)

    }

    return rotations

}