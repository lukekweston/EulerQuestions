
fun truncLeft(p:Int, primes:ArrayList<Int>):Boolean{
    var pString = p.toString()

    for(i in 1..pString.length -1){
        pString = pString.substring(1, pString.length)
        if(!primes.contains(pString.toInt())){
            return false
        }
    }
    return true

}

fun truncRight(p:Int, primes:ArrayList<Int>):Boolean{
    var pString = p.toString()

    for(i in 1..pString.length -1){
        pString = pString.substring(0, pString.length -1)
        if(!primes.contains(pString.toInt())){
            return false
        }
    }
    return true

}



fun main() {

    //Get the primes to 1,000,000 - make this list class level to be used everywhere
    //loop through starting from 11 (2-7 not considered truncable)

    //write a method to trunc left and write, strip char 1 by 1 until length == 1 and check all are prime

    //if truncLeft && trunccRight -> primesSum += prime

    //print result

    var primesSum = 0
    var primesCount = 0
    var primes = SieveOfEratosthenes(1000000)
    var primesTest = primes.subList(4,primes.size)


    for(p in primesTest){
        if(truncRight(p, primes) && truncLeft(p, primes)){
            primesCount += 1
            println("truncable: $p")
            primesSum += p
            if(primesCount == 11){
                break
            }
        }

    }
    println("Result : $primesSum")


}