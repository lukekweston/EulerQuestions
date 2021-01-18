
//Recursively get the factors
fun fact(factor: Int):Int{

    if(factor == 1){
        return 1
    }
    else{
        return factor * fact(factor -1)
    }
}


//Sum the digits in a total number factors
fun sum(number: Int):Int{

    var sum = 0

    for(c in number.toString()){
        sum += numbers[c.toInt() - 48]
    }

    return sum

}

//List that holds the pre calculated factors
val numbers = arrayListOf<Int>()

fun main() {

    var totalCurious = 0

    //Special case, 0! = 1
    numbers.add(1)

    //Fill out the pre calculated list
    for(i in 1..9){
        numbers.add(fact(i))
        println(fact(i))
    }

    //Check up to 1,000,000 - could be sped up by rejecting numbers right away that will be smaller than the total
    //example 189 - has 9 which 9! = 362,860
    for(i in 3..1000000){
        if (i == sum(i)){
            println(i)
            totalCurious += i
        }
    }
    println("Result: $totalCurious")

}