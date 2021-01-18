

fun main() {
    //println(SieveOfEratosthenes(100))

    //get a list of the first 1 million primes

    //Loop

    //loop through all primes and for each make a list of the primes rotations

    //check that all primes exist in the 1 million

    //if so count

    //go to next prime

    //print the result

    var primes = SieveOfEratosthenes(1000000)

    var count = 0

    for( p in primes){
        var cirlePrimes = getCirlce(p)
        for(pc in 0..cirlePrimes.count() - 1){
            if(!primes.contains(cirlePrimes[pc])){
                break
            }
            else if( pc == cirlePrimes.count() - 1){
                println(p)
                count += 1
            }
        }


    }

    println("Result: $count")


}